for i in range(125):
    print("Hello World")

#for i in range ფუნქცია გამოიყენება loop ისთვის, ანუ ბრძანების იმდენჯერ შესასრულებლად, რამდენჯერაც გადავცემთ ჩვენ მას.
#აქ მოთავსებულ "i"-ს ეწოდება საიტერაციო ცვლადი. საიტერაციო ცვლადს შეგვიძლია ის დავარქვათ რაც გვინდა. 
#საიტერაციო ცვლადი შეგვიძლია ჩავანაცვლოთ ნებისმიერი სიტყვით. "i" iteration-ის (იტერაციის) შემოკლებული ფორმაა.

for letter in range(200):
    print(letter)

for i in range(200):
    print(i) 

#თუ "i"-ს ადგილას მყოფი სიმბოლოები დაემთხვევა print ფუნქციაში მოთავსებულ სიმბოლოებს(სტრინგის გარეშე), 
#print ფუნქცია გამოგვიტანს range ფუნქციაში მოთავსებულ რაოდენობას 0 იდან. 
#ეს range არის ფუნქცია. ნებისმიერ რამეს რასაც ბოლოში ფრჩხილები ეწერება არის ფუნქცია.

#ასეც შეგვიძლია მოვიქცეთ:

for i in range(100):
    print("hello world" + str(i))


#საბოლოოდ, რომ ვთქვათ, ეს არის for loop.

#საკლასო დავალება: გამოიტანეთ 50 ამდე ყველა კენტი რიცხვი.

for i in range(50):
    if (i % 2 == 1):
        print(i) #Done!

#range ფუნქციას გადაეცემა სამი არგუმენტი range(start, end, step).
#როცა ჩვენ range ფუნქციას გადავცემთ ერთ არგუმენტს, იგი defaultad მას იყენებს როგორც end არგუმენტს.

for i in range(150, 321):
    print(i)

#start - ათვლის დასაწყისი, end - ათვლის დასასრული, 
#step - ყოველი step-ისთვის გადაცემული რიცხვის გამეორება პირველი ორი არგუმენტის მიერ მიღებულ დიაპაზონში.

for i in range(5, 20, 10):
    print(i)

    #ჩვენ ამით range ფუნქციას ვეუბნებით, რომ დაგვიბეჭდოს ყოველი მეათე რიცხვი 5 იდან 20 მდე.


#საკლასო დავალება: თქვენი დავალება იქნება 30 დან 120 ის ჩათვლით დამიპრინტეთ ყოველი მეათე რიცხვი და გამირკვიეთ იყოფა, თუ არა 2-ზე.

for i in range(30, 121, 10):
    if i % 2 == 0:
        print(i)

        #მაგრამ 10-ი 2-ზე აუცილებლად იყოფა, ვერ შემაცდენთ :დ

#ჩვენ შეგვიძლია loop-ი კიდევ loop-ში მოვაქციოთ, რასაც ასეთი შედეგი მოჰყვება:
for i in range(50):
    print("Hello", i)
    for a in range(50):
        print("Hello World", a)

#ამ კოდის შედეგი არის ის, რომ ყოველი პირველი ფუნქციის გამეორების შემდეგ, მეორე ფუნქცია მეორდება სრულად. 
#როცა პირველი range ფუნქციის Hello დაიპრინტება ერთხელ, მეორე ფუნქციის Hello World დაიპრინტება 50-ჯერ, პირველი range ფუნქციის მეორედ დაპრინტვისას იგივე განმეორდება. კოდი პირველი ფუნქციის დასრულების შემდეგ დასრულდება.
#მარტივად, რომ ვთქვათ კომპიუტერს ვუბრძანეთ, რომ 50-ჯერ მოცემული Hello World დაგვიპრინტოს 50-ჯერ, ანუ ჯამში 2500-ჯერ.
