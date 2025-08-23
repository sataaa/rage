FROM python:3.11-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the keep-alive script into the container
COPY src/keep_alive.py .

# Expose a port (e.g., 8000) for the API Gateway to connect to
EXPOSE 8000

# Set the command to run the Python script
CMD ["python3", "keep_alive.py"]