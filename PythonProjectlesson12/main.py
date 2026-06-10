#with open ("example.txt", "r") as file:
    content = file.read()

    print(content)


with open ("example.txt", "w") as file:
    file.write("hello this is new content\n")


with open ("example.txt", "a") as file:
    file.write("hello this is new content\n")

currentTime = datetime.datetime.now()

print(currentTime.year)
print(currentTime.month)
