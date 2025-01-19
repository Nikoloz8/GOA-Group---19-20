#შეასრულეთ codewars-ები, მიღებული შედეგების სქრინები ჩააგდეთ homework folder-ში, ხოლო კოდი დააკოპირეთ და ჩასვით პითონის ფაილში.

# 1)

arr = [1, 4, 6, -69, 712, -5] #codewars ცვლადებს თვითონ ქმნის, აქ ეს მაგალითად შემოვიტანე


def positive_sum(arr):  #აქ იქმნება ფუნქცია, რომელსაც პარამეტრად გადაეცემა arr[] list-ი.
    sum = 0   #აქ ვქმნი sum ცვლადს
    for i in range(len(arr)):  # აქ loop-ს ვამეორებ იმდენჯერ, რამდენიც აქვს სიგრძე arr ლისთს.
        if arr[i] > 0:  #აქ ვეუბნები, რომ თუ arr ლისთში მოცემული ელემენტი მეტია 0-ზე, ის დაუმატოს sum ცვლადს, რომელიც 0-ს გავუტოლეთ
            sum = sum + arr[i]  #აქ კი უკვე ვუმატებთ 0-ზე მეტ arr ლისთის ელემენტებს sum ცლადს.
    return sum  #აქ ვაბრუნებთ sum ცვლადს.
print(positive_sum(arr))

# 2)

def square_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i] ** 2  #აქ ფიგურულ ფრჩხილებში მოცემული i ფაქტობრივად numbers ლისთისთვის არის ინდექსის აღმნიშვნელი.
    return sum

# 3)

def double_integer(i):
    sum = 0
    sum = i + i
    return sum


    