marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

total_percenntage = (100*(marks1 + marks2 + marks3))/300

if(total_percenntage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass")

else :
    print("You failed,try again next year")