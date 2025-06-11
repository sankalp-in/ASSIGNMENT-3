#Calculate Factorial Using a Function

n = int ( input("Enter a number: "))

def factorial(a) :
    u = n
    fact = 1
    for i in range(a):
        fact = fact * u
        u = u - 1
    return fact
ans = factorial(n)
print("Factorial of {} is: {}".format(n,ans))
