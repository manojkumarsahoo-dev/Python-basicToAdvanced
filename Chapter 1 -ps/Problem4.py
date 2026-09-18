import os

directory_path = '/riot games'

contents = os.listdir(directory_path)

for item in contents:
    print(item)