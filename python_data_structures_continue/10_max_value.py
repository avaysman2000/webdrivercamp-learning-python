#!/usr/bin/python3
def max_value(d):

    if d is None:
        return None

    max_key = None
    max_value = float('-inf')  # Initialize max_value to negative infinity
    
    for key, value in d.items():
        if isinstance(value, int) and value > max_value:
            max_key = key
            max_value = value
    
    return max_key

if __name__=="__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")
    max_key = max_value(None)
    print(f"Max number - {max_key}")
