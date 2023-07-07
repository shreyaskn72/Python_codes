from IPython.utils.io import Tee
from contextlib import closing
from datetime import datetime
import traceback
import sys

def get_date_time_now():
    now = datetime.now()
    time_now = now.strftime("%d/%m/%Y %H:%M:%S")
    return time_now




# A decorator function inputs another function as argument
# A decorator wraps its behaviour inside
# an inner function, and returns the wrapped function.



def logging_print_decorator(func):
    def wrapper(arg1):
        terminal_log_file_name = "terminal.log"

        with closing(Tee(terminal_log_file_name, "a", channel="stdout")) as outputstream:
            try:
                func(arg1)

            except Exception as e:
                print(e)

                traceback.print_exc(file=sys.stdout)


    return wrapper





@logging_print_decorator
def hello(name):
    #r
    print(get_date_time_now(), "signed in time")
    print("hello",name)




if __name__ == "__main__":
    hello("mr AB CD EF")