lines = ["This is a test!-4", "This is a test!-5", "This is a test!-6"]
with open("test.txt", "w") as file:
    for line in lines:
        file.write(line + '\n')
with open("test.txt") as file:
    data = file.readlines()
del data[1]
with open("test.txt", "w") as file:
    file.writelines(data)
with open("test.txt") as file:
    data = file.readlines()
    print(data)