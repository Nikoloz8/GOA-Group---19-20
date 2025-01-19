# დაწერე ფუნქცია, რომელიც იღებს x და y პარამეტრებს და აბრუნებს მათ სხვაობას. მაგალითად, გამოიყენე არგუმენტები 10 და 5. (გამოიტანა: 5)

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

def differance(x, y):
    return x - y

# შექმენი ფუნქცია, რომელიც იღებს word1 და word2 პარამეტრებს და აბრუნებს მათ ერთად შერწყმულს. მაგალითად, გამოიყენე არგუმენტები "გამარჯობა" და "მეგობარო". (გამოიტანა: "გამარჯობა მეგობარო")

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
def concatination(word1, word2):
    return word1 + " " + word2

# დაწერე ფუნქცია, რომელიც იღებს length და width პარამეტრებს და ითვლის მართკუთხედის ფართობს. მაგალითად, გამოიყენე არგუმენტები 4 და 6. (გამოიტანა: 24)

length = int(input("Enter length of square: "))
width = int(input("Enter width of square: "))
def area(length, width):
    return width * length

# შექმენი ფუნქცია, რომელიც იღებს name პარამეტრს და აბრუნებს "გამარჯობა, [name]" შეტყობინებას. მაგალითად, გამოიყენე არგუმენტი "ანა". (გამოიტანა: "გამარჯობა, ანა")

name = input("Please enter your name: ")
def hello_name(name):
    return "გამარჯობა", name
print(hello_name(name))
 
# შექმნი ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "დიდია" თუ number 10-ზე მეტია და "პატარა" თუ ნაკლებია. მაგალითად, გამოიყენე არგუმენტი 9. (გამოიტანა: "პატარა")

number = int(input("Enter random number: "))
def big_small(number):
    if number > 10:
        return "დიდია"
    else:
        return "პატარაა"

# დაწერე ფუნქცია, რომელიც აბრუნებს შეტყობინებას "კარგი დღე გქონდეს!". პარამეტრები არ არის საჭირო.

def good_day():
    return "კარგი დღე გქონდეს!"

# შექმნი ფუნქცია, რომელიც იღებს a და b პარამეტრებს და აბრუნებს მათ ჯამს. მაგალითად, გამოიყენე არგუმენტები 7 და 3. (გამოიტანა: 10)

a = int(input("Enter random number: "))
b = int(input("Enter random number again: "))
def sum(a, b):
    return a + b

# დაწერე ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს number-ის კუბს. მაგალითად, გამოიყენე არგუმენტი 3. (გამოიტანა: 27)

number = int(input("Enter random number: "))
def cube(number):
    return number ** 3
print(cube(number))

# შექმენი ფუნქცია, რომელიც აბრუნებს შეტყობინებას "საუკეთესო ხარ!". პარამეტრები არ არის საჭირო.

def you_are_best():
    return "საუკეთესო ხარ!"

# დაწერე ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "კენტი" ან "ლუწი". მაგალითად, გამოიყენე არგუმენტი 8. (გამოიტანა: "ლუწი")

number = int(input("Enter random number: "))
def odd_even(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"