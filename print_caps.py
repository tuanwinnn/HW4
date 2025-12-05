def allcaps(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper