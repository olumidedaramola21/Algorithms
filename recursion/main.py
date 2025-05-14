"""
- Recursion is defined as function calling itself
- Almost all the situations where we use loops, we can substitute the loops using recursion
- Recursion solves problems that seems complex at first
"""
# Factorial
"""
n! = n . (n-1) . (n-2)... 1
5! = 5 . 4 . 3 . 2 . 1 
"""
def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result

print(factorial(5))

# Steps to consider in recursion
"""
1. Identifying base case to ensure the algorithm doesn't run forever
"""

def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n * (factorial_recursion(n -1))

print(factorial_recursion(5))

"""
How recursion works
- Computer uses a stack to keep track of the functions
- Call stack
"""

"""
Dynamic programming
- optimization techniques
- Mainly applied to recursion
- Can reduce the complexity of recursive algorithms.
- Used for:
    - any problem that can be divided into smaller subproblems
    - subproblems overlap
- Solutions of subproblems are saved, avoiding the need to recalculate.
    - Memoization
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        fibonacci(n-1) + fibonacci(n-2)

cache = [None]*(100)
def fibo_dynamic(n):
    if n <= 1:
        return n
    
    # check if the value exists
    if not cache[n]:
        cache[n] = fibo_dynamic(n-1) + fibo_dynamic(n-2)

    return cache[n]
print(fibo_dynamic(6))
