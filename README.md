# URL Shortener API

## Overview

This project is a containerized URL Shortener API built using FastAPI and PostgreSQL.

The application accepts a long URL, generates a short unique code, stores it in PostgreSQL, and redirects users when the short URL is accessed.

Example:

Input:

https://google.com

Output:

http://localhost:8000/Ab12Cd

When users open the short URL, they are redirected to the original URL.

---

## Architecture

Client → FastAPI → PostgreSQL

Flow:

1. User sends long URL.
2. FastAPI validates input.
3. Generates short code.
4. Stores data in PostgreSQL.
5. Returns short URL.
6. Redirect endpoint resolves short code.

---

## Tools and Technologies Used

### Backend

* FastAPI → API framework
* Uvicorn → ASGI server
* SQLAlchemy → ORM
* Pydantic → request validation

### Database

* PostgreSQL 16

### Containerization

* Docker
* Docker Compose

### Environment Management

* .env file

---

## Project Structure

url-shortener/
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
└── postgres/
└── init.sql

---

## API Endpoints

### POST /shorten

Creates short URL.

Request:

{
"original_url": "https://google.com"
}

Response:

{
"short_url": "http://localhost:8000/abc123"
}

---

### GET /{short_code}

Redirects to original URL.

Example:

GET /abc123

Response:

302 Redirect

---

## Setup

Clone repo:

git clone <repo>

Run:

docker compose up --build

Open:

http://localhost:8000/docs

---

## Database

Table: urls

Columns:

* id
* original_url
* short_code

---

## Future Enhancements

* Custom alias support
* URL expiry
* Analytics
* QR code generation
* Redis caching
* Rate limiting
* CI/CD with GitHub Actions
* Deployment with Nginx reverse proxy

