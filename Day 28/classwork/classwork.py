# დავალება 1) 0-დან 20-ის ჩათვლით გამოიტანეთ რიცხვები.

for i in range(21):
    print(i)

# დავალება 2) მომხმარებელს შემოატანინეთ ორი რიცხვი და მათ შორის არსებულები გამოიტანეთ.

num1 = int(input("Enter random number: "))
num2 = int(input("Enter random number again: "))
if num2 > num1:
    for i in range(num1, num2):
        print(i)
elif num1 > num2:
    for i in range(num2, num1):
        print(i)
else:
    print("ამ რიცხვებს შორის არ არის შუალედი, ტოლია!") 

# დავალება 3) 50-დან 100-ის ჩათვლით გამოიტანეთ რიცხვები.

for i in range(50, 101):
    print(i)

# დავალება 4) 100-დან 50-ის ჩათვლით გამოიტანეთ რიცხვები. (ჩათვალეთ დავალება 3-ის საპირისპირო)
numbers = 101

while numbers > 50:
    numbers = numbers - 1
    print(numbers)

#ან

for i in range(100, 49, -1):
    print(i)

# დავალება 5) 0-დან 50-ის ჩათვლით გამოიტანეთ რიცხვები და ბოლოს მათი ჯამი.

sum = 0
for i in range(51):
    sum = sum + i
print(sum)

# დავალება 6) მომხმარებელს შეეკითხეთ, რომ შემოიტანოს მთელი რიცხვი. შემდეგ 0-დან ამ რიცხვამდე გამოიტანეთ ყველა რიცხვი.

num = int(input("Enter whole number: "))
if num > 0:
    for i in range(0, num):  # თუ ამ რიცხვის ჩათვლით, მაშინ range(0, num + 1).
        print(i)
else:
    for i in range(0, num, - 1): #თუ მოვინდომებთ ამ რიცხვის ჩათვლით, მაშინ range(0, num - 1, -1)
        print(i)

# დავალება 7) მომხმარებელს შეეკითხეთ ასაკი. შექმენით ცვლადი, სადაც შენახული იქნება 10 წლის შემდეგ მომხმარებლის ასაკი, 
# საბოლოოდ დაპრინტეთ მომხმარებლის ასაკსა და 10 წლის შემდეგ წლოვანებას შორის არსებული მთელი რიცხვები.

age = int(input("Enter your age: "))
age_after_ten = age + 10
for i in range(age + 1, age_after_ten):
    print(i)



#  8) შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს 5 რიცხვს, ხოლო ამ 5 რიცხვს შორის გამოიყენეთ
#  ყველა არითმეტიკული ოპერაცია (+,-,*,/,%,//), საბოლოოდ დაბეჭდეთ შედეგები ტერმინალში + ახსენით
#  თითოეული ნაწილი კოდის რატომ დაწერეთ კონკრეტული ხაზი და რას აკეთებს.

num1 = int(input("Enter Random Number 1: "))
num2 = int(input("Enter Random Number 2: "))
num3 = int(input("Enter Random Number 3: "))  #აქ შემომაქვს ცვლადები და მინიჭების ოპერატორის დახმარებით მათ ვაკავშირებ input ფუნქციებთან, რომელსაც თავიდანვე ვაქცევ integer-ად.
num4 = int(input("Enter Random Number 4: "))
num5 = int(input("Enter Random Number 5: "))

