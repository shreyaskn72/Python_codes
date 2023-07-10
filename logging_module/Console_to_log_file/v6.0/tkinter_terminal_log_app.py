from tkinter import *
import sys

from IPython.utils.io import Tee
from contextlib import closing
from datetime import datetime
import traceback
import sys

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
    print("hello", name)
    print("too many word below:")
    print("dfsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("Welcome to", city)

root=Tk()

# Add a Scrollbar(Vertical)
v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')

# Add a Scrollbar(Vertical)
h=Scrollbar(root, orient='horizontal')
h.pack(side=BOTTOM, fill='x')



textbox=Text(root, font=("Calibri, 16"), wrap=NONE, xscrollcommand=h.set,  yscrollcommand=v.set)

# Attach the scrollbar with the text widget
v.config(command=textbox.yview)
h.config(command=textbox.xview)
textbox.pack()
button1=Button(root, text='output', command=lambda: greetings("cmd_terminal", "Shreyas", "Bengaluru"))
button1.pack()


#Pushing console print to tkinter text box
def tkinter_print_decorator(func):
    def inner(inputStr):
        try:
            textbox.insert(INSERT, inputStr)
            return func(inputStr)
        except:
            return func(inputStr)
    return inner

sys.stdout.write=tkinter_print_decorator(sys.stdout.write)



root.mainloop()
