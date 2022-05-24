from lib2to3.pgen2.token import EQUAL


furniture = ["table", "chair", "cabinet", "desk", "couch"]
for x in furniture:
    if x == "cabinet":
        continue
    print(x)

i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer than 15.")