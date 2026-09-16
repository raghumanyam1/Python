def fun():
    print("hello world!")
fun() 


def greet(name):
    print("hello", name)
greet("Raghu")
greet("rahul")

def add(x,y):
    print(x+y)

add(10,20)

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Raghu", 22)

def myfun(fname):
    print(fname + "hiiii")

myfun("Raghu")
myfun("Rahul")
myfun("Ramesh")

def myfun(name):
    print("Hello " + name)

myfun("raghu")

def myfun(name="Raghu"):
    print("Hello " + name)

myfun("rahul")
myfun("rajesh")
myfun()
myfun("ramesh")

#keyword arguments
def myfun(animal,name):
    print("i have a", animal)
    print("my", animal+ "'s name is", name)

myfun(animal = "dog", name = "buddy")

def myfun(a,b,c,d):
    return a+b+c+d
result = myfun(10,20,30,40)
print(result)


def fun(a,b):
    if a>b:
        return a
    else:
        return b
result = fun(10,20)
print(result)




#using *args
def add(*numbers):
    print(numbers)

add(10,20,30,40)



def add(*numbers):
    total =0

    for number in numbers:
        total = total + number
    return total
print(add(10,20,30,40))

#**kwargs


def students(**details):
    print(details)

students(name="raghu", age=22, course="python")


def student(*subjects, **details):
    print("Subjects:", subjects)
    print("Details:", details)

student("python", "java", name="Raghu", age=22)
