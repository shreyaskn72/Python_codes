import itertools


#taking only interested keys from big dictionary

def big_small_mappings(small_dict, big_dict):
    mapped_dict = {}

    for k, v in small_dict.items():
        for key1, value1 in big_dict.items():
            if k == key1:
                mapped_dict[k] = value1

    return mapped_dict


#converting nested dictionary into dictionary with list as keys

def nested_dict_to_dict_list(nested_dict):
    dict_list = {}

    for k, v in nested_dict.items():
        dict_list[k] = []
        for key2, value2 in v.items():
            dict_list[k] += [value2]

    return dict_list


#Making the combinations as per interest

def final_combo(dict_list):
    final = [
        {k: v for k, v in zip(sorted(dict_list.keys()), list_prod_value)}
        for list_prod_value in itertools.product(*(dict_list[k] for k in sorted(dict_list.keys())))
    ]

    return final




if __name__ == "__main__":
    small_dict = {"a": {}, "b": {}}

    big_dict = {"a": {1: {'name': 'Emil', 'year': 2004}, 2: {'name': 'goel', 'year': 2005}, 3: {'name': 'virender', 'year': 2003}}, "c": {1: 2},
               "b": {20: {'name': 'jolly', 'year': 2004}, 21: {'name': 'param', 'year': 2005}, 22: {'name': 'praveen', 'year': 2005}}, "d": {10: 2}}


    converted_dict = big_small_mappings(small_dict, big_dict)

    print("converted mapped dictionary is")

    print(converted_dict)



    dict_list = nested_dict_to_dict_list(converted_dict)

    print(dict_list)

    final_combo = final_combo(dict_list)

    print(final_combo)

    print(len(final_combo))