print(num1 + num2 + num3 + num4 + num5) #როგორც დავალებაშია, აქ ვასრულებ პირველ არითმეტიკულ ოპერაციას, ანუ მიმატებებს და ვბეჭდავ.
print(num1 - num2 - num3 - num4 - num5) #აქ ვასრულებ გამოკლებებს.
print(num1 * num2 * num3 * num4 * num5) #აქ ვასრულებ გამრავლებებს.
print(num1 / num2 / num3 / num4 / num5) #აქ ვასრულებ გაყოფებს.
print(num1 % num2 % num3 % num4 % num5) #აქ ვბეჭდავ გაყოფის შედეგად მიღებულ ნაშთებს.
print(num1 // num2 // num3 // num4 // num5) #აქ ვბეჭდავ უნაშთო integer-ებს.

# 9) შემოატანინეთ მომხმარებელს ასაკი და შეამოწმეთ არის თუ არა 18 წელზე მეტის და 20 წელზე ნაკლების, მიღებული შედეგი დაპრინტეთ.

age = int(input("Enter your age: "))
print("User are over 18 years old:", age > 18, "User are less than 20 years old:", 20 > age)

# 10) ჩამოწერეთ ხუთ-უთი მაგალითი ყველა ლოგიკურ ოპერატორზე >, <, <=, >=,  !=, ==.
5 > 3 # True
10 > 15 # False
7 > 7 # False
20 > 10 # True
100 > 50 # True

3 < 5 # True
15 < 10 # False
7 < 7 # False
10 < 20 # True
50 < 100 # True

5 <= 5 # True
3 <= 4 # True
10 <= 10 # True
15 <= 12 # False
8 <= 9 # True

5 >= 5 # True
10 >= 7 # True
4 >= 6 # False
15 >= 15 # True
8 >= 3 # True

5 != 3 # True
10 != 10 # False
7 != 8 # True
12 != 15 # True
6 != 6 # False

5 == 5 # True
10 == 5 # False
8 == 8 # True
3 == 2 # False
15 == 15 # True


# 11) მომხმარებელს პირველ ინფუთში მთელი რიცხვი, ხოლო მეორე ინფუთში ათწილადი შემოატანინეთ.
# საბოლოოდ შეადარეთ ცვლადების მნიშვნელობების მონაცემთა ტიპები.

integer = int(input("Enter random number: "))
float = float(input("Enter random number again: "))
print(type(integer) == type(float))

# 12) შექმენით რამდენიმე სხვადასხვა ტიპის ცვლადი და დაბეჭდეთ მათი მონაცემთა ტიპები.

integer = 5
float = 2.5
boolean = True
string = "string"
print(type(integer), type(float), type(boolean), type(string))

# 13) მომხმარებელს შემოატანინეთ 1-დან 7-ის ჩათვლით რომელიმე რიცხვი, ამის შემდეგ კი გამოიყენეთ if elif else,
# რომ შეუსაბამოთ კვირის დღე 1 ორშაბათისთვის, 2 სამშაბათისთვის, 3 ოთხშაბათისთვის და ასე შემდეგ.

week_day = int(input("Enter number of day in week for now: "))

if week_day == 1:
    print("First day of week is monday!")
elif week_day == 2:
    print("Second day of week is tuesday!")
elif week_day == 3:
    print("Third day of week is wednesday!")
elif week_day == 4:
    print("Fourth day of week is thursday!")
elif week_day == 5:
    print("Fifth day of week is friday!")
elif week_day == 6:
    print("Sixth day of week is saturday!")
elif week_day == 7:
    print("Seventh day of week is sunday!")
else:
    print("Error!")

# 14) შექმენით ისეთი while ციკლი, რომელიც 0-დან 10 ის ჩათვლით დაბეჭდავს ყველა რიცხვს და
# if else გამოყენებით გაიგეთ არის თუ არა ლუწი ან კენტი, დასერჩეთ how to know if number is even or odd  in python.

number = 11
while number >= 1:
    number = number - 1
    if number % 2 == 0:
        print(number, "is even!")
    else:
        print(number, "is odd!")


# 15) მომხმარებელს შემოატანინეთ თავისი ასაკი და შეამოწმეთ, თუ მომხმარებლის ასაკი მეტია 5-ზე და ნაკლები 12-ზე დაუბეჭდეთ,
# რომ არის ბავშვი, სხვა შემთხვევაში, თუ მომხმარებლის ასაკი არის 12-ზე მეტი და 18-ზე ნაკლები დაუბეჭდეთ,
# რომ არის თინეიჯერი და თუ არის 18-ზე მეტი დაუბეჭდეთ, რომ არის ზრდასრული.

age = int(input("Enter your age: "))
if age > 5 and age < 12:
    print("You are kid!")
elif age > 12 and 18 > age:
    print("You are teenager!")
elif age < 0: 
    print("Bro, you ain't even born!")
else:
    print("You are adult!")

# 16) მომხმარებელს ჯერ შემოატანინეთ ბიუჯეტი, შემდეგ კი ის თანხა,
# რომელიც სასურველი ნივთის საყიდლად სჭირდება. დაბეჭდეთ შეუძლია ყიდვა, თუ არა.

budget = int(input("Enter your budget: "))
price = int(input("Enter price of item you want to buy: "))

if budget >= price:
    print("You can buy it!")
else:
    print("You can't buy it.")