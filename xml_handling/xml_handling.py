import xmltodict
from dict2xml import dict2xml

import os

class crudoopsxml:

    def __init__(self, filename):

        self.filename = filename
        if not os.path.exists(self.filename):
            print("The xml file doesnot exist. So when you create first resource.. xml is created automatically")

    def open_file(self):
        # Open the sample xml file and read it into variable
        with open(self.filename) as f:
            xml_example = f.read()

        # Parse the XML into a Python dictionary
        xml_dict = xmltodict.parse(xml_example)

        return xml_dict

    def write_file(self, xml_dict):
        xml_string = dict2xml(xml_dict, indent="   ")

        with open(self.filename, "w") as file1:
            file1.write(xml_string)

    def readone(self, id):
        xml_dict = crudoopsxml.open_file(self)
        if id in xml_dict["student"].keys():
            print("The student with the id", id, "is", xml_dict["student"][id])

        else:
            print("The id doesnot exist")

    def readall(self):
        xml_dict = crudoopsxml.open_file(self)
        print("The details of all the students inside the xml file is:")
        print(xml_dict["student"])

    def deletee(self, id):
        xml_dict = crudoopsxml.open_file(self)
        if id in xml_dict["student"].keys():
            del xml_dict["student"][id]

            crudoopsxml.write_file(self, xml_dict)

        else:
            print("The data with the id doesnot exist in the file so I cannot delete")

    def addresource(self, id, new):
        try:
            xml_dict = crudoopsxml.open_file(self)
            if id in xml_dict["student"].keys():
                print("the id already exist. Change the id please")
            else:
                xml_dict["student"][id] = new

                crudoopsxml.write_file(self, xml_dict)

        except FileNotFoundError:
            dicwrite = {id: new}
            xml_string = dict2xml(dicwrite, wrap='student', indent="   ")
            with open(self.filename, "w") as file1:
                file1.write(xml_string)

    def updatxml(self, id, value):
        xml_dict = crudoopsxml.open_file(self)
        if id in xml_dict["student"].keys():
            xml_dict["student"][id] = value

            crudoopsxml.write_file(self, xml_dict)

        else:
            print("the key doesnot exist in the xml file so its impossible to update")



if __name__ == "__main__":
    filename = 'trial.xml'
    object1 = crudoopsxml(filename)

    object1.addresource('hs', {'Name': 'lupo', 'Class': 100, 'Grade': 5, 'Rank': 1})
    object1.addresource('ha', {'Name': 'marco', 'Class': 10, 'Grade': 3.5, 'Rank': 10})
    object1.addresource('hn', {'Name': 'Narasimha', 'Class': 12, 'Grade': 1, 'Rank': 1})
    object1.addresource('hb', {'Name': 'lucy', 'Class': 1, 'Grade': 1, 'Rank': 1})

    object1.updatxml('ha',
                      {'Name': 'suji', 'Class': 10, 'Grade': 98, 'Rank': 1,
                       'subjects': ['physics', 'chemistry', 'biology']})

    object1.updatxml('hb',
                      {'Name': 'sujayaa', 'Class': 1, 'Grade': 9, 'Rank': 1,
                       'subjects': ['physics', 'chemistry', 'maths']})

    object1.readone('ha')

    object1.readall()

    object1.deletee('ha')
