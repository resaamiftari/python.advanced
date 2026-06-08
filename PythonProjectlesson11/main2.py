with open("example.txt","r") as file:
    content = file.read()

    print(content)


with open("example.txt", "r") as file:
    file1 = file.readline() ##kjo e lexon vetem nje line te kodit

    print(file1)


with open("example.txt", "r") as file:
    lines = file.readlines()

    print(lines)