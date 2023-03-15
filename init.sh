#!/bin/sh

#
# Start task scheduler
#
celery -A autotweeterproject beat -l info --detach

#
# Start task message-broker server
#
rabbitmq-server -detached

#
# Start worker
#
celery -A autotweeterproject worker -l info &> /var/log/celery_worker.log &

#
# Start Django server
#
python manage.py runserver 0.0.0.0:8000