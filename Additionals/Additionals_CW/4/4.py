# ```შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს 2 რციხვს, ხოლო ამ 2 რიცხვს შორის გამოიყენეთ ყველა არითმეტიკული ოპერაცია (+,-,*,/,%,//), საბოლოოდ დაბეჭდეთ შედეგები ტერმინალში + ახსენით თითოეული ნაწილი კოდის რატომ დაწერეთ კონკრეტული ხაზი და რას აკეთებს.

a = int(input("Enter random number: ")) #აქ ვქმნი a ცვლადს, რომელშიც ვათავსებ მომხმარებლის მიერ შემოტანილ პირველ რიცხვს.
b = int(input("Enter random number again: ")) #აქ ვქმნი b ცვლადს, რომელშიც ვათავსებ მომხმარებლოს მიერ შემოტანილ მეორე რიცხვს.
print(a + b) #აქ ვასრულებ მომხმარებლის მიერ შემოტანილ რიცხვებს შორის მიმატების ოპერაციას.
print(a - b) #აქ ვასრულებ მომხმარებლის მიერ შემოტანილ რიცხვებს შორის გამოკლების ოპერაციას.
print(a * b) #აქ ვასრულებ მომხმარებლის მიერ შემოტანილ რიცხვებს შორის გამრავლების ოპერაციას.
print(a / b) #აქ ვასრულებ მომხმარებლის მიერ შემოტანილ რიცხვებს შორის გაყოფის ოპერაციას.
print(a % b) #აქ ვასრულებ მომხმარებლის მიერ შემოტანილ რიცხვებს გაყოფის ოპერაციას, თუმცა % ოპერატორი ტერმინალში მხოლოდ ნაშთს დააბრუნებს.
print(a // b) #აქ ვასრულებ მომხმარებლის მიერ შემოტანილ რიცხვებს შორის გაყოფის ოპერაციას, თუმცა // ოპერატორი ტერმინალში დააბრუნებს რიცხვს       ნაშთის/ათწილადის გარეშე.

#   შემოატანინეთ მომხარებელს ასაკი და შეამოწმეთ არის თუ არა 18 წელზე მეტის და 20 წელზე ნაკლების მიღებული შედეგი დაპრინტეთ

age = int(input("Enter your age: "))
if age > 18 and age < 20:
    print(True)
else:
    print(False)

#  ჩამოწერეთ ხუთ-ხუთი მაგალითი ყველა ლოგიკურ ოპერატორზე > ,<, <=, >=, !=, == 

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

#  მომხმარებელს პირველ ინფუთში მთელი რიცხვი, ხოლო მეორე ინფუთში ათწილადი შემოატანინეთ. საბოლოოდ დაბეჭდეთ ცვლადების მნიშვნელობების მონაცემთა ტიპები

float = float(input("Enter random float: "))
integer = int(input("Enter random integer: "))
print(type(float), type(integer))
 
#  შექმენით რამოდენიმე სხვადასხვა ტიპის ცვლადი და დაბეჭდეთ მათი მონაცემთა ტიპები

boolean = True
integer = 5
float = 5.5 
string = "string"
print(type(boolean), type(integer), type(float), type(string))

#  ) მომხმარებელს შემოატანინეთ 1 დან 7-ის ჩათვლით რომელიმე რიცხვი ამის შემდეგ კი გამოიყენეთ if elif else რომ შეუსაბამოდ კვირის დღე 1 ორშაბათისთვის 2 სამშაბათისთვის 3 ოთხშაბათისთვის და ასე შემდეგ

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


#  შექმენით ისეთი while ციკლი რომელიც 0 დან 10 ის ჩათვლ;ით დაბეჭდავს ყველა რიცხვს და if else  გამოყენებით გაიგეთ არის თუ არა ლუწი ან კენტი

count = 11

while count >= 1:
    count = count - 1
    if count % 2 == 0:
        print(count, "is even!")
    else:
        print(count, "is odd!")


# მომხმარებელს შემოატანინეთ თავისი ასაკი და შეამოწმეთ თუ მომხმარებლის ასაკი მეტია 5 ზე და ნაკლები 12 ზე დაუბეჭდეთ რომ არის ბავშვი , სხვა შემთხვევაში თუ მომხმარებლის ასაკი არის 12 ზე მეტი და 18 ზე ნაკლები დაუბეჭდეთ რომ არის თინეიჯერი და თუ არის 18 ზე მეტი დაუბეჭდეთ რომ არის ზრდასრული

age = int(input("Enter your age: "))
if age > 5 and age < 12:
    print("You are kid!")
elif age > 12 and 18 > age:
    print("You are teenager!")
elif age < 0: 
    print("Bro, you ain't even born!")
else:
    print("You are adult!")

# მომხმარებელს ჯერ შემოატანინეთ ბიუჯეტი, შემდეგ კი ის თანხა, რომელიც სასურველი ნივთის საყიდლად სჭირდება. დაბეჭდეთ შეუძლია ყიდვა თუ არა.```

budget = int(input("Enter your budget: "))
price = int(input("Enter price of item you want to buy: "))

if budget >= price:
    print("You can buy it!")
else:
    print("You can't buy it.")