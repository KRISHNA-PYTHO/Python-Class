print('---sum of digit,using Recursive function -----')

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
    
print(sum_of_digits(168))



print('-----fibannoci using recursive function-----')

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    

n=5
print(f'fibannoci series of {n} is : {fibonacci(n)}')