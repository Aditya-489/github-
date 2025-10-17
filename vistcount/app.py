# app.py
from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
# The 'redis' in the host parameter is the name of the Redis service
# defined in our docker-compose.yml file.
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increment a counter in Redis called 'hits'
    count = redis.incr('hits')
    return f'Hello! This page has been viewed {count} times.\n'

if __name__ == "__main__":
    # The host='0.0.0.0' makes the server accessible from outside the container
    app.run(host="0.0.0.0", port=5000, debug=True)