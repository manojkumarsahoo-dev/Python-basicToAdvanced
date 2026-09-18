from typing import List ,Union,Tuple 
n: int = 5

name : str = "Harry"

def sum(a:int,b:int)->int:
    return a+b

print(sum(4,5))

def greeting (name:str)-> str:
    return f"Hello {name}!"
#usage
print(greeting("Alice"))