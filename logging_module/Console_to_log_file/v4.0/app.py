from IPython.utils.io import Tee
from contextlib import closing

print('This is not written in the log file.')

with closing(Tee("terminal_info.log", "w", channel="stdout")) as outputstream:
    print('This is written in terminal info log and printed in consold too.')

print('This is not written to log file')
