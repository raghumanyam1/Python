
#largest among them

a, b, c = 5, 12, 8
largest = max(a, b, c)
print(f"The largest number is {largest}")

#factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

#calculator program

numb1 = float(input("enter first number: "))
numb2 = float(input("enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '-':
    print(numb1 - numb2)
elif op == '+':
    print(numb1 + numb2)
elif op == '/':
    print(numb1 / numb2 if numb2 !=0 else "cannot divide by zero")
elif op == '*':
    print(numb1 * numb2) 


#prime number 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
        return True
print(is_prime(13))

