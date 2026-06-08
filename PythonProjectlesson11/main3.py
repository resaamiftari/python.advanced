import os


lines = ["hello world\n","Welcome to python\n"]

with open("example2.txt", "w") as file:
    ##file.write("kete rresht deshiroj ta shenoj ne file example 2")

    file.writelines(lines)


if os.path.exists("example2.txt"):
    print("example2.txt exists")

    