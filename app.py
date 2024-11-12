def prime_number(num):
    n = 0
    count = 0
    for i in range(2,num):
        n = 0
        for j in range(2,i):
            if i % j == 0:
                n+=1
        if n == 0:
            count+=1
            # print(i)
    print('number of PN is:', count)
# prime_number(777)
def min_to_sec(min):
    return min * 60
min_to_sec(int(input("Please enter a number: ")))
def addition(num):
    if num < 10:
        result = num + addition(num + 1)
        print(result)
    else:
        result = 0
    return result

# addition(int(input("Please enter a number: ")))
