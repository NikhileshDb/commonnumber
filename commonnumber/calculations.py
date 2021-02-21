from datetime import datetime


x = int(input("Please type first round result: "))
y = int(input("Please type second round result: "))
day1 = int(input("Select Date: "))
month1 = int(input("Select Month: "))

day = int(datetime.now().strftime('%d'))
month = int(datetime.now().strftime('%M'))
year = int(datetime.now().strftime('%Y'))

def firstDigit(x):
    # Remove last digit from number
    # till only one digit is left
    while x >= 10:
        x = x / 10;
        return int(x)

def firstDigityear(x):
    while x >= 10:
        x = x //1000
        return int(x)

#The input Must be four digit

def secondDigit(x):
    while x >= 10:
        x = x//100;
        return lastDigit(int(x))

#The input Must be four digit
def thirdDigit(x):
        return firstDigit(x % 100)

def lastDigit(x):
    return (x % 10)

# Calculation Start
user_1_first = int(0 if firstDigit(x) is None else firstDigit(x))
user_1_second = int(0 if lastDigit(x) is None else lastDigit(x))
user_2_first = int(0 if firstDigit(y) is None else firstDigit(y))
user_2_second = int(0 if lastDigit(y) is None else lastDigit(y))
today_first = int(0 if firstDigit(day1) is None else firstDigit(day1))
today_second = int(0 if lastDigit(day1) is None else lastDigit(day1))
month_first = int(0 if firstDigit(month1) is None else firstDigit(month1))
month_second = int(0 if lastDigit(month1) is None else lastDigit(month1))
first_year = int(0 if firstDigityear(year) is None else firstDigityear(year))
second_year = int(0 if secondDigit(year) is None else secondDigit(year))
third_year = int(0 if thirdDigit(year) is None else thirdDigit(year))
fourth_year = int(0 if lastDigit(year) is None else lastDigit(year))

a = fourth_year + third_year
#print(lastDigit(a))
b = third_year + second_year + int(0 if firstDigit(a) is None else firstDigit(a))
#print(lastDigit(b))
c = second_year + first_year + int(0 if firstDigit(b) is None else firstDigit(b))
#print(lastDigit(c))
d = first_year + month_second + int(0 if firstDigit(c) is None else firstDigit(c))
#print(lastDigit(d))
e = month_second + month_first + int(0 if firstDigit(d) is None else firstDigit(d))
#print(lastDigit(e))
f = month_first + today_second + int(0 if firstDigit(e) is None else firstDigit(e))
#print(lastDigit(f))
g = today_second + today_first + int(0 if firstDigit(f) is None else firstDigit(f))
#print(lastDigit(g))
h = today_first + user_2_second + int(0 if firstDigit(g) is None else firstDigit(g))
#print(lastDigit(h))
i = user_2_second + user_2_first + int(0 if firstDigit(h) is None else firstDigit(h))
#print(lastDigit(i))
j = user_2_first + user_1_second + int(0 if firstDigit(i) is None else firstDigit(i))
#print(lastDigit(j))
k = user_1_second + user_1_first + int(0 if firstDigit(j) is None else firstDigit(j))
#print(lastDigit(k))

l = lastDigit(a) + lastDigit(b)
#print(lastDigit(l))
m = lastDigit(b) + lastDigit(c) + int(0 if firstDigit(l) is None else firstDigit(l))
#print(lastDigit(m))
n = lastDigit(c) + lastDigit(d) + int(0 if firstDigit(m) is None else firstDigit(m))
#print(lastDigit(n))
o = lastDigit(d) + lastDigit(e) + int(0 if firstDigit(n) is None else firstDigit(n))
#print(lastDigit(o))
p = lastDigit(e) + lastDigit(f) + int(0 if firstDigit(o) is None else firstDigit(o))
#print(lastDigit(p))
q = lastDigit(f) + lastDigit(g) + int(0 if firstDigit(p) is None else firstDigit(p))
#print(lastDigit(q))
r = lastDigit(g) + lastDigit(h) + int(0 if firstDigit(q) is None else firstDigit(q))
#print(lastDigit(r))
s = lastDigit(h) + lastDigit(i) + int(0 if firstDigit(r) is None else firstDigit(r))
#print(lastDigit(s))
t = lastDigit(i) + lastDigit(j) + int(0 if firstDigit(s) is None else firstDigit(s))
#print((lastDigit(t)))
u = lastDigit(j) + lastDigit(k) + int(0 if firstDigit(t) is None else firstDigit(t))
#print(lastDigit(u))

#Adding Last Digit With Last Digit
def addingLast(x,y):
    x = lastDigit(x) + lastDigit(y)
    return int(x)

