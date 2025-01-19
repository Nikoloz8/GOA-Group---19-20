# 1) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხმარებელს რიცხვის და დაუმატებს მას 1-ს.

def num_add_1():
    num = int(input("Enter any number: "))
    return "If we add 1 to your number, it will be", num + 1

# 2) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცვს და დააბრუნებს "მაგარია!", თუ რიცხვი 10-ზე მეტია.

def cool_num():
    cool_num = int(input("Enter any number: "))
    if cool_num > 10:
        return "მაგარია!"

# 3) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ ციფრს და დააბრუნებს მათ შორის უმცირესს.

def greater_less():
    num1 = int(input("Enter random number: "))
    num2 = int(input("Enter random number again: "))
    if num1 > num2:
        return num1, "is greater than", num2
    elif num1 < num2:
        return num2, "is greater than", num1
    else:
        return num1, "is equal to", num2

# 4) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ტექსტს და დააბრუნებს ტექსტის სიგრძეს.

def text_len():
    text = input("Enter Any text: ")
    return "Quantity of this symbols is", len(text)

# 5) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ რიცხვს და დააბრუნებს მათ ჯამს.

def sum():
    number1 = int(input("Enter random number: "))
    number2 = int(input("Enter random number again: "))
    return "Sum of this numbers is:", number1 + number2

# 6) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და თუ ის დადებითი იქნება, დააბრუნებს "დადებითი", და თუ უარყოფითი იქნება, "უარყოფითი".

def positivity_negativity():
    num = int(input("Enter random number: "))
    if num > 0:
        return "დადებითი"
    elif num < 0:
        return "უარყოფითი"
    else:
        return "ნული"
    


# 7) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.

def odd_even():
    num = int(input("Enter random number: "))
    if num % 2 == 0:
        return True
    else:
        return False

# 8) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ რიცხვს და დააბრუნებს მათ ჯამს დამატებული 5.

def nums_add_5():
    num1 = int(input("Enter random number: "))
    num2 = int(input("Enter random number again: "))
    return "Sum of this numbers and + 5 is", num1 + num2 + 5
print(nums_add_5())