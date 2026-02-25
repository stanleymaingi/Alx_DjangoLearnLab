# Social Media API

## Setup

1. Clone repository
2. Create virtual environment
3. Install requirements:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Start server:
   python manage.py runserver

## Authentication

### Register
POST /api/accounts/register/

### Login
POST /api/accounts/login/

Returns authentication token.

### Profile
GET /api/accounts/profile/
Requires Token Authentication.
## Posts Endpoints

GET /api/posts/
POST /api/posts/
PUT /api/posts/{id}/
DELETE /api/posts/{id}/
Search: /api/posts/?search=keyword

## Comments Endpoints

GET /api/comments/
POST /api/comments/
PUT /api/comments/{id}/
DELETE /api/comments/{id}/