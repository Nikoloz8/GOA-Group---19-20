#შევქმნათ პროგრამა, რომელსაც გადავცემთ მოსწავლეების სახელებს, შემდეგ კი ეს პროგრამა
#ამ სახელებიდან რენდომულად ამოარჩევს სახელებს და გაანაწილებს ჯგუფებში.

#list
  #append - ლისთის ბოლოს ამატებს ახალ ელემენტს.
  #extend - აერთიანებს ლისთებს.
  #insert - ამატებს ლისთში ელემენტს.
  #remove - შლის ლისთში ელემენტს. 


#loop
#if else
#random - ახალი ბიბლიოთეკა, რომელიც random ამორჩევაში გვეხმარება. მის გამოსაყენებლად გვჭირდება choice ფუნქცია.

import random 


Cars = ["Audi RS6", "Nissan GTR", "Nissan Silvia s14", "Toyota Supra", "Toyota Prius", "Dodge Charger", "Ford Mustang", "Dodge Hellcat"]
#print(Cars[1])  #ასე იბეჭდება ინდექსის დახმარებით ის ელემენტი, რომელიც ჩვენ გვინდა.
#random.choice(Cars)
# print(len(Cars))  len ფუნქცია გამოიყენება იმისთვის, რომ გავიგოთ თუ რამდენი ელემენტი ინახება სიაში.

Teams = []
Duo = []

while Cars != []:
    Car = random.choice(Cars)
    Duo.append(Car)
    Cars.remove(Car)

    if len(Duo) == 2:
        Teams.append(Duo)
        Duo = []

for i in range(4):
    print(Teams[i])