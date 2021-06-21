import json
import os

class crudoopsjson:

    def __init__(self, filename):

        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as outfile:
                json.dump({}, outfile)

    def openfile(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data

    # Dont use this method writefile() when running the code!

    def writefile(self, dic):
        with open(self.filename, 'w') as fp2:
            json.dump(dic, fp2, indent=4)

    def addrow(self, id, new):
        dic= crudoopsjson.openfile(self)
        if id in dic.keys():
            print("the id already exist. Change the id please")
        else:
            dic[id] = new
            crudoopsjson.writefile(self, dic)