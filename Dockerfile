# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file if it exists
# COPY requirements.txt /app/

# Install dependencies
# RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Command to run the application
CMD ["python", "inventory_system.py"]
