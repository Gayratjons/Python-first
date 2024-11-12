def age_in_days():
    age = int(input("Please enter an age: "))
    days = 0
    for i in range(age):
        days += 365
    return days


def reminder(*a):
    return a[0] % a[1]


def calculate_points(wins, draws, loses):
    return wins * 5 + draws * 2 + loses


def count_legs(chickens, cows, lambs):
    return chickens * 2 + cows * 4 + lambs * 4


print("Input: 2 => Output:", age_in_days())  # Expected: 730
print("Input: (10, 3) => Output:", reminder(10, 3))  # Expected: 1
print("Input: (3, 2, 1) => Output:", calculate_points(3, 2, 1))  # Expected: 23
print("Input: (3, 2, 1) => Output:", count_legs(3, 2, 1))  # Expected: 20

def cels_to_kelv():
    float(input("Input the celsius"))
    return celcius + 273
print(cels_to_faren(30.7))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def max_from_list(a):
    max = 0
    for i in a:
        if i > max:
            max = i
    return max
print(max_from_list([12,8778, 9999, 0, 10000]))

def fibonaci(n):
    first = 1
    second = 1
    for i in n:
        sumw = first + second
        first = second 
        second = sumw
    return sumw

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
result = count_vowels("Hello World")
print(result)

