def extract_list_of_dictionaries(big_list, small_list):


    # Create a set of 'specific_id's from list 2
    ids_set = {item['specific_id'] for item in small_list}

    # Extract dictionaries from list 1 where 'id' is common in list 2
    filtered_list1 = [item for item in big_list if item['id'] in ids_set]

    # Display filtered list
    print("Filtered List 1:")
    print(filtered_list1)

    return filtered_list1

if __name__ == "__main__":
    # Sample lists of dictionaries
    # big list
    list1 = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Alice'},
        {'id': 3, 'name': 'Bob'},
        # More dictionaries...
    ]
    # small list
    list2 = [
        {'specific_id': 1},
        {'specific_id': 3}
    ]

    filtered = extract_list_of_dictionaries(big_list=list1, small_list=list2)
    print("filtered is")

    print(filtered)




