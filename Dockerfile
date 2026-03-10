# Use an official Python image as base (small & secure)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Expose port 5000 so we can access the app
EXPOSE 5000

# Command to run when container starts
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
