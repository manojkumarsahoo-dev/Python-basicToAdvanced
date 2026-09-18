class Employee:
    language = " Python"
    salary = 1200000

    def __init__(self):
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")
harry = Employee()
harry.name = "Harry"
print(harry.name,harry.salary)

rohan = Employee()