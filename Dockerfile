FROM ubuntu:22.04

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY /src/main/python/playspace /app/

# Install dependencies
# RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
RUN apt-get install git -y
RUN pip install -r requirements.txt
# Make port 1234 available to the world outside this container
EXPOSE 1234

CMD ["flet", "run", "--web", "--port", "1234", "main.py"]

# CMD ["cat", "requirements.txt"]