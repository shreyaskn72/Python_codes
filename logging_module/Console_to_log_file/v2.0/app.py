#Reference:

import sys
import time
import traceback

from module1.helloword import hello
from module1.get_date import get_date_time_now

old_stdout = sys.stdout

log_file = open("message.log","w")

sys.stdout = log_file


# datetime object containing current date and time

try:

    hello()

except Exception as e:
    print(e)

    traceback.print_exc(file=sys.stdout)
    raise Exception(e)#prints exception in terminal also



print(get_date_time_now(), "this will be written to message.log")


sys.stdout = old_stdout

log_file.close()
