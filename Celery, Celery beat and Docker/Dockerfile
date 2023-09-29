# Use the official Python image as the base image
# FROM python:3.8-slim-buster
FROM python:3

# Set environment variables for Python and unbuffered output
ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Create and set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the Django application and Celery tasks into the container
# COPY . /app/

# Expose the port if needed
# EXPOSE 8000

# # Run migrations and collect static files (modify as needed)
# RUN python manage.py migrate

# # Command to start the Django development server and Celery worker
# CMD ["celery", "-A", "myproject", "worker", "--loglevel=info"]
