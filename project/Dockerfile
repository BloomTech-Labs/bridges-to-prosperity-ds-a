# pull official base image
FROM python:3.7-slim-buster

# set working directory
WORKDIR /usr/src/project
COPY . .
# install python dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
