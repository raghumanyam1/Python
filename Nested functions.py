def outer():
    print("This is the outer function.")
    
    def inner():
        print("This is the inner function.")
    
    inner()
outer()

def calculator():

    def add(a, c):
        return a + c

    def subtract(a, c):
        return a - c

    print(add(10, 5))
    print(subtract(10, 5))

calculator()