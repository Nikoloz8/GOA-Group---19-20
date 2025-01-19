# 1) შექმენით კალკულატორის ფუნქცია  რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და მოქმედების ტიპს(მიმატება, გამოკლება, გამრავლება, გაყოფა) შესაბამისად ფუნქცია დააბრუნებს ანუ დაბეჭდავს შედეგს იმისდამიხედვით მომხმარებელს რა სურს და რა რიცხვები შემოიტანა, მაგალითად მომხმარებელმა თუ შემოიტანა 5 და 2 და ასევე მას სურს გამრავლება ფუნქციამ უნდა დააბრუნოს დაბეჭდოს შედეგად 2 * 5 ანუ 

def calculation():
    value1 = int(input("Enter value1 for calculation: "))
    operator = input("Enter operator: ")
    value2 = int(input("Enter value2 for calculation: "))
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "/":
        return value1 / value2
    else: 
        return value1 * value2
print(calculation())

# 2) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს

list = [1, 9, 7, 3]
def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum
print(sum_list(list))

# 3) შექმენით ფუნქცია რომელშიც დააბრუნებს სიაში არსებული რიცხვების საშუალო არითმეტიკულკს

numbers = [1, 5, 4, 2, 1, 9, 3]

def arithmetical_mean(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    return sum / len(numbers)
print(arithmetical_mean(numbers))


# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი

def odd_even():
    odd_or_even = int(input("Enter any number: "))
    if odd_or_even % 2 == 0:
        return "Your number is even!"
    else:
        return "Your number is odd!"
print(odd_even())

# 5) შექმენით დროში მოგზაურობის ფუნქცია რომელიც მომხმარებელს შეეკითხება მის ახლანდელ ასაკს და ამჟამინდელ წელს, ასევე რამდენი ხანით სურს დროშ მოგზაურობა შემდეგ კი ფუნქციამ უნდა დააბრუნოს დაბეჭდოს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი, ასევე დაამატეთ რომ მომხმარებელმა მიიღოს გადაწყვეტილება წარსულში სურს დრში მოგზაურობა თუ მომავალში

def time_travel():
    age = int(input("Please enter your age for now: "))
    year = int(input("Please enter what year is for now: "))
    past_future = int(input("Enter 1, if you want to travel in past, enter 2 if you want to travel in future: "))
    time_of_travel = int(input("Now, enter how many years you want to jump into past/future: "))
    if past_future == 1 and (age - time_of_travel) > 0: 
        return "Now is", year - time_of_travel, ", and you are", age - time_of_travel, "years old!" 
    elif past_future == 1 and (age - time_of_travel) < 0: 
        return "Now is", year - time_of_travel, ", and you are not even born, or you are", age - time_of_travel, "years old!" 
    elif past_future == 2:
        return "Now is", year + time_of_travel, ", and you are", age + time_of_travel, "years old!"
    else:
        return "Error!"

print(time_travel())