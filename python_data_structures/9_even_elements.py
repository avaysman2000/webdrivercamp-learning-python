#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]

result_tuple = tuple(num % 2 == 0 for num in my_list)

print("My List:    ", my_list)
print("True/False: ",result_tuple)


