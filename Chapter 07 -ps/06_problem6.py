#finding factorial 
n = int(input("Enter the number: "))
product =1
for i in range(1, n+1): # we need 1 to n
    product = product * i

print(f"The factorial of {n} is {product}")    