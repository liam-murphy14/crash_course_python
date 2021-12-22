"""Stores and retrieves different users' favorite numbers"""

import json

filename = "fav_nums.json"

def get_num_dict():
    try:
        with open(filename, 'r') as f:
            num_dict = json.load(f)
    except FileNotFoundError:
        num_dict = {}
        return num_dict
    else:
        return num_dict

def get_input():
    num_dict = get_num_dict() 
    while True:
        name = input("What is your name ?? ").lower()
        if name in num_dict.keys():
            print("That name is already taken, please choose another")
        else:
            break
    while True:
        try:
            num = int(input("What is your favorite number ?? "))
        except ValueError:
            print("Please enter a valid number")
        else:
            break
    num_dict[name] = num
    return num_dict

def run_and_store():
    num_dict = get_input()
    with open(filename, 'w') as f:
        json.dump(num_dict, f)

run_and_store()
    
