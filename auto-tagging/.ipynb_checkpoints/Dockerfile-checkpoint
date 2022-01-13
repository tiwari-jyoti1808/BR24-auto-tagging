# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Allow statements and log messages to immediately appear
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install libraries from text file
RUN pip install -r requirements.txt

# Disable TensorFlow INFO and WARNING messages 
ENV TF_CPP_MIN_LOG_LEVEL=2

# Export port for web server
EXPOSE 8007

# Start gunicon
CMD exec gunicorn --bind 0.0.0.0:8007 --workers 1 --log-level debug --timeout 120 main:app
