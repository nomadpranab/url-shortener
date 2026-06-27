# URL Shortener API — DevOps Focused Deployment

### Project Overview

This project is a containerized URL Shortener API built using **FastAPI**, **PostgreSQL**, **Docker**, and Docker Compose.

The goal of this project was not only to build an API but to understand how backend applications are packaged, deployed, networked, and managed using containerization tools.

This project simulates how microservices are deployed in production.

---

# Objective

The project solves two problems:

## Application Layer

* Accept long URLs
* Generate short URLs
* Store mappings
* Redirect users

### Infrastructure Layer

* Package application into a container
* Run database in isolated container
* Connect services using internal Docker networking
* Persist database using volumes
* Manage environment variables securely
* Make deployment portable across environments

---

# Architecture

```text
Client
   |
   | HTTP Request
   ↓
FastAPI Container
   |
   | SQL Query
   ↓
PostgreSQL Container
```

Infrastructure flow:

1. User sends API request.
2. Request reaches FastAPI container.
3. FastAPI connects to PostgreSQL container over Docker internal network.
4. Data is stored persistently in Docker volume.
5. Response returned to client.

---

# Tech Stack

## Application

* FastAPI
* Uvicorn
* SQLAlchemy
* Pydantic

---

## Infrastructure

* Docker
* Docker Compose
* PostgreSQL
* Environment Variables

---

# Why Docker was used

Traditional deployment problems:

* "Works on my machine" issue
* Dependency mismatch
* Python version conflicts
* Package inconsistency

Docker solves this by packaging:

* application code
* dependencies
* runtime
* startup commands

into a single image.

In this project:

Docker was used to:

* Build isolated Python runtime
* Install dependencies
* Run FastAPI server
* Maintain consistency across systems

Command used:

```bash
docker build -t url-shortener .
```

This creates an immutable image.

---

# Why Docker Compose was used

Running multiple containers manually is difficult.

Without Docker Compose:

```bash
docker run postgres ...
docker run fastapi ...
docker network connect ...
docker volume create ...
```

This becomes operationally difficult.

Docker Compose solves:

* Multi-container orchestration
* Networking
* Dependency management
* Volume mapping
* Environment injection

In this project:

Docker Compose manages:

### Service 1: Database

* PostgreSQL container
* Persistent storage
* Initialization script

### Service 2: Application

* FastAPI container
* API exposure
* Database connectivity

Command:

```bash
docker compose up --build
```

This builds and starts everything together.

---

# DevOps Concepts Implemented

---

## 1. Containerization

FastAPI app packaged into Docker image.

Benefits:

* portability
* reproducibility
* version control

---

## 2. Multi-container deployment

Application and database separated.

Benefits:

* loose coupling
* easier scaling
* service isolation

---

## 3. Service Discovery

FastAPI connects to PostgreSQL using:

```python
DATABASE_URL=postgresql://admin:admin123@db:5432/url_db
```

`db` is Docker Compose service name.

Docker automatically resolves it.

No manual IP needed.

Important DevOps concept.

---

## 4. Persistent Storage

Used Docker volume:

```yaml
volumes:
  postgres_data:
```

Purpose:

If container is deleted, database remains.

Production-grade concept.

---

## 5. Bind Mounts

Used:

```yaml
./app:/app
```

Purpose:

Sync local code with container.

Benefits:

* live reload
* fast development

---

## 6. Environment Variable Management

Used `.env`

Stores:

* DB credentials
* app config
* URLs

Avoids hardcoding secrets.

Best practice.

---

## 7. Health and Debugging

Used:

```bash
docker ps
docker ps -a
docker logs fastapi_app
docker exec -it postgres_db psql -U admin -d url_db
```

Important operational skills.

---

## 8. Rebuild Strategy

Used:

```bash
docker compose down -v
docker compose up --build
```

Used for:

* resetting infrastructure
* rebuilding images
* testing clean deployments

---

# Project Structure

```text
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
```

---

# Deployment Workflow

Step 1:

Build images:

```bash
docker compose build
```

Step 2:

Start services:

```bash
docker compose up
```

Step 3:

Verify:

```bash
docker ps
```

Step 4:

Access API:

```bash
http://localhost:8000/docs
```

Step 5:

Check DB:

```bash
docker exec -it postgres_db psql -U admin -d url_db
```

---

# Operations Commands

Stop:

```bash
docker compose down
```

Clean all:

```bash
docker compose down -v --rmi all
```

View logs:

```bash
docker logs fastapi_app
```

Check running:

```bash
docker ps
```

Enter DB:

```bash
docker exec -it postgres_db psql -U admin -d url_db
```

---

# Production Improvements

This project can be extended with:

* Nginx reverse proxy
* SSL/TLS
* GitHub Actions CI/CD
* Kubernetes deployment
* Health checks
* Monitoring with Prometheus
* Logging with ELK
* Redis caching
* Rate limiting
* Load balancing

---

# DevOps Learning Outcome

This project helped understand:

* Docker image lifecycle
* Docker Compose orchestration
* Service-to-service communication
* Persistent storage
* Container debugging
* Infrastructure rebuild
* Database operations
* Environment management
* Multi-service deployment

This project reflects real-world DevOps deployment fundamentals.
