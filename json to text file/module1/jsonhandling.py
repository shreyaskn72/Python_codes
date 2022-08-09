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

    def readone(self, id):
        dic = crudoopsjson.openfile(self)
        if id in dic.keys():
            print("The read resource with the id", id, "is", dic[id])
        return dic[id]
