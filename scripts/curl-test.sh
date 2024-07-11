#!/bin/bash

# CHECKING IF JQ IS INSTALLED
if !command -v jq &> /dev/null; then
    echo "jq is not installed. Please install jq to proceed."
    echo "Debian OS: sudo apt-get install jq"
    echo "Mac OS: brew install jq"
    exit 1
fi



# CONSTANTS
url="http://127.0.0.1:5000/api/timeline_post"
random_number=$((RANDOM))

# POST BODY + API RESPONSE
name="Ethan_$random_number"
email="ethan_$random_number@example.com"
content="This is a test post with a random number: $random_number"
post_response=$(curl -s $url -X POST -d "name=$name&email=$email&content=$content&password=$random_number" )

# TESTING POST RESPONSE
if [[ $(echo "$post_response" | jq -e --arg name "$name" '.name == $name') > /dev/null && \
      $(echo "$post_response" | jq -e --arg email "$email" '.email == $email') > /dev/null && \
      $(echo "$post_response" | jq -e --arg content "$content" '.content == $content') > /dev/null ]]; then
    echo "Test 1/3 POST OPERATION SUCCESS | $post_response"
else
    echo "Test 1/3 POST OPERATION FAILED"
    exit 1
fi



# GET API RESPONSE
get_response=$(curl -s "$url")

# TESTING GET RESPONSE
if created_at=$(jq -e --arg name "$name" --arg email "$email" --arg content "$content" '
        .timeline_posts[] | select(.name == $name and .email == $email and .content == $content) | .created_at
        ' <<< "$get_response"); then

    echo "Test 2/3 GET OPERATION SUCCESS | $post_response"
else
    echo "Test 2/3 GET OPERATION FAILED"
    exit 1
fi



# DELETE BODY + API RESPONSE
sleep 2
delete_response=$(curl -s $url -X DELETE -d "name=$name&start=$created_at&end=$created_at&password=$random_number" )

# TESTING DELETE RESPONSE
if echo "$delete_response" | jq -e '.delete_count == 1' > /dev/null; then
    echo "Test 3/3 DELETE OPERATION SUCCESS | $delete_response"
else
    echo "Test 3/3 DELETE OPERATION FAILED"
    exit 1
fi


