# REST API Server

Server made using Flask with GET request functionality. When called the server sends an HTTP response with the required RESTful headers and caching functionality using Flask-Caching.

I wrote this server for the purpose of bettering my understanding of REST API, and to explain REST in an article on Medium.

# How to Run the Project

### Run the server

- In the rest_api_server directory

`pipenv install`

`pipenv shell`

`python app.py`

### Make a GET request with curl

- Now open a new terminal and run:

`curl -v http://127.0.0.1:5001`
