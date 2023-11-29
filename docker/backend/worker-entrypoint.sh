#!/bin/sh

until cd /app/likesoft
do
    echo "Waiting for server volume..."
done

# run a worker
celery -A likesoft worker --loglevel=info --concurrency 1 -E

