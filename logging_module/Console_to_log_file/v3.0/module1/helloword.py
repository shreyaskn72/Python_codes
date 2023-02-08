from .get_date import get_date_time_now
import sys
import traceback

# A decorator function inputs another function as argument
# A decorator wraps its behaviour inside
# an inner function, and returns the wrapped function.

def logging_print_decorator(func):
    def wrapper(arg1, *args):
        old_stdout = sys.stdout

        #log_file = open("message.log", "w")

        log_file = open(arg1, "w")

        sys.stdout = log_file

        # datetime object containing current date and time

        try:

            func(arg1, *args)

        except Exception as e:
            print(e)

            traceback.print_exc(file=sys.stdout)
            raise Exception(e)  # prints exception in terminal also

        print(get_date_time_now(), "this will be written to message.log")

        sys.stdout = old_stdout

        log_file.close()

    return wrapper

@logging_print_decorator
def hello(path, greeting, name):
    #r
    print(get_date_time_now(), "signed in time")
    print(greeting," ", name)