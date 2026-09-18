f = open("file2.txt")

# lines = f.readlines()

# print(lines,type(lines))

line = f.readline()
while (line!=""):
    print(line,type(line))
    line =f.readline()
f.close()