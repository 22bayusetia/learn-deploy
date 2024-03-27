# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port number on which your Flask application will run
EXPOSE 8000

# Define environment variable for the Python script
ENV PYTHONPATH=/app

# Command to run your Flask application using gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
