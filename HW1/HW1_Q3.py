## Problem 3

# iterative function
def sum_it(n): #when we call this function later, we feed it with variable n
    sum = 0   #initialize a counter
    for i in range (1,n+1):
        sum += i
    return sum

print(sum_it(100))

# recursive function
def sum_rec(n):
    if n==1:
        return 1
    else:
        return n+sum_rec(n-1)

print(sum_rec(100))