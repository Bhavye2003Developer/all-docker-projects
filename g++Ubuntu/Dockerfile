# Use Ubuntu as the base image
FROM ubuntu

# Update package list and install g++
RUN apt-get update && apt-get install -y build-essential

RUN apt-get install -y python3

# Set the startup command to print a message
CMD echo "I have created a docker image of ubuntu with python, g++ and gcc installed."
