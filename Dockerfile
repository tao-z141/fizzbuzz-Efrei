# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir coverage

# Copy test files
COPY Unit_test.py /app

EXPOSE 5000

CMD ["sh", "-c", "coverage run --source=. -m unittest Unit_test.py && coverage report"]

