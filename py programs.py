#calculator program

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2 if num2 !=0 else "cannot divide by zero")


#prime number 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
        return True
print(is_prime(13))


