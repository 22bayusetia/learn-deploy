# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI application code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Expose port 80
EXPOSE 80

# Command to run the FastAPI application using Uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
