# Advanced API Development with Django REST Framework

This project demonstrates **advanced API development** using **Django REST Framework (DRF)**, including **custom serializers, nested relationships, generic views, permissions, and CRUD operations**.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Models](#models)
- [Serializers](#serializers)
- [Views](#views)
- [URL Endpoints](#url-endpoints)
- [Permissions](#permissions)
- [Testing](#testing)
- [Future Improvements](#future-improvements)

---

## Project Overview

This project is designed to handle **Authors and Books**:

- `Author` has a one-to-many relationship with `Book`.
- The API supports CRUD operations on Books.
- Nested serializers allow retrieving Authors with their related Books.
- Generic views are used to simplify API development.
- Permissions restrict create/update/delete actions to authenticated users, while list/detail views are publicly accessible.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/stanleymaingi/Alx_DjangoLearnLab.git
cd advanced-api-project

## This stages all changes only inside advanced-api-project


git add advanced-api-project

git commit -m "Update advanced-api-project: generic views, custom serializers, permissions"

git push origin main



git add advanced-api-project/advanced_api_project/urls.py
git add advanced-api-project/api/serializers.py
git add advanced-api-project/api/urls.py
git add advanced-api-project/api/views.py
git add advanced-api-project/urls.py
git add api_project/api/views.py
git add api_project/api_project/settings.py
git add api_project/api_project/urls.py


git commit -m "Update API views, urls, serializers, and project settings"


git push origin main --force

