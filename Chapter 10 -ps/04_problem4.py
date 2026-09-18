class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**(1/2):g}")

    @staticmethod
    def hello():
        print("Hello there!")

user_num = int(input("Enter any number: "))
a = Calculator(user_num)
a.hello()
a.square()
a.cube()
a.squareroot()   