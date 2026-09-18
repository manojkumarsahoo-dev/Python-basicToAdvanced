a = int(input("Enter your age: "))

#if statement no :1

if(a%2 ==0):
    print("a is even")
#end of if statement no :1
# if statement no :2

if (a>=18):
    print("You are above age of consent")
    print("Good for you")
elif (a<0):
    print("You are entering an invalid negative age")
elif (a==0):
    print("You are entering zero age, which is not valid")
else :
    print("You are below age of consent")

#End of if statement no :2    

print("This is the end of the program")     