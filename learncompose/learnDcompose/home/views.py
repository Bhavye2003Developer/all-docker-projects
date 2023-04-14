from django.shortcuts import render
from django.http import HttpResponse

import redis
import time

cache = redis.Redis(host='redis')

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# Create your views here.
def index(request):
    cnt = get_hit_count()
    return HttpResponse(f"<h1>The visit count is : {cnt}</h1>")