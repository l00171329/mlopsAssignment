FROM ubuntu:latest

# Update the package manager and install necessary dependencies
RUN apt-get update && \
    apt-get install -y gcc openssl libssl-dev libbz2-dev libffi-dev zlib1g-dev wget make

# Download and install Python 3.8.12
WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz && \
    tar xzf Python-3.8.12.tgz && \
    cd Python-3.8.12 && \
    ./configure --enable-optimizations && \
    make altinstall

# Install additional Python packages
RUN pip3.8 install sklearn joblib numpy pandas scikit-learn Flask

# Set the working directory for the container
WORKDIR /mlopsAssignment
# Copy your application files to the container
COPY . /mlopsAssignment

# Specify the command to run when the container starts

# Specify the command to run when the container starts
CMD ["python3.8", "FlaskApp.py"]
EXPOSE 5000

