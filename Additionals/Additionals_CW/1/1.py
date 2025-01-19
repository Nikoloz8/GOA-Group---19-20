#     1) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და დააბრუნებს მათ ჯამს

def sum():
    num1 = int(input("Please enter random number: "))
    num2 = int(input("Enter random number again: "))
    return num1 + num2 

#     2) შექმენით ფუნქცია რომელიც შეეკითხება მომხარებელს რიცხვს და დააბრუნებს ლუწია თუ კენტი

def odd_even():
    number = int(input("Enter number: "))
    if number % 2 == 0: 
        return "Number is even!"
    else:
        return "Number is odd"
print(odd_even())