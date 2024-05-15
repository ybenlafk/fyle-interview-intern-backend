# Use the official Python image as a base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Reset the database
RUN export FLASK_APP=core/server.py && rm core/store.sqlite3 && flask db upgrade -d core/migrations/

# Expose the port Flask runs on
EXPOSE 7755

# Run the bash script to start the server
CMD ["bash", "run.sh"]
