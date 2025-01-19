#for loop:

# 1) Write a program that calculates and prints the sum of numbers from 1 to 10 using a for loop.

sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum) 

# 2)Print the squares of numbers from 1 to 15.

for i in range(1, 16):
    i = i ** 2
    print(i)

# 3)Write a program that calculates and prints the sum of squares of numbers from 1 to 5 using a for loop.

sum = 0
for i in range(1, 6):
    sum = sum + i ** 2
print(sum)

# 4)Print numbers divisible by both 3 and 5 from 1 to 100 inclusive.

for i in range(1, 101):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0: 
        print(i)

# 5)Write a program that prints numbers from 10 to 1 in reverse order using a for loop.

for i in range(-9, 1):
    print(1- i)

# while loop:
# 1)Calculate the sum of digits of a number entered by the user.

digit1 = int(input("Enter any number: "))
digit2 = 0
while digit1 > 1: 
    digit1 = digit1 - 1
    digit2 = digit2 + digit1 
print("Sum of digits of a number you entered", digit2)

# 2)Write a program that uses a while loop to print numbers from 10 down to 1.

number = 11

while number > 1:
    number = number - 1
    print(number)  

# 3)Write a program that calculates and prints the sum of all integers from 1 to 100 using a while loop.

num1 = 101
num2 = 0
while num1 > 1: 
    num1 = num1 - 1
    num2 = num2 + num1 
print(num2)

# 4)Write a program that calculates and prints the square of numbers from 1 to 10 using a while loop.

number1 = 11
number2 = 0
while number1 > 1:
    number1 = number1 - 1 
    number2 = number2 + number1 ** 2
print(number2)


# If - Else:
# 1)Write an if-else statement to determine if a year entered by the user is a leap year.

year = int(input("Enter any year: "))
if year % 4 == 0:
    print("Your entered year is leap year")
else:
    print("Your entered year isn't leap year")


# 2)Check if a given string entered by the user is a palindrome.

#?

# 3)termine if a number entered by the user is positive, negative, or zero.
random_number = int(input("Enter random number: "))
if random_number < 0:
    print("Your entered number is negative")
elif random_number == 0:
    print("Your entered number is zero")
else: 
    print("Your entered number is positive")


# 4)lculate the BMI of a person based on their height and weight entered by the user and classify their BMI category using if-else.

weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

print(weight / (height ** 2))

