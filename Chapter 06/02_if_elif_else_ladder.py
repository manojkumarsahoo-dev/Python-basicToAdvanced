a = int(input("Enter your age: "))

if (a>=18):
    print("You are above age of consent")
    print("You are adult")
elif (a<0):
    print("You are entering an invalid negative age")
elif (a==0):
    print("You are entering zero age, which is not valid")
else :
    print("You are below age of consent")

print("This is the end of the program")