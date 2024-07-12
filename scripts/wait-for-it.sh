#!/usr/bin/env bash

# Original script from https://github.com/vishnubob/wait-for-it

set -e

TIMEOUT=15
STRICT=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --timeout=*)
      TIMEOUT="${1#*=}"
      shift
      ;;
    --strict)
      STRICT=1
      shift
      ;;
    --)
      shift
      break
      ;;
    *)
      break
      ;;
  esac
done

HOST="$1"
PORT="$2"
shift 2

echo "Waiting for $HOST:$PORT..."

for i in `seq $TIMEOUT` ; do
  nc -z "$HOST" "$PORT" > /dev/null 2>&1 && break
  echo -n .
  sleep 1
done

if [ "$STRICT" == "1" ]; then
  if ! nc -z "$HOST" "$PORT" > /dev/null 2>&1 ; then
    echo "Operation timed out" >&2
    exit 1
  fi
fi

echo "Host $HOST on port $PORT is available!"
exec "$@"
