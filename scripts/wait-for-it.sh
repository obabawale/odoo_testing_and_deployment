#!/usr/bin/env bash
# Use this script to test if a given TCP host/port are available

set -e

HOST="$1"
PORT="$2"
TIMEOUT="${3:-15}"

until nc -z -v -w30 $HOST $PORT
do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

echo "$HOST:$PORT is available!"