#ფუნქციები functions


#პითონში შეგვიძლია ჩვენით შევქმნათ ფუნქციები.

#ამისთვის შეგვიძლია გამოვიყენოთ "def" ბრძანება, რაც define-ს შემოკლებული ფორმაა.

# def say_hello():
#     print("hello")  #აქ შევქმნეით ფუნქცია "say_hello", რომელსაც გავუწერეთ მისალმება.

# say_hello()   #აქ გამოვიძახეთ ზემოთხსენებული ფუნქცია.

# say_hello()
# say_hello()
# say_hello()
# say_hello()


# def plus():
#     num1 = int(input("Enter Num1: "))
#     num2 = int(input("Enter Num2: "))
#     print("Sum of this numbers is", num1 + num2)




#  1) შექმენით 4 ფუნქცია ერთ გაყოფის ერთი გამრვალების ერთი დამატებით ერთიც გამოკლების


def plus():
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    print("Sum of this numbers is", num1 + num2)


def divide():
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    print("Division of this numbers is", num1 / num2)


def multiplie():
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    print("Multiplie of this numbers is", num1 * num2)


def minus():
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    print("Differance of this numbers is", num1 - num2)

#  2) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს, შემდეგ კი ფუნქცია დაბეჭდავს არის თუ არა ეს რიცხვი 10 ზე მეტი

def number():
    number = int(input("Enter random number: "))
    if number > 10:
        print("This number is greater than 10")
    else:
        print("This number is less than 10")