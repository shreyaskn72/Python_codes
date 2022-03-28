# This is the hardcoded final one

import os

"""
Suppose I want to run the following commands in command prompt:
cd C:/Users/shreyas/PythonProjects/command_prompt_automation/venv
CALL Scripts/activate
cd C:/Users/shreyas/PythonProjects/command_prompt_automation/0.requirements_folder
pip3 install -r requirements.txt
cd C:/Users/shreyas/PythonProjects/command_prompt_automation/venv
CALL Scripts/deactivate
exit
"""



# os.system will run all the codes. But make sure to insert && in between two commands

os.system('cmd /k "cd C:/Users/shreyas/PythonProjects/command_prompt_automation/venv && CALL Scripts/activate && cd C:/Users/shreyas/PythonProjects/command_prompt_automation/0.requirements_folder && pip3 install -r requirements.txt && cd C:/Users/shreyas/PythonProjects/command_prompt_automation/venv && CALL Scripts/deactivate && exit"')