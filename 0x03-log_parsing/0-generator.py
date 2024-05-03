#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(30):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 223), random.randint(1, 254), random.randint(1, 254), random.randint(1, 254),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 777, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
