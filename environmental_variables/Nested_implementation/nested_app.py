import os
import json


def configure_envvar(key, value):
    env_var = "MYPROJECT"

    if env_var not in os.environ:
        print("env_var written for the first time")
        os.environ[env_var] = '{}'
        print(os.environ.get(env_var))

    initial_var = os.environ.get(env_var)

    #print(type(initial_var))

    inital_dict = json.loads(initial_var)

    if key in inital_dict:
        print("The key", key, "already exists it is overwritten & updated")

    #print(type(inital_dict))

    inital_dict[key] = value

    converted_string = json.dumps(inital_dict)

    os.environ[env_var] = converted_string

    final_env_dict = json.loads(os.environ.get(env_var))

    return final_env_dict


def read_envvar():
    env_var = "MYPROJECT"

    if env_var not in os.environ:
        print("env_var MYPROJECT does not exist")
        raise Exception('env_var MYPROJECT does not exist.')

    converted_dict_env = json.loads(os.environ.get(env_var))

    return converted_dict_env


def read_single_envvar(key):
    env_var = "MYPROJECT"

    if env_var not in os.environ:
        print("env_var MYPROJECT does not exist")
        raise Exception('env_var MYPROJECT does not exist.')

    converted_dict_env = json.loads(os.environ.get(env_var))

    if key not in converted_dict_env:
        print("key", key, "does not exist inside environement variable")


    interested_env = converted_dict_env[key]

    return interested_env




if __name__ == "__main__":
   start = configure_envvar("age", 20)
   print(start)

   start2 = configure_envvar("class", 2)
   print(start2)
   print(type(start2))

   start3 = configure_envvar("rank", 2)

   print(start3)
   print(type(start3))

   thisdict = {
       "brand": "Ford",
       "model": "Mustang",
       "year": 1964
   }

   start4 = configure_envvar("nested key", thisdict)

   print(start4)
   print(type(start4))

   converted_dict_env = read_envvar()
   print("read from environmental variable")

   print(converted_dict_env)


   interest = read_single_envvar("age")
   print(interest)

   test = configure_envvar("class", 3)

   converted_dict_env = read_envvar()
   print("read from environmental variable")

   print(converted_dict_env)
