# ```შექმენით პროგრამა, რომელიც ბეჭდავს 5-ის ჯერადებს 1-დან 50-ის ჩათვლით for loop-ის გამოყენებით.

for i in range(0, 51, 5):
    print(i)

# დაწერეთ პროგრამა, რომელიც ბეჭდავს ლუწ რიცხვებს 2-დან 20-ის ჩათვლით for loop-ის გამოყენებით.

for i in range(2, 21, 2):
    print(i)

# დაწერეთ ალგორითმი, რომელიც დაბეჭდავს 5-იდან ათის ჩათვლით რიცხვების ნამრავლს for loop-ის გამოყენებით.

sum = 1
for i in range(5, 11):
    sum = sum * i
print(sum)


 
num = int(input("Enter random number: "))
if num % 2 == 0:
    print(num / 2)
else:
    print((num / 3) + 1)

# შექმენით ოთხი მათემატიკური ფუნქცია, თითოეულს გადაეცით ორი არგუმენტი და სახელის შესაბამისად მოახდინეთ მუშაობა. ოპერაციები: +, -, *, /.

a = 25
b = 5

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiplie(a, b):
    return a * b

def division(a, b):
    return a / b


# შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის სიგრძესა და სიმაღლეს, გამოითვლით მის ფართობს.

length = int(input("Enter length of square: "))
height = int(input("Enter height of square: "))

def area(length, height):
    return length * height


# შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის ოთხ გვერდს, გამოითვლით მის პერიმეტრს.

side1 = int(input("Enter square length of first side: "))
side2 = int(input("Enter square length of second side: "))
side3 = int(input("Enter square length of third side: "))
side4 = int(input("Enter square length of forth side: "))

def p(side1, side2, side3, side4):
    return side1 + side2 + side3 + side4

# შექმენით ფუნქცია, რომელიც მიიღებს არგუმენტად სიას და დაბეჭდეთ სიის რიცხვების ჯამი, არ გამოიყენოთ sum.

list = [1, 7, 9, 3, 15, 27]
def sum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

# შექმენით ფუნქცია, რომელიც დაბეჭდავს კონკრეტული სიიდან მინიმალურ და მაქსიმალურ რიცხვებს, არ გამოიყენოთ min და max. გამოიყენეთ def, for, if/else, indexing, print.

list_min_max = [6543, 121, 67, 921, 267, 9]

def minimal_maximal(list_min_max):
    minimal = list_min_max[0]
    maximal = list_min_max[0]
    for i in range(len(list_min_max)):
        if list_min_max[i] > maximal:
            maximal = list_min_max[i]
            list_min_max[i]
        elif list_min_max[i] < minimal:
            minimal = list_min_max[i] 
    return maximal, minimal 

# შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. თქვენი დავალებაა, რომ ამ სიის ლუწ ინდექსებზე მყოფი რიცხვების ჯამი დააბრუნოთ. აუცილებლად გამოიყენეთ return ამ და ასევე შემდეგ დავალებებში.

list = [3, 6, 4312, 123, 1432, 768, 927, 9531, 5, 43]
def even_index(list):
    sum_index = 0
    for i in range(len(list)):
        if i % 2 == 0: 
            sum_index = sum_index + list[i]
    return sum_index

# შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ ლუწია თუ კენტი ის რიცხვი.
 
integer = int(input("Enter full number: "))

def full_number(integer):
    if integer % 2 == 0:
        return "Number is even!"
    else:
        return "Number is odd!"

# ```