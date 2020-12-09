import os
import redis
from flask import Flask

app = Flask(__name__)
REDIS = os.environ.get('REDIS', 'localhost:6379')
r = redis.Redis(REDIS)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/redis')
def hello_world_redis():
    i = r.incr('a')
    return f'Hello, World! {i}' 


app.run(host='0.0.0.0')