a1 = addingLast(l,m)
a2 = addingLast(m,n) + int(0 if firstDigit(a1) is None else firstDigit(a1))
a3 = addingLast(n,o) + int(0 if firstDigit(a2) is None else firstDigit(a2))
a4 = addingLast(o,p) + int(0 if firstDigit(a3) is None else firstDigit(a3))
a5 = addingLast(p,q) + int(0 if firstDigit(a4) is None else firstDigit(a4))
a6 = addingLast(q,r) + int(0 if firstDigit(a5) is None else firstDigit(a5))
a7 = addingLast(r,s) + int(0 if firstDigit(a6) is None else firstDigit(a6))
a8 = addingLast(s,t) + int(0 if firstDigit(a7) is None else firstDigit(a7))
a9 = addingLast(t,u) + int(0 if firstDigit(a8) is None else firstDigit(a8))

b1 = addingLast(a1,a2)
b2 = addingLast(a2,a3) + int(0 if firstDigit(b1) is None else firstDigit(b1))
b3 = addingLast(a3,a4) + int(0 if firstDigit(b2) is None else firstDigit(b2))
b4 = addingLast(a4,a5) + int(0 if firstDigit(b3) is None else firstDigit(b3))
b5 = addingLast(a5,a6) + int(0 if firstDigit(b4) is None else firstDigit(b4))
b6 = addingLast(a6,a7) + int(0 if firstDigit(b5) is None else firstDigit(b5))
b7 = addingLast(a7,a8) + int(0 if firstDigit(b6) is None else firstDigit(b6))
b8 = addingLast(a8,a9) + int(0 if firstDigit(b7) is None else firstDigit(b7))

c1 = addingLast(b1,b2)
c2 = addingLast(b2,b3) + int(0 if firstDigit(c1) is None else firstDigit(c1))
c3 = addingLast(b3,b4) + int(0 if firstDigit(c2) is None else firstDigit(c2))
c4 = addingLast(b4,b5) + int(0 if firstDigit(c3) is None else firstDigit(c3))
c5 = addingLast(b5,b6) + int(0 if firstDigit(c4) is None else firstDigit(c4))
c6 = addingLast(b6,b7) + int(0 if firstDigit(c5) is None else firstDigit(c5))
c7 = addingLast(b7,b8) + int(0 if firstDigit(c6) is None else firstDigit(c6))

d1 = addingLast(c1,c2)
d2 = addingLast(c2,c3) + int(0 if firstDigit(d1) is None else firstDigit(d1))
d3 = addingLast(c3,c4) + int(0 if firstDigit(d2) is None else firstDigit(d2))
d4 = addingLast(c4,c5) + int(0 if firstDigit(d3) is None else firstDigit(d3))
d5 = addingLast(c5,c6) + int(0 if firstDigit(d4) is None else firstDigit(d4))
d6 = addingLast(c6,c7) + int(0 if firstDigit(d5) is None else firstDigit(d5))

e1 = addingLast(d1,d2)
e2 = addingLast(d2,d3) + int(0 if firstDigit(e1) is None else firstDigit(e1))
e3 = addingLast(d3,d4) + int(0 if firstDigit(e2) is None else firstDigit(e2))
e4 = addingLast(d4,d5) + int(0 if firstDigit(e3) is None else firstDigit(e3))
e5 = addingLast(d5,d6) + int(0 if firstDigit(e4) is None else firstDigit(e4))

f1 = addingLast(e1,e2)
f2 = addingLast(e2,e3) + int(0 if firstDigit(f1) is None else firstDigit(f1))
f3 = addingLast(e3,e4) + int(0 if firstDigit(f2) is None else firstDigit(f2))
f4 = addingLast(e4,e5) + int(0 if firstDigit(f3) is None else firstDigit(f3))


print(user_1_first, user_1_second, user_2_first, user_2_second, today_first, today_second, month_first, month_second, first_year, second_year, third_year, fourth_year)
print(lastDigit(k), lastDigit(j),lastDigit(i),lastDigit(h),lastDigit(g),lastDigit(f),lastDigit(e),lastDigit(d),lastDigit(c),lastDigit(b),lastDigit(a) )
print(lastDigit(u), lastDigit(t), lastDigit(s), lastDigit(r), lastDigit(q), lastDigit(p), lastDigit(o),lastDigit(n), lastDigit(m),lastDigit(l))
print(lastDigit(a9),lastDigit(a8), lastDigit(a7), lastDigit(a6), lastDigit(a5), lastDigit(a4),lastDigit(a3), lastDigit(a2), lastDigit(a1))
print(lastDigit(b8), lastDigit(b7), lastDigit(b6), lastDigit(b5), lastDigit(b4),lastDigit(b3), lastDigit(b2), lastDigit(b1))
print(lastDigit(c7), lastDigit(c6), lastDigit(c5), lastDigit(c4),lastDigit(c3), lastDigit(c2), lastDigit(c1))
print(lastDigit(d6), lastDigit(d5), lastDigit(d4),lastDigit(d3), lastDigit(d2), lastDigit(d1))
print(lastDigit(e5), lastDigit(e4),lastDigit(e3), lastDigit(e2), lastDigit(e1))
print(lastDigit(f4),lastDigit(f3), lastDigit(f2), lastDigit(f1))