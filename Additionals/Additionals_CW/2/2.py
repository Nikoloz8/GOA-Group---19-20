# ```1)შექმენით ფუნქცია რომელსაც ექნება ერთი პარამეტრი ასაკისთვის და ამ ფუნქციამ უნდა დააბრუნოს მხოლოდ თქვენი ასაკი, ფუნქციის გამოძახების დროს ფუნქციას არგუმენტად გადაეცით თქვენი ასაკი

age = int(input("Enter your age: "))

def age():
    return age 

# 2) მომხმარებელს შეეკითეთ სახელი, გვარი, ასაკი, საცხოვრებელი, შემდეგ შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ამ მონაცემებს და ეს ფუნქცია დააბრუნებს ერთ გრძელ წინადადებას მომხმარებლის შესახებ მაგ. hello {სახელი} {გვარი} შენ ცხოვრობ {საცხოვრებელი}```

age = (int(input("Enter your age: ")))
name = input("Enter your name: ")
lastname = input("Enter your last name: ")
living_place = input("Enter your living place: ")

def words(age, name, lastname, living_place):
    return "Hello " + name + " " + lastname + " you are live in " + living_place + "!"

print(words(age, name, lastname, living_place))