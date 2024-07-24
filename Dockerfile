FROM python:3.9-slim-buster

# Set up work directory
WORKDIR /MLH-portfolio-website

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=3004"]

# For some reason port 5000 is being used on my local system
# and I could not kill the process to save my life
EXPOSE 3004