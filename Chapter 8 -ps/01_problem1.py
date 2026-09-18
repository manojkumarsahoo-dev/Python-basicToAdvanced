def greatest(a,b,c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>a and c>b):
        return c
    
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

greatest = greatest(a,b,c)

print(f"{greatest} is greatest")