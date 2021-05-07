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

    def readone(self, id):
        dic = crudoopsjson.openfile(self)
        if id in dic.keys():
            print("The student with the id", id, "is", dic[id])

    def readall(self):
        dic = crudoopsjson.openfile(self)
        print(dic)

    def updatjson(self, id, value):
        dic = crudoopsjson.openfile(self)

        if id in dic.keys():
            dic[id] = value
            crudoopsjson.writefile(self, dic)

        else:
            print("the key doesnot exist in the json file so its impossible to update")

    def deletee(self, id):
        dic = crudoopsjson.openfile(self)
        if id in dic.keys():
            del dic[id]
            crudoopsjson.writefile(self, dic)
        else:
            print("The data with the id doesnot exist in the file so I cannot delete")

if __name__ == "__main__":
    filename = 'trial_python.json'
    object1 = crudoopsjson(filename)
    print(object1.openfile())
    print(type(object1.openfile()))
    object1.addrow('hs', {'Name': 'lupo', 'Class': 100, 'Grade': 5, 'Rank': 1})
    object1.addrow('ha', {'Name': 'marco', 'Class': 10, 'Grade': 3.5, 'Rank': 10})
    object1.addrow('hn', {'Name': 'Narasimha', 'Class': 12, 'Grade': 1, 'Rank': 1})
    object1.addrow('hb', {'Name': 'lucy', 'Class': 1, 'Grade': 1, 'Rank': 1})
    object1.updatjson('ha',
          {'Name': 'suji', 'Class': 10, 'Grade': 98, 'Rank': 1, 'subjects': ['physics', 'chemistry', 'maths']})
    object1.updatjson('hb',
                      {'Name': 'sujayaa', 'Class': 1, 'Grade': 9, 'Rank': 1,
                       'subjects': ['physics', 'chemistry', 'maths']})
    object1.readone('ha')
    object1.readall()
    object1.deletee('ha')
