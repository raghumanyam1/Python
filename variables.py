x=1
y="raghu"

print(x,y)

my_var=2
myvar=1
_my_var=3
myvar2=4
myVar=6

print(my_var)
print(myvar)
print(_my_var)
print(myvar2)
print(myVar)


x,y,z="orange", "apple", "banana"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

cars = ["audi","toyota","honda"]
x,y,z=cars
print(x)
print(y)
print(z)

#global variables
x="awe"

def myfun():
    print("python is" , x)

myfun()


x="awesome"

def myfun():
    x="fantastic"
    print("python is", x)

myfun()

print("python is",x)

#global keyword

def myfun():
    global x
    x="fun"

myfun()

print("python is",x)


x="good"
def myfun():
    global x
    x="bad"
myfun()
print("python is", x)

