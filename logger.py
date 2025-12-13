import time

def log_time(func):
    def wrapper():
        print(time.ctime())
        func()
    return wrapper