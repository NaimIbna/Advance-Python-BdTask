# Find the factorial of a given number using loop

def factorial_num(x):
    if x < 0:
        print("Factorial does not exist for negative numbers")
    elif x == 0 or x == 1:
        return 1
    else:
        return(x*factorial_num(x-1))

n = int(input("Enter your number: "))

result = factorial_num(n)

print("Factorial of", n , "is: ",result)
