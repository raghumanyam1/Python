#python syntax

print("Hello World")
#This is a comment
print("Hello world")
"""This is a
multiline docstring."""
print("Hello, World!")

#python variables

x =5
y ="john"
print(x)
print(y)

x="python"
y="is"
z="awesome" 
print(x,y,z)

#dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

#if-else
a = 33
b = 200

if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#while loop

i = 1
while i<6:
  print(i)
  i +=1

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#nested
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#functions
def my_function():
  print("Hello from a funnction")

my_function()

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
