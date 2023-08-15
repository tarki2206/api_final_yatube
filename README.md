Social Media API
This is a Social Media API built using Django and Django REST framework. It allows users to interact with posts, comments, and communities through various endpoints. Users can subscribe and unsubscribe, view and create posts, comment on posts, and perform CRUD operations on comments. The API also supports filtering based on different fields.

Authentication
To access the API endpoints, users need to authenticate and obtain a token.

Getting a Token
To obtain a token, make a POST request to /api/v1/jwt/create/ with the following data:
{
  "username": "your_username",
  "password": "your_password"
}
Endpoints
Create a Post

Endpoint: POST /api/v1/posts/

Create a new post by sending a POST request with the text field in the request body. Remember to include the token in the Authorization header like this: Authorization: Bearer <your_token>.

Example Request:

{
    "text": "tarki"
}

Comment on a Post

Endpoint: POST /api/v1/posts/{post_id}/comments/

Comment on a post by sending a POST request with the post and text fields in the request body. Include the token in the Authorization header.

Example Request:

{
  "post": 1,
  "text": "tarki"
}

Example Response:

{
    "id": 10,
    "author": "tarki2206",
    "post": 1,
    "text": "tarki",
    "created": "2023-08-07T16:53:03.302824Z"
}

Getting Started
To get started with the API, follow these steps:

Clone the repository: git clone <git@github.com:tarki2206/api_final_yatube.git>

Install the required packages: pip install -r requirements.txt

Run migrations: python manage.py migrate

Create a superuser: python manage.py createsuperuser

Start the development server: python manage.py runserver

Access the API at http://localhost:8000/api/v1/

That's it! You can now use the API to interact with posts, comments, and communities.
