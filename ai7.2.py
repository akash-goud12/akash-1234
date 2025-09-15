# Buggy factorial function
def factorial(n):
    if n == 0:
        return 0  # Bug: should return 1 for factorial(0)
    else:
        return n * factorial(n - 1)