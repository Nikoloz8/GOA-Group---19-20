#Codewars solutions!

# 1)

def solution(string):
    reversed_string = ""
    length = len(string)
    while length > 0:
        length = length - 1
        reversed_string = reversed_string + string[length] 
    return reversed_string

# 2)

def summation(num):
    num = num + 1
    sum = 0
    while num > 0:
        num = num - 1
        sum = sum + num
    return sum

# 3) 
arr = [-3, 7, -9, 51, 59] #ეს სია შევქმენი მაგალითად.
def find_smallest_int(arr):
    smallest = arr[0] # აქ ვქმნი ცვლადს, რომელსაც ვუტოლებ arr სიაში მყოფ პირველ ელემენტს.
    for i in range(1, len(arr)): #აქ ვქმნი ციკლს 1 დან arr ლისთის სიგრძემდე.
        element = arr[i] #აქ ვქმნი element ცვლადს, რომელსაც ვუტოლებ arr ლისთში მყოფი ელემენტებიდან პირველის გარდა ყველას.
        if element < smallest: #აქ ვქმნი პირობას, რომ თუ ელემენტი ნაკლებია პირველ ელემენტზე, მაშინ იგი გაუტოლდება smallest ცვლადს. 
            smallest = element #ამის შემდეგ თუ ამ პირობას კიდევ შეხვდება ლისთში smallest ცვლადში მყოფ მნიშვნელობაზე ნაკლები რიცხვი,    იგი ყოველთვის გაუტოლდება smallest ცვლადს.
    return smallest

# 4)

def remove_char(s):
    string = "" #აქ ვქმნი string-ისთვის განკუთვნილ ცარიელ ცვლადს.
    count = -1 #აქ ვქმნი count ცვლადს, რომელიც ქვევით დამჭირდება. 
    for i in range(len(s) - 2):#აქ ვქმნი ციკლს, რომელსაც range ში გადავცემ იმ რაოდენობას - 2, რა სიგრძისაც იქნება s ცვლადში მოთავსებული string.
        count = count - 1  #ამ ციკლში კი ვათავსებ count ცვლადს, რომელსაც ყოველ გამეორებაზე ვაკლებ კიდევ 1-ს.          
        string = string + s[count]#აქ ზემოთ შექმნილ sting ცვლადში ვათავსებ count ცვლადს, ბოლო ასოს გარეშე, ამასთან ერთად კი შემობრუნებულს.
    unreverse_string = "" #აქ ვქმნი კიდევ ერთ ცვლადს, შემობრუნებული სტრინგის დასალაგებლად.
    length = len(string)  #აქ ვქმნი length ცვლადს რომელიც არის string ცვლადში მოთავსებული string-ის ტოლი, იგი while loop-ისთვის არის საჭირო.
    while length > 0: #აქ ვქმნი ციკლს, რომელიც განმეორდება მანამდე, სანამ string-ის სიგრძე იქნება 0-ზე მეტი.
        length = length - 1 #აქ ციკლის ყოველ გამეორებაზე ვაკლებ სიგრძეს 1-ს
        unreverse_string = unreverse_string + string[length] #აქ შემობრუნებულ სტრინგს ვალაგებ სწორი თანმიმდევრობით.
    return unreverse_string