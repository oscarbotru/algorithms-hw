import time


def timing(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        print(f'Func: "{func.__name__}" finished in: {t2 - t1:.4f} sec')
        return res
    return wrapper
