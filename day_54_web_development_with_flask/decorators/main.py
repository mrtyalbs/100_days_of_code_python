import time

current_time = time.time()
print(current_time)


def speed_calculation_decorator(function_param):
    def wrapper_function():
        start_time = time.time()
        function_param()
        end_time = time.time()
        print(f"{function_param.__name__} run speed: {end_time - start_time}")

    return wrapper_function


@speed_calculation_decorator
def fast_func():
    for i in range(100):
        i * i


@speed_calculation_decorator
def slow_func():
    for i in range(10000000):
        i * i


fast_func()
slow_func()
