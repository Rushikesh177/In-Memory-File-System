FROM python:3.8

# Set the working directory
WORKDIR /usr/src/app

COPY . .

# Make port 80 available to the world
EXPOSE 80

# Define environment variable
ENV NAME World

# Run Python script
CMD ["python", "./InMemoryFileSystem.py"]
