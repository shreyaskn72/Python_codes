import json


def extract_list_of_dictionaries(big_list, small_list, big_id, small_id, small_include):
    result = [
        {**item, small_include: small_item[small_include]}
        for item in big_list
        for small_item in small_list
        if item[big_id] == small_item[small_id]
    ]

    return result

if __name__ == "__main__":
    big_list = [
        {'id': 1, 'name': 'John', 'age': 30},
        {'id': 2, 'name': 'Alice', 'age': 25},
        {'id': 3, 'name': 'Bob', 'age': 35},
        {'id': 4, 'name': 'Carol', 'age': 40}
    ]

    small_list = [
        {'specific_id': 2, 'weight': 65},
        {'specific_id': 4, 'weight': 72}
    ]

    result = extract_list_of_dictionaries(big_list=big_list, small_list=small_list, big_id="id", small_id="specific_id", small_include= "weight")

    print(json.dumps(result,indent=4))




