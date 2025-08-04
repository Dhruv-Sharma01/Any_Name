import os,sys
from math import *

def badFunc(x,y):
 a=10
  b=20
   if x>y:
    print('x is greater')
   elif y>x:
        print("y is greater")
   else:
    print("equal")
   return
   print("this will never run")

def doStuff():
    global x
    x=5
    for i in range(10):
     if i%2==0:
         continue
     else:
          break
    return

def input(x):
    pass

z = lambda x : x+1
def _():pass
print = 5
eval("print('bad')")
