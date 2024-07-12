#!/bin/bash
# wait-for-it.sh

HOST=$1
PORT=$2

while ! nc -z -v -w30 $HOST $PORT; do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done
echo "$HOST:$PORT is available!"