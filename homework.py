
#module 1
user = (input('What is your name?'))
user2 = (input('What is your sername?'))
if user == 'Viivi' and user2 == 'Virta':
    print('Hello, ', user, ' ', user2, '!', sep='')
else:
    print("I don't know who you are.")

#module 2
#number 1
user = input('What is your name?')
print('Hello ', user, '!', sep='')

# number 2
r = float(input('write the radius of a circle'))
s = 3.14 * r ** 2
print(s)

#number 3
d = float(input('Write a lenght of a rectangle'))
l = float(input('Write a width of a rectangle'))
s = d * l
p = d + d + l + l
print('Perimetr:', p)
print('Area', s)

#number 4
n1 = int(input('Wrire a number'))
n2 = int(input('One more'))
n3 = int(input('One more'))
print('Summ:', n1 + n2 + n3)
print('Product', n1 * n2 * n3)
print('Average', (n1 + n2 + n3) / 3)

#number 5
a = float(input('Write a mass in a talents'))
b = float(input('Write a mass in a pounds'))
c = float(input('Write a mass in a lots'))
a1 = (a * 20 * 32 * 13.3) / 1000
b2 = (b * 32 * 13.3) / 1000
c2 = (c * 13.3)/1000
x = int(a1 + b2 + c2)
v = ((a1 + b2 + c2) - x) * 1000
v = str(v)
v = v[:6]
print(x, 'killograms and', v, 'grams.')

#module 3
#number 1
l = int(input('How long is zander (in cm)'))
if l >= 42:
    print("It's good")
else:
    b = 42 - l
    print('Catch ', b,' centimeters more fish to collect. This fish needs to be released.')
#number 2
c = input('Enter the cabin class of a cruise ship')
if c == 'LUX':
    print('Upper-deck cabin with a balcony')
elif c == 'A':
    print('Above the car deck, equipped with a window')
elif c == 'B':
    print('Windowless cabin above the car deck')
elif c == 'C':
    print('Windowless cabin below the car deck')
else:
    print('Invalid cabin class')

#number 3
b = (input('What is your biological gender. Male or Female?'))
if b == 'Male' or b == 'Female':
    c = int(input('What is yoyur hemoglobin value (g/l)'))
    if b == 'Male':
        if 117 <= c <= 155:
            print('Good')
        else:
            if c > 155:
                print('Your level of hemoglobin is hight')
            elif c < 117:
                print('Your level of hemoglobin is low')
    else:
        if b == 'Female':
            if 134 <= c <= 167:
                print('Good')
            else:
                if c > 167:
                    print('Your level of hemoglobin is hight')
                elif c < 134:
                    print('Your level of hemoglobin is low')
else:
    print('Write gender correctly.')

#number 4
year = int(input('Write a year'))
if year % 4 == 0 or year % 400 == 0:
    print('Leap year', year)
else:
    print('Not leap year', year)










'''
#module 4
#number 1
v = 1
while v <= 1000:
    if v % 3 == 0:
        print(v)
        v += 1
    else:
        v += 1

#number 2
c = 1
while c >= 0:
    c = int(input('Write amount of inches'))
    if c >= 0:
        b = c * 2.54
        print(b, 'Centimetrs')
    else:
        print('Incorrect value')

#number 3
a = int(input('Write a number'))
b = 0
while a = 1:
print('Max: ',max(a, b))
print('Min: ',min(a, b))
'''