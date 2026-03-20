# 🚀 DevOps Portfolio - AWS Cloud Deployment

A professional portfolio website demonstrating core DevOps engineering skills: containerization, cloud deployment, CI/CD automation, and infrastructure management.

## 🎯 Project Overview

This project showcases a containerized Flask web application deployed on AWS EC2, built as part of my journey to become a Junior DevOps Engineer. It demonstrates practical skills in:

- ✅ Docker containerization & orchestration
- ✅ AWS EC2 cloud deployment
- ✅ Linux system administration
- ✅ CI/CD pipeline automation (GitHub Actions)
- ✅ RESTful API development
- ✅ Security best practices (OWASP awareness)

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Languages** | Python, Bash, JavaScript, HTML5, CSS3 |
| **Container** | Docker, Docker Compose |
| **Cloud** | AWS EC2 (Free Tier) |
| **CI/CD** | GitHub Actions |
| **Web Framework** | Flask, RESTful APIs |
| **Database** | PostgreSQL, SQL |
| **OS** | Linux (Ubuntu 22.04) |
| **Version Control** | Git, GitHub |

## 📁 Project Structure

```
devops-portfolio-aws/
├── app.py                 # Flask application with portfolio site
├── Dockerfile             # Container build configuration
├── docker-compose.yml     # Multi-container orchestration (optional)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🚀 Quick Start

### Local Development
```bash
# Clone the repo
git clone https://github.com/MohamedSayed458/portfolio-flask-docker.git
cd devops-portfolio-aws

# Build and run with Docker
docker build -t portfolio .
docker run -d -p 80:5000 --name portfolio-app portfolio
```

### Access the Application
- 🌐 Website: `http://localhost:8000`
- 🔍 Health Check: `http://localhost:8000/health`
- 📡 API: `http://localhost:8000/api`

## ☁️ AWS Deployment

This application is deployed on AWS EC2 using:
- Ubuntu 22.04 LTS
- Docker Engine
- Security Groups (HTTP:80, SSH:22 restricted)
- Public IPv4 endpoint

### Deployment Commands (on EC2)
```bash
# Pull and build
git clone https://github.com/MohamedSayed458/portfolio-flask-docker.git
cd devops-portfolio-aws
docker build --no-cache -t portfolio .

# Run container
docker run -d -p 80:5000 --name portfolio-app --restart unless-stopped portfolio
```

## 🔗 Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main portfolio website (HTML) |
| `/api` | GET | JSON API response |
| `/health` | GET | Health check for monitoring (returns 200 OK) |

## 👤 About the Developer

**Mohamed Sayed** | Junior DevOps Engineer

🎓 Studying Embedded Systems at Technische Universität Chemnitz  
🔧 Passionate about infrastructure automation, CI/CD, and cloud-native technologies  
🌍 Languages: English (Fluent), German (Good Knowledge), Arabic (Native)

### 🔗 Connect
- 💼 LinkedIn: [https://www.linkedin.com/in/mohamed-newish-8470a5395]
- 📧 Email: [mohamedsayed2646@gmail.com]
- 🐙 GitHub: https://github.com/MohamedSayed458

