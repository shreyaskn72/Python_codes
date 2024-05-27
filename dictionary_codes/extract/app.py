# Sample lists of dictionaries
#big list
list1 = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Alice'},
    {'id': 3, 'name': 'Bob'},
    # More dictionaries...
]
#small list
list2 = [
    {'specific_id': 1},
    {'specific_id': 2}
]

# Create a set of 'specific_id's from list 2
ids_set = {item['specific_id'] for item in list2}

# Extract dictionaries from list 1 where 'id' is common in list 2
filtered_list1 = [item for item in list1 if item['id'] in ids_set]

# Display filtered list
print("Filtered List 1:")
print(filtered_list1)
