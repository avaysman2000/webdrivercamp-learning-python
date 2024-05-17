#!/usr/bin/python3

import random
random_num = random.randint(-10, 10)
#
if random_num < 0:
   print(random_num, " is negative")
elif random_num == 0:
   print(random_num, " is zero")
elif random_num > 0:
   print(random_num, " is positive")
