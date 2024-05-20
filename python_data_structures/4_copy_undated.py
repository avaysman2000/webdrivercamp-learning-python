#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

#if 0 <= index < len(list_):
#   list_[index] = element_to_replace
#
#print(list_)

modified_list = list(list_)

if 0 <= index < len(modified_list):
    modified_list[index] = element_to_replace

print("Copy:    ", modified_list)
print("Original:", list_)

