
#module 5
#number 1
import random
b = 0
x = int(input('How many dice to roll?'))
for i in range(x):
    c = random.randint(1, 6)
    b += c
print(b)

#number 2
numbers = []
while True:
    a = input('Write a number: ')
    if a == '' or a == ' ':
        break
    a = int(a)
    numbers.append(a)
    if len(numbers) > 5:
        numbers = numbers[-5:]
numbers.sort(reverse=True)
print(numbers)

#number 3
a = int(input('Write a number'))
if a % a == 0 and a > 1 and a % 2 != 0:
    print('Number', a, 'is a prime number')
else:
    print('Number', a, 'is not a prime number')

#number 4
words = []
for i in range(5):
    word = input('Write a City')
    words.append(word)
print("You print this words:")
for word in words:
    print(word)


#module 6
#number 1
import random
def throws_until_six():
    throws = 0
    while True:
        throws += 1
        a = random.randint(1, 6)
        print('Now number is:', a)
        if a == 6:
            break
    return throws
throws_needed = throws_until_six()
print('It took', throws_needed, 'throws to get a 6.')


#number 2
import random

def throws_until_six():
    throws = 0
    n = int(input('How many sided dice do you want to roll?'))
    while True:
        throws += 1
        a = random.randint(1, n)
        print('Now number is:', a)
        if a == n:
            break
    return throws

throws_needed = throws_until_six()
print('It took', throws_needed, 'throws to get a 6.')

#number 3
def gallons_to_liters(gallons):
    if gallons < 0:
        return None
    liters = gallons * 3.785
    return liters

while True:
    a = float(input('What is the amount of gasoline in gallons? (or negative value for result): '))
    if a < 0:
        break
    b = gallons_to_liters(a)
    if b is not None:
        print(f'Liters in {a} gallons: {b}')
    else:
        print('Negative value entered, program terminated.')

#number 4
numbers = []
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
a = 1
while a != 0:
    if __name__ == "__main__":
        a = int(input('Write a number. For exit write 0'))
        numbers.append(a)
        result = calculate_sum(numbers)
print("Sum of numbers in a list:", result)


#number 5
mylist = []
mylist2 = []
h = 0
n = int(input('How many numbers will be in the list: '))
while h != n:
    a = int(input('Write a number: '))
    mylist.append(a)
    h += 1
mylist_copy = mylist

while len(mylist_copy) != 0:
    b = mylist_copy[0]
    if b % 2 == 0:
        mylist2.append(b)
    mylist_copy = mylist_copy[1:]
print('Original list', mylist)
print('Abbreviated list', mylist2)



#number 6

d = int(input('Write a diametr of pizza'))
cost = int(input('Write a cost of pizza'))
metr = 3.14 * d ** 2 / 4
calc1 = metr / cost

d2 = int(input('Write a diametr of second pizza'))
cost2 = int(input('Write a cost of second pizza'))
metr2 = 3.14 * d2 ** 2 / 4
calc2 = metr2 / cost2

if calc1 > calc2:
    print('Second pizza better')
else:
    print('First pizza better')

#module 7
#number 1
month = int(input('What month is it?'))
if month == 12 or month == 1 or month == 2:
    print(month, 'the month is winter')
elif month == 3 or month == 4 or month == 5:
    print(month, 'the month is spring')
elif month == 6 or month == 7 or month == 8:
    print(month, 'the month is summer')
elif month == 9 or month == 10 or month == 11:
    print(month, 'the month is autumn')
else:
    print('Enter the month correctly')

#number 2
names = []
while True:
    name = input('Write a name')
    if name in names:
        print('Existing name')
    else:
        print('New name')
    names.append(name)
    if name == '':
        print('Names list:')
        for name in names:
            print(name)
        if name == '':
            break

#number 3
import csv

airports = {}

while True:
    print("Select an option:")
    print("1. Introduce a new airport")
    print("2. Get information about an existing airport")
    print("3. Exit")
    a = int(input())

    if a == 1:
        icao = input('Write IKAO')
        airport = input('Write airport name')
        with open('icaonames.csv', 'r', encoding='utf-8') as file:
            icaocheck = csv.reader(file, delimiter=',')
            if any(icao in line for line in icaocheck):
                print('This ICAO code already exists')
            else:
                with open('icaonames.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([icao, airport])
                    print(f"Airport name with ikao code {icao}: {airport} added.")

    elif a == 2:
        with open('icaonames.csv', 'r', encoding='utf-8') as file:
            lines = csv.reader(file, delimiter=',')
            for line in lines:
                icao_code, airport_name = line[0], line[1]
                airports[icao_code] = airport_name
            n = input('Write ICAO')
            if n in airports:
                airport_name = airports[n]
                print(f"Airport name with ikao_code {n}: {airport_name}")

    elif a == 3:
        print('You are quit')
        break