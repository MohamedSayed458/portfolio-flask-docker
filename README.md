# Portfolio Flask App

> A production-ready Dockerized Flask portfolio application with CI/CD, demonstrating real-world DevOps practices including containerization, automated testing, and cloud deployment on AWS.

---

## Live Demo

- Application: [http://51.20.55.234/](http://51.20.55.234/)
    
- Health Check: [http://51.20.55.234/health](http://51.20.55.234/health)
    

---

## Project Overview

This project demonstrates a complete DevOps workflow for building, testing, and deploying a Python Flask application.

It highlights:

- Containerization using Docker and Docker Compose
    
- Automated CI pipeline with GitHub Actions
    
- Deployment on AWS EC2
    
- Health monitoring and service reliability
    
- Clean and responsive portfolio interface
    

---

## Features

- REST API endpoint (`/api`)
    
- Health check endpoint (`/health`)
    
- Dockerized application
    
- CI pipeline with GitHub Actions
    
- Production deployment on AWS EC2
    

---

## Tech Stack

|Category|Tools|
|---|---|
|Language|Python 3.11|
|Framework|Flask|
|Containerization|Docker, Docker Compose|
|CI/CD|GitHub Actions|
|Cloud|AWS EC2|
|Web Server|Gunicorn|
|OS|Linux (Ubuntu)|

---

## Project Structure

```
portfolio-flask-docker/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/MohamedSayed458/portfolio-flask-docker.git
cd portfolio-flask-docker
```

### 2. Run with Docker Compose

```bash
docker compose up --build
```

### 3. Access the app

- App: [http://localhost:5000](http://localhost:5000/)
    
- Health: [http://localhost:5000/health](http://localhost:5000/health)
    

---

## CI/CD Pipeline

This project includes a GitHub Actions pipeline that:

- Builds the Docker image
    
- Runs the container
    
- Tests the `/health` endpoint
    
- Ensures the application is working before deployment
    

---

## Author

**Mohamed Newish**  
Junior DevOps Engineer

GitHub: [https://github.com/MohamedSayed458](https://github.com/MohamedSayed458)  
LinkedIn: [https://www.linkedin.com/in/mohamed-newish-8470a5395](https://www.linkedin.com/in/mohamed-newish-8470a5395)
