#1) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

def odd_even():
    num = int(input("Enter any number: "))
    if num % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

#2) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი დადებითია თუ უარყოფითი

def positive_negative():
    number = int(input("Enter any number: "))
    if number > 0:
        print("Your number is positive")
    elif number == 0:
        print("Your number is zero")
    else: 
        print("Your number is negative")

#3) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი არის თუ არა ხუთის ჯერადი

def multiple():
    multiple_of_5 = int(input("Enter any number: "))
    if multiple_of_5 % 5 == 0:
        print("Your number is multiple of 5")
    else:
        print("Your number is not a multiple of 5")

#4) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება ასაკს შემდეგ კი დაბეჭდავს ის არის თუ არა სრულწლოვანი

def adult_or_not():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are adult!")
    else:
        print("Your are not adult!")

#5) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიხვს შემდეგ კი დაბეჭდავს ეს აყვანილი კვადრატში

def square():
    square = int(input("Enter any number: "))
    square = square ** 2
    print("Square of your entered number is:", square)

#6) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება პაროლს შემდეგ შეამოწმებს ეს პაროლი
#შეიცავს თუ არა 8 სიმბოლოს თუ შეიცავს დაბეჭდეთ რომ რეგისტრაციამ წარმატებით ჩიარა,
#შხვა შემთხვევაში ხელახლა შეეკითხეთ პაროლი და უთხარი რომ აუცილებელია შეიყვანოს 8 სიმბოლო

def password():
    password = input("Please enter your password: ")
    while len(password) != 8:
        print("You need to use only 8 symbol!")
        password = input("Please enter your password again: ")
        if len(password) == 8:
            print("Registration was succesful!")

#7) შექმენით ფუნქცია რომელიც მომხმარებელს 10ჯერ შეეკითხება რიცხვს,
#ამ რიცხვებს დაამატებს სიაში, შემდეგ კი ამ სიიდან მიწვდება თითოეულს და დაბეჭდავს მათ კვადრატებს

print("Please enter numbers!")
def ten_numbers():
    numbers_list = []
    for i in range(10):
        numbers = int(input("Enter random number: "))
        numbers_list.append(numbers)
        counter = 0
    while counter < len(numbers_list):
        print("Square of", numbers_list[i], "is", numbers_list[i] ** 2)
        counter = counter + 1