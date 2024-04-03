# create a program to calculate the nth number of the fibonacci sequence

# take the user input as n
n = int(input("Enter the number of terms: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(n))