import time

def decorator_1(func):
    """
    Funksiya bajarilish vaqtini hisoblaydigan dekorator.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} call executed in {end_time - start_time:.4f} sec")
        return result
    return wrapper

@decorator_1
def example_function():
    print("Function is running...")
    time.sleep(1)

example_function()
