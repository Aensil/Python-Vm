#Special Closure
def decorator(func):
    def envoltura():
        print('Hello')
        func()
    return envoltura
def saludo():
    print('Hola!')
saludo = decorator(saludo)
saludo()

#Sugar sintax
def decorator(func):
    def envoltura():
        print('Hello')
        func()
    return envoltura
@decorator                  #The same but different sintax
def saludo():
    print('Hola!')
saludo()


from datetime import datetime
def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass
random_func()