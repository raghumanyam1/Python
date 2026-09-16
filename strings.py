#creating a string

name = "Raghu"
city = "Banglore"
message = "welcome to python programming"

print(name)
print(city)
print(message)
#string indexing

print(name[0])
print(name[1])
print(name[2])
#Negative indexing
print(name[-1]) 
print(name[-2])
print(name[-3])

#index slicing

print(name[0:2])
print(name[:3])
print(name[2:])

print(len(name))
#string concatination

first = "Raghu"
last = "Manyam"

name = first + " " + last

print(name)

name = "Raghu "

print(name * 3)

print(name.upper())
print(name.lower())