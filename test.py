i = 0
while i < 5:
    print(i)
    i+= 1

def great():
    print('Hello world')

great()

Great without name from user

def great(name):
    print(f"Hello {name}")

great('ali')

Great with name from user
def grat():
    name = input("Eter ame: ")
    print(f"Hello {name}")
grat()

Summin function
def total(num1,num2):
    calc= num1+num2
    print(calc)

total(1,2)

Calculator

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

# Main calculator function
def calculator():
    # Get user input for two numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    # Perform the chosen operation
    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        result = "Invalid operation."

    # Print the result
    print(f"The result of {operation} is: {result}")

# Call the main calculator function
calculator()

#Temparatures convertor
#Function to convert to celcius
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#To convert to Fahrenheit
def to_fahrenheit(celcius):
    return celcius*(9/5) + 32

# Main convertor function
def f_c_convertor():
    temperature = float(input("Enter the temperature: "))
    convert_to = input("Do you want to con vert from F to C or from C to F: ").upper()
    
    if convert_to == "F TO C":
        final_temperature = to_celsius(temperature)
        unit = "Celsius"
    elif convert_to == "C TO F":
        final_temperature = to_fahrenheit(temperature)
        unit = "Fahrenheit"
    else:
        print("Invalid conversion direction.")
        return
      
    print(f"The converted temperature is: {final_temperature:.2f} {unit}")

f_c_convertor()


