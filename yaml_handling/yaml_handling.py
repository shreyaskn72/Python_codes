import yaml
import os

class crudoopsyaml:

    def __init__(self, filename):

        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as outfile:
                yaml.dump({}, outfile)

    def openfile(self):
        with open(self.filename, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    # Dont use this method writefile() when running the code!

    def writefile(self, dic):
        with open(self.filename, 'w') as fp2:
            yaml.dump(dic, fp2, indent=4)

    def addrow(self, id, new):
        dic= crudoopsyaml.openfile(self)
        if id in dic.keys():
            print("the id already exist. Change the id please")
        else:
            dic[id] = new
            crudoopsyaml.writefile(self, dic)

    def readone(self, id):
        dic = crudoopsyaml.openfile(self)
        if id in dic.keys():
            print("The student with the id", id, "is", dic[id])

    def readall(self):
        dic = crudoopsyaml.openfile(self)
        print(dic)

    def updatyaml(self, id, value):
        dic = crudoopsyaml.openfile(self)

        if id in dic.keys():
            dic[id] = value
            crudoopsyaml.writefile(self, dic)

        else:
            print("the key doesnot exist in the yaml file so its impossible to update")

    def deletee(self, id):
        dic = crudoopsyaml.openfile(self)
        if id in dic.keys():
            del dic[id]
            crudoopsyaml.writefile(self, dic)
        else:
            print("The data with the id doesnot exist in the file so I cannot delete")

if __name__ == "__main__":
    filename = 'trial_python.yaml'
    object1 = crudoopsyaml(filename)
    print(object1.openfile())
    print(type(object1.openfile()))
    object1.addrow('hs', {'Name': 'lupo', 'Class': 100, 'Grade': 5, 'Rank': 1})
    object1.addrow('ha', {'Name': 'marco', 'Class': 10, 'Grade': 3.5, 'Rank': 10})
    object1.addrow('hn', {'Name': 'Narasimha', 'Class': 12, 'Grade': 1, 'Rank': 1})
    object1.addrow('hb', {'Name': 'lucy', 'Class': 1, 'Grade': 1, 'Rank': 1})
    object1.updatyaml('ha',
          {'Name': 'suji', 'Class': 10, 'Grade': 98, 'Rank': 1, 'subjects': ['physics', 'chemistry', 'maths']})
    object1.updatyaml('hb',
                      {'Name': 'sujayaa', 'Class': 1, 'Grade': 9, 'Rank': 1,
                       'subjects': ['physics', 'chemistry', 'maths']})
    object1.readone('ha')
    object1.readall()
    object1.deletee('ha')