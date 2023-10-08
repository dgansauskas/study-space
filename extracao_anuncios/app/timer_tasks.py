from datetime import datetime
from functools import wraps

def elapsed_time_process(func):
    '''funcao para mensurar tempo de processamento de processos'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        print()
        print(f'-> PROCESSANDO FUNÇÃO: {func.__name__}')
        print('-' * 50)
        print(f'DESCRIÇÃO:')
        print(f'{func.__doc__}\n')
        print('-' * 50)
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print()
        running_time = datetime.now()-start_time
        print('-'*50)
        print(f"TEMPO DE PROCESSAMENTO: {running_time}")
        return result
    print()
    return wrapper

def elapsed_time_subprocess(func):
    '''
    Funcao para mensurar tempo de processamento de subprocessos
    funciona integrada com a `elapsed_time_process`
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        running_time = datetime.now()-start_time
        print(f'FUNÇÃO INTERNA: {func.__name__}')
        print(f'DESCRIÇÃO:')
        print(f'{func.__doc__}')
        print(f'TEMPO DE PROCESSAMENTO: {running_time}')
        print()
        return result
    return wrapper