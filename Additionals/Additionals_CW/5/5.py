#Codewars solutions! 

# 1)

def sum_array(a):
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]
    return sum

# 2)

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0:
        return True
    else:
        return False

# 3)

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return m * n