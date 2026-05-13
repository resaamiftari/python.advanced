greetings= "Hello"

def greet(name):
    global message

    message = f" {greetings},{name}"
    print(message)

    greet("bob")
    print(message)


