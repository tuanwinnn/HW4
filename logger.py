import time

def log_time(func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)
    return wrapper