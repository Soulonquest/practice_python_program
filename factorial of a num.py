def factorial(z):
    result = 1
    for z in range(1, z+1):
        result *= z
    return result

num = 5
print(f"Factorial of a {num} is {factorial(num)}")
