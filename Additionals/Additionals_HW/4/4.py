#codewars!

# 1)

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "/":
        return value1 / value2
    else: 
        return value1 * value2

# 2)

def count_sheeps(sheep):
    sum = 0
    count = []
    for i in range(len(sheep)):
        if sheep[i] == True:
            count.append(sheep)
    return len(count)

# 3)

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# 4)

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return False
    else:
        return True
    
# 5)

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9



