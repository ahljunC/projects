#function to add
def add(x, y):
	return x + y

#function to subtract
def subtract(x, y):
	return x - y

#function to multiply
def multiply(x, y):
	return x * y	


print("Select Operation: ")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")

#Get input from user
selection = input("Enter selection: ") 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if selection == '1':
	print(num1,"+",num2, "=", add(num1, num2))

elif selection == '2':
	print(num1, "-", num2, "=", subtract(num1, num2)) 

elif selection == '3':
	print(num1, "*", num2, "=", multiply(num1, num2))

else:
	print("invalid input")
