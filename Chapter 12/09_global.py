a = 89 # a is global varriable

def fun():
    global a
    a = 3
    print (a)

print(a) # since fun() is not called yet a = 89
fun()
print(a)    