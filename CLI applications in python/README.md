# Building CLI applications in python


The objective is to call Python function from command prompt. Typer is used to write CLI application in python.

The entire application is in main_fun.py. 

The objective is to run python functions inside main_fun.py from command prompt.




## Install

    pip install typer

## Open
    Open folder containing mainfun.py in cmd inside virtual environment.



## Calling hello(word) function in cmd
### Syntax
    main_fun.py hello <argument>

### Example

    main_fun.py hello Shreyas

#### Output

    Shreyas

## Calling printword() function in cmd
### Syntax
    main_fun.py printword

### Example

    main_fun.py printword

#### Output
    Shreyas K N


## Calling list_to_df(list_input) function in cmd
### Syntax
    main_fun.py list-to-df <str(list argument)>

### Example

    main_fun.py list-to-df "[1,2,3,4]"

#### Output
       0
    0  1
    1  2
    2  3
    3  4

## Calling dcitionary_input(dict) function in cmd
### Syntax
    main_fun.py dcitionary-input <str(dictionary argument)>

### Example

    main_fun.py dcitionary-input "{'Name': 'supi', 'Age': 12, 'Class': 'fifth'}"

#### Output
    dict['Name']:  supi
    dict['Age']:  12


## Calling tuple_input(tup) function in cmd
### Syntax
    main_fun.py tuple-input <str(tuple argument)>

### Example

    main_fun.py tuple-input "(1, 2, 3, 4, 5, 6, 7)"

#### Output
    tup[1:5]:  (2, 3, 4, 5)



## Calling set_input(setinput) function in cmd
### Syntax
    main_fun.py set-input <str(set argument)>

### Example

    main_fun.py set-input "{'grape', 'banana', 'jackfruit'}"

#### Output
    True
    set before addition: {'grape', 'jackfruit', 'banana'}
    set after addition: {'grape', 'mango', 'jackfruit', 'banana'}
    <class 'set'>


## Calling list_dict(list1, dict1) function in cmd
### Syntax
    main_fun.py list-dict <str(list argument)> <str(dictionary argument)>

### Example

    main_fun.py list-dict "[500, 700, 600]" "{'Name': 'supi', 'Age': 12, 'Class': 'fifth'}"

#### Output
    Maximum of list 700
    dict['Name']:  supi
    dict['Age']:  12


## Appendix

 - typer installation: https://pypi.org/project/typer/#description
 - typer Documentation: https://typer.tiangolo.com/
 - Source Code: https://github.com/tiangolo/typer
 
