# Rename Keys of Dictionaries in a List

This Python script demonstrates how to rename keys of dictionaries within a list of dictionaries.

## Overview

Suppose you have a list of dictionaries where each dictionary represents an entity with keys that you want to rename uniformly across all dictionaries. This script provides a way to achieve that by renaming keys based on a specified mapping.

## Requirements

- Python 3.x

## Usage

1. Define your list of dictionaries in the Python script.
2. Modify the `new_keys_mapping` dictionary to specify the renaming mapping for keys.
3. Run the script.
4. The script will output the list of dictionaries with keys renamed according to the specified mapping.

## Example

```python
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
new_keys_mapping = {'id': 'person_id', 'name': 'full_name', 'age': 'person_age'}

# Rename keys of all dictionaries in the list
list_of_dicts = [rename_keys(dictionary, new_keys_mapping) for dictionary in list_of_dicts]

print(list_of_dicts)
