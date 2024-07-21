# Arithmetic operations script

# Addition
num1 = 10
num2 = 5
sum_result = num1 + num2
print("Sum:", num1, "+", num2, "=", sum_result)

# Subtraction
difference = num1 - num2
print("Difference:", num1, "-", num2, "=", difference)

# Multiplication
product = num1 * num2
print("Product:", num1, "*", num2, "=", product)

# Division
quotient = num1 / num2
print("Quotient:", num1, "/", num2, "=", quotient)

# Integer Division (Floor division)
integer_quotient = num1 // num2
print("Integer Quotient:", num1, "//", num2, "=", integer_quotient)

# Modulus (Remainder)
remainder = num1 % num2
print("Remainder:", num1, "%", num2, "=", remainder)

# Exponentiation
exponent = num1 ** num2
print("Exponentiation:", num1, "**", num2, "=", exponent)

# String manipulation script

# Concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print(f"Concatenated String: {concatenated_str}")

# Length of a string
length_of_str1 = len(str1)
print(f"Length of '{str1}': {length_of_str1}")

# String slicing
substring = str1[1:4]
print(f"Sliced substring of '{str1}': {substring}")

# String repetition
repeated_str2 = str2 * 3
print(f"Repeated '{str2}' three times: {repeated_str2}")

# String formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)

# Conditional statements script

# If-else statement
a = 10
b = 5
if a > b:
    print(a, "is greater than", b)
else:
    print(b, "is greater than or equal to", a)

# Nested if-else statement
num = 0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Using logical operators
x = 5
y = 7
z = 10
if x < y and x < z:
    print(x, "is the smallest")
elif y < x and y < z:
    print(y, "is the smallest")
else:
    print(z, "is the smallest")

# For loop
numbers = [1, 2, 3, 4, 5]
print("Printing numbers using a for loop:")
for number in numbers:
    print(number)

# While loop
countdown = 5
print("Countdown using a while loop:")
while countdown > 0:
    print(countdown)
    countdown -= 1

# Function for addition
def add_numbers(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract_numbers(num1, num2):
    return num1 - num2

# Main program to demonstrate the functions
if __name__ == "__main__":
    # Example usage of the functions
    a = 10
    b = 5

    # Addition
    result_addition = add_numbers(a, b)
    print("Addition of", a, "and", b, "is:", result_addition)

    # Subtraction
    result_subtraction = subtract_numbers(a, b)
    print("Subtraction of", a, "and", b, "is:", result_subtraction)

# List operations

# Creation
my_list = [1, 2, 3, 4, 5]
print("Created list:", my_list)

# Manipulation
my_list.append(6)
print("After append:", my_list)

my_list.insert(2, 10)
print("After insert:", my_list)

my_list.remove(3)
print("After remove:", my_list)

# Deletion
del my_list[0]
print("After deletion:", my_list)

# Tuple operations

# Creation
my_tuple = (1, 2, 3, 4, 5)
print("Created tuple:", my_tuple)

# Manipulation (Tuples are immutable, so we can't change them directly)
# Convert tuple to list for manipulation
tuple_as_list = list(my_tuple)
tuple_as_list.append(6)
my_tuple = tuple(tuple_as_list)
print("After append (converted to tuple):", my_tuple)

# Deletion (Since tuples are immutable, we cannot delete elements directly)
# Convert tuple to list for deletion
tuple_as_list = list(my_tuple)
del tuple_as_list[0]
my_tuple = tuple(tuple_as_list)
print("After deletion (converted to tuple):", my_tuple)

# Dictionary operations

# Creation
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Created dictionary:", my_dict)

# Manipulation
my_dict['age'] = 31
print("After update:", my_dict)

my_dict['job'] = 'Engineer'
print("After adding new key-value pair:", my_dict)

# Deletion
del my_dict['city']
print("After deletion:", my_dict)


