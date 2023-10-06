# << IF >>
# 36 -->
list = []
for i in range(3):
    list.append(int(input()))
print(max(list))

# 37 -->
list = []
for i in range(3):
    list.append(int(input()))
list.sort(reverse=True)
for i in range(3):
    print(list[i])

# 38 -->
number = int(input())
if number >= 1 and number <= 7:
    print(1)
elif number > 7 and number <= 14:
    print(2)
elif number > 14 and number <= 21:
    print(3)
elif number > 21 and number <= 28:
    print(4)
elif number > 28 and number <= 30 or number > 28 and number <= 31:
    print(5)
else:
    print("ERORR")

# 39 -->
number = int(input())
number = str(number)
number = number.replace("0", "")
print(int(number))

# 40 -->
number = int(input(), 2)
number2 = int(input(), 2)
Sum = number + number2
print(bin(Sum)[2:])

# << FOR >>
# 66 --> 
list = []
list2 = []
for i in range(100):
    list.append(int(input()))

for i in range(len(list)):
    number = list[i]
    number0 = 0
    number1 = 1
    while number1 < number:
        fib = number0 + number1
        number0 = number1
        number1 = fib
    if number1 == number:
        list2.append(number)

for i in range(len(list2)):
    print(list2[i])

# 67 -->
number = int(input())
list = []
number0 = 0
number1 = 1
while number1 < number:
        fib = number0 + number1
        number0 = number1
        number1 = fib
        if number % number1 == 0:
            list.append(number1)
for i in range(len(list)):
    print(list[i])

# 68 -->
number = int(input())
count = 0
while number > 0:
    if number % 10 == 0:
        count += 1
    number //= 10
print(count)

# 69 -->
number = int(input())
number = str(number)
number = number.replace("0", "")
print(int(number))

# 70 -->
number_min = 56
number_max = 1984
for i in range(number_min, number_max+1):
    number = i
    number2 = 1
    print(f"{i} ->")
    while number2 <= number:
        if number % number2 == 0:
            print(number2)
        number2 += 1

# << ARRAY >>
# 86 -->
list = []
number = int(input())
for i in range(number):
    list.append(int(input()))
print(max(list))

# 87 -->
list = []
number = int(input())
for i in range(number):
    list.append(int(input()))
list.sort(reverse=True)
for i in range(number):
    print(list[i])

# 88 -->
list = []
number = int(input())
for i in range(number):
    list.append(int(input()))
if list == sorted(list):
    print("yes")
else:
    print("no")

# 89 -->
list = []
for i in range(10):
    list.append(int(input()))
list.pop(0)
for i in range(len(list)):
    print(list[i])

# 90 -->
list = []
number = int(input())
for i in range(number):
    list.append(int(input()))
for i in range(number):
    f = 1
    fa = 1
    while f <= list[i]:
        fa *= f
        f += 1
    print(f"{list[i]} = {fa}")

# << FUNCTION >>
# 106 -->
def CountEvenNUmber(list):
    count = 0
    for i in range(5):
        if list[i] % 2 == 0:
            count += 1
    return count
list = []
for i in range(5):
    list.append(int(input()))
print(CountEvenNUmber(list))

# 107 -->
list = []
for i in range(5):
    list.append(int(input()))
av = 0
for i in range(5):
    av += list[i]
av //= 5
for i in range(5):
    if list[i] == av+3 or list[i] == av-3:
        print(list[i])

# 108 -->
def CountA(number):
    list = []
    countA = 0
    for i in range(number):
        list.append(int(input()))
    for i in range(number):
        l = 1
        count = 0
        while l <= list[i]:
            if list[i] % l == 0:
                count += 1
            l += 1
        if count == 2:
            countA += 1
    return(countA)
print(CountA(int(input())))
    
# 109 -->
def FA(number):
    list = []
    for i in range(number):
        list.append(int(input()))
    for i in range(number):
        f = 1
        fa = 1
        while f <= list[i]:
            fa *= f
            f += 1
        print(f"{list[i]} = {fa}")
FA(int(input()))

# 110 -->
def MaxMin(number):
    list = []
    for i in range(number):
        list.append(int(input()))
    list.sort(reverse=True)
    for i in range(number):
        print(list[i])
MaxMin(int(input()))


# << STRING >>
# 117 -->
string = input()
string = string.capitalize()
print(string)

# 118 -->
import re
strring  = input()
print(re.findall(r'\d+', strring))

# 119 -->
string = input()
string = string.replace("a", "")
print(string)

# 120 -->
string = input()
string = string.replace(" ", "")
print(string)

# 121 -->
string = input()
string1 = input()
number = int(string) + int(string1)
print(str(number))
    