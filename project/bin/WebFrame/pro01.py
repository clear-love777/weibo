import csv
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./static/login.html")
str=""
with open(path) as f:
    test = list(csv.reader(f))
    for i in test:
        if not i:
            break
        str+=i[0]
    print(str)
print(my_path)
print(path)