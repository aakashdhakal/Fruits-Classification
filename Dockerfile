# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the website directory contents into the container
COPY website/ /app/

# Copy the model file into the container
COPY fruits_classification.keras /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]