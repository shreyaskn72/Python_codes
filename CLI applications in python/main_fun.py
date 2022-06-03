import typer
import ast
import pandas as pd


app = typer.Typer()


#command to be run in cmd
#main_fun.py hello Shreyas
@app.command()
def hello(word):
    print(word)


#command to be run in cmd
#main_fun.py printword
@app.command()
def printword():
    print("Shreyas K N")


#Command to be given in the command prompt
# main_fun.py list-to-df "[1,2,3,4]"
@app.command()
def list_to_df(list_input):
    if type(list_input) == str:
        list_input = ast.literal_eval(list_input)  # converts to python list

    #print(list_input)
    df = pd.DataFrame(list_input)
    print(df)
    return df

#Command to be given in the command prompt
#main_fun.py dcitionary-input "{'Name': 'supi', 'Age': 12, 'Class': 'fifth'}"
@app.command()
def dcitionary_input(dict):

    if type(dict) == str:
        dict = ast.literal_eval(dict)  # converts to python dictionary

    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])


#Command to be given in the command prompt
#main_fun.py tuple-input "(1, 2, 3, 4, 5, 6, 7)"
@app.command()
def tuple_input(tup):
    if type(tup) == str:
        tup = ast.literal_eval(tup)  # converts to python tuple

    print("tup[1:5]: ", tup[1:5])


#Command to be given in the command prompt
#main_fun.py set-input "{'grape', 'banana', 'jackfruit'}"
@app.command()
def set_input(setinput):

    if type(setinput) == str:
        setinput = ast.literal_eval(setinput)  # converts to python set


    print("grape" in setinput)
    print("set before addition:", setinput)
    setinput.add("mango")
    print("set after addition:", setinput)
    print(type(setinput))


#Command to be given in the command prompt
#main_fun.py list-dict "[500, 700, 600]" "{'Name': 'supi', 'Age': 12, 'Class': 'fifth'}"
@app.command()
def list_dict(list1, dict1):
    if type(list1) == str:
        list1 = ast.literal_eval(list1)  # converts to python list
    if type(dict1) == str:
        dict1 = ast.literal_eval(dict1)  # converts to python dictionary


    print("Maximum of list", max(list1))
    print("dict['Name']: ", dict1['Name'])
    print("dict['Age']: ", dict1['Age'])




if __name__ == "__main__":
    # hello("Shreyas")
    #
    #list_input = [1, 2, 3, 4, 5]
    # list_input = list_input  # convert list to str due to command line integration
    #df = list_to_df(list_input)
    # print(df)

    # dict = {'Name': 'supi', 'Age': 12, 'Class': 'fifth'}
    # dcitionary_input(dict)

    # tup = (1, 2, 3, 4, 5, 6, 7)
    # tuple_input(tup)

    # setinput = {"grape", "banana", "jackfruit"}
    # set_input(setinput)

    # list1 = [500, 700, 600]
    # dict1 = {'Name': 'supi', 'Age': 12, 'Class': 'fifth'}
    # list_dict(list1, dict1)

    app()