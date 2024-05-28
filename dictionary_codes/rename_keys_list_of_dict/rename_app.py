import json



# Sample list of dictionaries
list_of_dicts = [
    {'id': '001', 'name': 'John', 'age': 30},
    {'id': '002', 'name': 'Alice', 'age': 25},
    {'id': '003', 'name': 'Bob', 'age': 35},
    {'id': '004', 'name': 'Carol', 'age': 40}
]

# Function to rename keys in a dictionary
def rename_keys(dictionary, new_keys):
    return {new_keys.get(key, key): value for key, value in dictionary.items()}

# New keys mapping for all dictionaries
new_keys_mapping = {'id': 'person_id', 'age': 'person_age'}

# Rename keys of all dictionaries in the list
list_of_dicts = [rename_keys(dictionary, new_keys_mapping) for dictionary in list_of_dicts]

print(json.dumps(list_of_dicts,indent=4))
