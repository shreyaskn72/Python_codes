import json
def rename_keys_in_list(list_of_dicts, new_keys_mapping):
    # Function to rename keys in a dictionary
    def rename_keys(dictionary, new_keys):
        return {new_keys.get(key, key): value for key, value in dictionary.items()}

    # Rename keys of all dictionaries in the list
    return [rename_keys(dictionary, new_keys_mapping) for dictionary in list_of_dicts]


# Example usage:
list_of_dicts = [
    {'id': '001', 'name': 'John', 'age': 30},
    {'id': '002', 'name': 'Alice', 'age': 25},
    {'id': '003', 'name': 'Bob', 'age': 35},
    {'id': '004', 'name': 'Carol', 'age': 40}
]

new_keys_mapping = {'id': 'person_id', 'name': 'full_name', 'age': 'person_age'}

result = rename_keys_in_list(list_of_dicts, new_keys_mapping)
print(json.dumps(result,indent=4))
