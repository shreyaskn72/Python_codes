import json
import os
import yaml


class crudoopsjson():

    def __init__(self, filename):

        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as outfile:
                json.dump({}, outfile)

    # Private methode used because. We dont need to use this method openfile when running the code!
    def __openfile(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data

    # Private methode used because. We dont need to use this method writefile() when running the code!

    def __writefile(self, dic):
        with open(self.filename, 'w') as fp2:
            json.dump(dic, fp2, indent=4)

    def addrow(self, id, new):
        dic= crudoopsjson.__openfile(self)
        if id in dic.keys():
            print("the id already exist. Change the id please")
        else:
            dic[id] = new
            crudoopsjson.__writefile(self, dic)

    def readone(self, id):
        dic = crudoopsjson.__openfile(self)
        if id in dic.keys():
            print("The student with the id", id, "is", dic[id])

    def readall(self):
        dic = crudoopsjson.__openfile(self)
        print(dic)

    def update_record(self, id, value):
        dic = crudoopsjson.__openfile(self)

        if id in dic.keys():
            dic[id] = value
            crudoopsjson.__writefile(self, dic)

        else:
            print("the key doesnot exist in the json file so its impossible to update")

    def deletee(self, id):
        dic = crudoopsjson.__openfile(self)
        if id in dic.keys():
            del dic[id]
            crudoopsjson.__writefile(self, dic)
        else:
            print("The data with the id doesnot exist in the file so I cannot delete")


class crudoopsyaml:

    def __init__(self, filename):

        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as outfile:
                yaml.dump({}, outfile)

    # Private methode used because. We dont need to use this method openfile when running the code!
    def __openfile(self):
        with open(self.filename, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    # Private methode used because. We dont need to use this method __writefile() when running the code!

    def __writefile(self, dic):
        with open(self.filename, 'w') as fp2:
            yaml.dump(dic, fp2, indent=4)

    def addrow(self, id, new):
        dic= crudoopsyaml.__openfile(self)
        if id in dic.keys():
            print("the id already exist. Change the id please")
        else:
            dic[id] = new
            crudoopsyaml.__writefile(self, dic)

    def readone(self, id):
        dic = crudoopsyaml.__openfile(self)
        if id in dic.keys():
            print("The student with the id", id, "is", dic[id])

    def readall(self):
        dic = crudoopsyaml.__openfile(self)
        print(dic)

    def update_record(self, id, value):
        dic = crudoopsyaml.__openfile(self)

        if id in dic.keys():
            dic[id] = value
            crudoopsyaml.__writefile(self, dic)

        else:
            print("the key doesnot exist in the yaml file so its impossible to update")

    def deletee(self, id):
        dic = crudoopsyaml.__openfile(self)
        if id in dic.keys():
            del dic[id]
            crudoopsyaml.__writefile(self, dic)
        else:
            print("The data with the id doesnot exist in the file so I cannot delete")






def json_yaml_handling_main(filename):
    split_tup = os.path.splitext(filename)
    file_extension = split_tup[1]
    print("file extension is", file_extension)

    if file_extension == ".json":
        object1 = crudoopsjson(filename)
        return object1

    elif file_extension == ".yaml":
        object1 = crudoopsyaml(filename)
        return object1








if __name__ == "__main__":

    #filename = 'trial_python.yaml'  #change this file to json if you want to perform json operations.
    filename = 'trial_python.json'

    object1 = json_yaml_handling_main(filename)

    #print(object1.__openfile())  #private method could not be accessed
    #print(type(object1.__openfile())) #private method could not be accessed

    object1.addrow('hs', {'Name': 'lupo', 'Class': 100, 'Grade': 5, 'Rank': 1})
    object1.addrow('ha', {'Name': 'marco', 'Class': 10, 'Grade': 3.5, 'Rank': 10})
    object1.addrow('hn', {'Name': 'Narasimha', 'Class': 12, 'Grade': 1, 'Rank': 1})
    object1.addrow('hb', {'Name': 'lucy', 'Class': 1, 'Grade': 1, 'Rank': 1})

    object1.update_record('ha',
          {'Name': 'suji', 'Class': 10, 'Grade': 98, 'Rank': 1, 'subjects': ['physics', 'chemistry', 'maths']})
    object1.update_record('hb',
                      {'Name': 'sujayaa', 'Class': 1, 'Grade': 9, 'Rank': 1,
                       'subjects': ['physics', 'chemistry', 'maths']})

    object1.readone('ha')
    object1.readall()

    object1.deletee('ha')