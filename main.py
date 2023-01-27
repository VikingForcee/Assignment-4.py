import random

marks = int(input('Enter Marks :'))
if 0 < marks < 100:
    if marks < 25:
        print('Grade : F')
    if 24 < marks < 45:
        print('Grade : E')
    if 44 < marks < 50:
        print('Grade : D')
    if 49 < marks < 60:
        print('Grade : C')
    if 59 < marks < 80:
        print('Grade : B')
    if marks > 79:
        print('Grade : A')
else:
    print("Enter valid marks")

print()
print()

year = int(input('Enter year :'))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(year, ':Not a Leap Year')
    else:
        print(year, ':Leap Year')
else:
    print(year, ':Not a Leap Year')


print()
print()
marks = 0
ques = 0

for ques in range(1, 11):
    d = random.randint(1, 10)
    e = random.randint(1, 10)

    q1 = int(input(f'Question {ques} : {d} * {e} = '))

    if q1 == (d * e):
        print('Right')
        marks = marks + 1
    else:
        print(f'Wrong the answer is {d * e}')
print(f"Your marks are {marks}")

print()
print()

print("Q4")
for candies in range(200):
    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:
                print("total pieces of candy in the bowl is", candies)
