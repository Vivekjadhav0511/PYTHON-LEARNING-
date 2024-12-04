# Numbers In Python 

a = 5
b = 6
c = 7

print(a + b)
print(a ** a)
print(5 ** 3)

x = print(a,b,c)
print(type(x))

result = 1 / 3.0
print()

print(repr("Vivek"))
print(str("vivek"))
print("Vivek")

print(1 == 2 < 3)
print(1 == 2 and  2 < 3)

import math
print(math.floor(3.5)) # closet value At Bottom 
print(math.trunc(2.9)) # Towards Zero 

import random
print(math.floor(random.random()* 10 + 1))
print(random.randint(1,10))

array = ["ADBMS","PYTHON", "DSA" ,"statistic" , "SEPM"]
print(random.choice(array))
random.shuffle(array)
print(array)
      
# ************* decimal **************
    
from decimal import Decimal
print((0.1 + 0.1 + 0.1) - 0.3 ) # 5.551115123125783e-17
print((Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3')) # 0.0

