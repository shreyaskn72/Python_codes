#copy and paste of tune3.py

import json
import os


class cmd_json:

    def __init__(self, filename):

        self.filename = filename
        if not os.path.exists(self.filename):
            print("json file is not found")

    def openfile(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data

def finalize_cmd(cmd_dict):
    #no_cmds = len(cmd_dict.keys())

    lastkey = list(cmd_dict.keys())[-1]

    final_cmd = ""

    for cmd_key, cmd_value in cmd_dict.items():
        if not (cmd_key == lastkey):
            final_cmd = final_cmd + cmd_value + " && "

        else:
            final_cmd = final_cmd + cmd_value

    return final_cmd


def run_cmd(filename):

    try:
        object1 = cmd_json(filename)
        cmd_dict = object1.openfile()
        print(cmd_dict)

        final_cmd = finalize_cmd(cmd_dict)
        print(final_cmd)
        os.system(final_cmd)

    except Exception as e:
        print(e)



# if __name__ == "__main__":
#     filename = 'command_prompt.json'
#     run_cmd(filename)