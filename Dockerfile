# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main script when the container starts
CMD ["python", "WS2_FINAL_Project.py"]
