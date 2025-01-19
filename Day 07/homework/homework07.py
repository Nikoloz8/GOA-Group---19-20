#1) დავალება: მომხმარებელს შემოატანინეთ 4 სხვადასხვა ტიპის მონაცემი (string,integer,float,boolean) შემდეგ დაბეჭდეთ ეს შემოტანილი მონაცემები და მათი მონაცემთა ტიპები.

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
height = float(input("Enter Your Height: "))
studying_in_goa = bool(input("You Are Studying In GOA (Enter True Or False): "))
print(name, age, height, studying_in_goa)
print(type(name), type(age), type(height), type(studying_in_goa))

#2) შექმენით 5+ ცვლადი და ისე შეადარეთ ერთმანეთს რომ დაიბეჭდოს True.
num1 = 21
num2 = 69
num3 = 12
num4 = 95
num5 = 33
num6 = 48
num7 = 121
num8 = 132

print(num1 < num8, num2 > num3, num4 > num1, num5 < num6, num7 < num8, num8 > num3)

#3) დაწერეთ True და False ყველა შესაძლო ვარიანტი and და or ოპერატორებზე
#  მაგ: True and False = False
#               True or False = True
# და ეს ყველაფერი დაპრინტეთ მაგ:  print(True and False) #False

True and False
False and False
False and True
True and True

True or False
False or False
False or True
True or True

print(True and False, False and False, False and True, True and True)
print(True or False, False or False, False or True, True or True)