import pandas as pd


nested_dict = {12: {'12.1': {'column1': "infrom", 'column2': 'intimate'},
                  '12.2': {'column1': "funny", 'column2': 'joke'}},
             15: {'15.1': {'column3': "I", 'column4': 'am'},
                  '15.2': {'column3': "a", 'column4': "student"}}}

df = pd.DataFrame.from_dict({(i,j): nested_dict[i][j]
                           for i in nested_dict.keys()
                           for j in nested_dict[i].keys()},
                       orient='index')

print(df)



# saving the excel
df.to_excel('nested_excel.xlsx')
print('DataFrame is written to Excel File successfully.')


#saving to csv file
df.to_csv('nested_csv.csv')
print('DataFrame is written to csv File successfully.')
