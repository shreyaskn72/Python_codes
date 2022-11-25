import pandas as pd

nested_dict = {12: {'12.1': {'column1': ["infrom", "inform2"], 'column2': ['intimate']},
                  '12.2': {'column1': "funny", 'column2': 'joke'}},
             15: {'15.1': {'column3': "I", 'column4': 'am'},
                  '15.2': {'column3': "a", 'column4': "student"}}}


nested_ids = []
frames = []

for nested_id, d in nested_dict.items():
    nested_ids.append(nested_id)
    frames.append(pd.DataFrame.from_dict(d, orient='index'))

df = pd.concat(frames, keys=nested_ids)

print(df)

# saving the excel
df.to_excel('nested_excel2.xlsx')
print('DataFrame is written to Excel File successfully.')


#saving to csv file
df.to_csv('nested_csv2.csv')
print('DataFrame is written to csv File successfully.')
