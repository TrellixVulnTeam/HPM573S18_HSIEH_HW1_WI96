## Problem 1_1
x=17
print('Setting x=',x)

# integer
y1=x
print('y1 is',y1)
print('y1 is an object of', type(y1))

# float
y2=float(x)
print('y2 is',y2)
print('y2 is an object of', type(y2))

# string
y3=str(x)
print('y3 is',y3)
print('y3 is an object of', type(y3))

# Boolean '17 > 14'
y4=bool(x>14)
print('y4 is an object of', type(y4))
print('Is it true or false that y4 is greater than 14? Ans: It is', y4)

## Problem1_2
text='The value of x is'+' '+ str(y1)+'.'
print(text)