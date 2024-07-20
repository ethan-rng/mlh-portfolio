import unittest
import os
os.environ['TESTING' ] = 'true'

from app import app

class AppTestCase (unittest. TestCase):
    def setUp(self):
        self.client = app.test_client()
            
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title></title>" in html
        # TODO Add more tests relating to the home page
        assert "<p>hobbies</p>" in html
        assert "currIndex = (currIndex + 1) % heroTags.length;" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # Test POST request
        post_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "content": "Hello, this is a test post.",
            "password": "password1"
        }
        response = self.client.post("/api/timeline_post", data=post_data)
        # json = response.get_json()
        assert response.status_code == 200  # assuming 201 Created status code
        assert response.is_json
        json = response.get_json()
        assert "id" in json

        # Verify that the post was created
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == post_data["name"]
        assert json["timeline_posts"][0]["email"] == post_data["email"]
        assert json["timeline_posts"][0]["content"] == post_data["content"]
        
        # TODO Add more tests relating to the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title></title>" in html
        assert "<main class=\"flex flex-col items-center w-full pt-24\">" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!", "password": "password1"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": "", "password": "password1"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!", "password": "password1"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
            