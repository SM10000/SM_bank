from datetime import datetime
from functools import wraps

def log(func):
    @wraps(func)
    def deco(*args,**kws):
        print("function"+func.__name__+"has been called at"+datetime.now().strftime('%y-%m-%d %H:%M:%S'))
        return func(*args,**kws)
    return deco


@log
def add(x,y):
    return x+y

flg=add(1,2)
print(flg)

ad=add.__name__
print(ad)

