# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

ARG SERVER_USER
ARG SERVER_UID

RUN apt-get update && apt-get install -y \
    pipenv \
    rabbitmq-server \
    libpq-dev

COPY . ./app

# Create system user to run Composer and Artisan Commands
RUN useradd -G www-data,root -u $SERVER_UID -d /home/$SERVER_USER $SERVER_USER
RUN mkdir -p /home/$SERVER_USER/.composer && \
    chown -R $SERVER_USER:$SERVER_USER /home/$SERVER_USER

WORKDIR /app


RUN pip install pipenv

# Run app.py when the container launches
RUN pipenv install --system --deploy


EXPOSE 8000

COPY init.sh /opt
RUN chmod +x /opt/init.sh

CMD ["/opt/init.sh"]