#!/bin/bash
# https://docs.docker.com/config/containers/multi-service_container/
set -m

exec flask run -h 0.0.0.0 -p 5000 --reload &
#exec gunicorn app:APP -w 1 -t 5 --bind 0.0.0.0:5000 --timeout 300;

fg %1