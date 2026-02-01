#AIM : Design a Python program to compute the factorial of a given integer N.
#CODER : Khan Rahmanuddin
#DATE : 30|1|26
#Hello world
#Factorial calc

num = int(input())
fact = 1
if num > 0 :
    for x in range(1,num+1):
        fact = fact * x
    print(f"Factorial of {num} is {fact}")
else :
    print(f"Factorial of {num} is Not Defined")
