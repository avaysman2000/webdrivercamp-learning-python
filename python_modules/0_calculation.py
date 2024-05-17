#!/usr/bin/python3

#import caclulation.py as calc

if __name__=="__main__":

   import calculation as calc

   a = 4 #use this variable as a first argument to call a function 
   b = 2 #use this variable as a second argument to call a function
   
   calc_add = calc.add
   calc_sub = calc.sub
   calc_mul = calc.mul
   calc_div = calc.div

   print(a," + ",b," = ", calc_add(a, b))
   print(a," - ",b," = ", calc_sub(a, b))
   print(a," * ",b," = ", calc_mul(a, b))
   print(a," / ",b," = ", calc_div(a, b))
