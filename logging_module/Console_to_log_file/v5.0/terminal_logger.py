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



#Pushing console print to log file
def logging_print_decorator(func):
    def wrapper(arg1, *args):
        terminal_log_file_name = arg1+".log"

        with closing(Tee(terminal_log_file_name, "a", channel="stdout")) as outputstream:
            try:
                func(*args)

            except Exception as e:
                print(e)

                traceback.print_exc(file=sys.stdout)


    return wrapper



@logging_print_decorator
def greetings(name, city):
    print(get_date_time_now(), "signed in time")
    print("hello", name)
    print("too many word below:")
    print("dfsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("Welcome to", city)



if __name__ == "__main__":
    filepath = "terminal_output"
    name = "Shreyas"
    city = "Bengaluru"
    greetings(filepath, name, city)
