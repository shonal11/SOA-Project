# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5004 available to the world outside this container
EXPOSE 5004

# Run the application
CMD ["python", "restaurant_service.py"]

