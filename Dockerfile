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

# Default command to run the unit tests with coverage
CMD ["coverage", "run", "-m", "unittest", "Unit_test.py"]
