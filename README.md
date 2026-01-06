# Django Demo Task – REST API with PostgreSQL

## Overview

This project is a simple web application built using **Python (Django)** and **PostgreSQL**.  
It demonstrates backend development fundamentals including REST APIs, third-party API integration, and reporting using database data.

This application was developed to fulfill all requirements of the provided demo task.

---

## Tech Stack

- Python 3
- Django 5
- Django REST Framework
- PostgreSQL
- psycopg2-binary
- Requests
- Gunicorn (for deployment)

---

## Features

---

## 1. CRUD REST APIs (Create, Read, Update, Delete)

The application provides full CRUD functionality for managing products using REST APIs.

### Products API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/api/products/` | Fetch all products |
| POST | `/api/products/` | Create a new product |
| GET | `/api/products/{id}/` | Fetch a single product |
| PUT | `/api/products/{id}/` | Update a product |
| DELETE | `/api/products/{id}/` | Delete a product |

---

## 2. Third-Party API Integration

The application integrates with a public third-party API to demonstrate external API consumption.

### Endpoint
GET /api/external-posts/


### Description
- Fetches data from:  
  `https://jsonplaceholder.typicode.com/posts`
- Returns a subset of posts via a Django REST API response
- No database storage required

---

## 3. Reporting / Data Visualization Support

A reporting API aggregates data from the PostgreSQL database and returns report-ready output.

### Endpoint
GET /api/report/summary/


### Returns
- Total number of products
- Total quantity of all products
- Total inventory value (sum of product prices)

This data can be directly used for:
- Charts
- Dashboards
- Analytics
- Excel exports

---



## Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/python_demo_task.git
cd python_demo_task/backend
```

### Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Update backend/settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_demo_db',
        'USER': 'django_user',
        'PASSWORD': 'django_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```
### Apply Migrations
```bash
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Run Development Server
```bash
python manage.py runserver
```

Application will be available at:

http://127.0.0.1:8000/

### API Testing

You can test APIs using Postman, curl, or a web browser.

### Products API

GET     /api/products/
POST    /api/products/
PUT     /api/products/{id}/
DELETE  /api/products/{id}/


### External API
GET /api/external-posts/

### Reporting API
GET /api/report/summary/


---
