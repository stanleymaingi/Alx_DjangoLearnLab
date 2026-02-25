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