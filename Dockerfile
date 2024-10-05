FROM ubuntu:20.04

# Installing system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Installing Python dependencies
RUN pip3 install flask flask-mysql

# Application code
COPY app.py /opt/

# Setting the working directory
WORKDIR /opt

# Exposing the application port
EXPOSE 8080

# Starting the Flask application
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]