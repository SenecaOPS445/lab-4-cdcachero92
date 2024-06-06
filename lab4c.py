#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    address_dict = {}
    ctr = 0    

    while ctr < len(keys):
        address_dict.update({keys[ctr]:values[ctr]})
        ctr+=1

    return address_dict

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    set_york = set()
    set_newnham = set()
    for value in dict1:
        set_york.add(dict1[value])
    for item in dict2:
        set_newnham.add(dict2[item])
    
    sharedElem = set_york.intersection(set_newnham)

    return sharedElem




if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
