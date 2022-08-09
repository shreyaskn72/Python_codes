from jsonhandling import crudoopsjson
import pandas as pd
import numpy as np


def dict_to_txt(filename, d):
    df = pd.DataFrame.from_dict(d, orient='index')
    df = df.replace(np.nan, '', regex=True)
    starring = df.values

    text_file = open(filename, 'w')

    for i in starring:
        list3 = list(i)
        #print(list3)

        my_string = ' '.join(map(str, list3))

        my_string2 = my_string.strip()

        #print(my_string2)

        text_file.write(my_string2 + '\n')

    text_file.close()


if __name__ == '__main__':
    input_file = 'input.json'
    object1 = crudoopsjson(input_file)

    d = object1.readone('text file')

    print(d)

    filename = "output.txt"
    a = dict_to_txt(filename, d)