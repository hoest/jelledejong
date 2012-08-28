import os

bind = "0.0.0.0:8080"
workers = 3
backlog = 2048
worker_class = "gevent"
errorlog = "./logs/error.log"
accesslog = "./logs/access.log"
