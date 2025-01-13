# simple program without using function and recursion

"""count=int(input("Enter the number : "))
a,b=0,1
print("fibonacci series")
for i in range(count):
    print(a , end=" ")
    a,b=b,a+b
print()"""

#----------------------------------------------------------------------------------

# by using function
"""
def recursion(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b
    print()

count=int(input("Enter the count "))
recursion(count)"""

#-------------------------------------------------------------------------------------

#by using recursion 
# Print the first 25 Fibonacci numbers
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
print("The first 25 numbers in the Fibonacci numbers are:")
for i in range(25):
    print(fibo(i), end=" ")


