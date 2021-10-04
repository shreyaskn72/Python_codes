from jsonhandling import crudoopsjson
import pandas as pd
import numpy as np


def dict_to_txt(filename, d):

    df = pd.DataFrame.from_dict(d, orient='index')
    df=df.replace(np.nan, '', regex=True)
    np.savetxt(filename, df.values, fmt="%s")

if __name__ == '__main__':
    input_file = 'input.json'
    object1 = crudoopsjson(input_file)

    # Output from UI should be a dictionary
    d = object1.readone('text file')

    print(d)

    # Do dictionary operations here to perform optimization

    filename = "output.txt"
    a = dict_to_txt(filename, d)