#Reference:


import sys
import time
from module1.helloword import hello

old_stdout = sys.stdout

log_file = open("message.log","w")

sys.stdout = log_file

hello()

print(time.time(), "this will be written to message.log")

sys.stdout = old_stdout

log_file.close()