with open("testcode.txt") as file:
    data = file.readlines()
del data[1]
with open("testcode.txt", "w") as file:
    file.writelines(data)