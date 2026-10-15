print("HEllo world")
a=10
b=6
sum=a+b
print(sum)
a=67
b=8
r=a%b
print(r)
a="150"
b=int(a)
print(b)
print(type(b))
a=30
b=20
a,b=b,a
print(a)
print(b)
c=10.67
print(type(c))
num=24
if num%2==0:
    print("even")
else:
    print("odd")
num=89
if num>0:
    print("positive number")
else:
    print("negative numbetr")
year=2016
if year%4==0:
    print("leaf year")
else:
    print("not leaf year")
for i in range(1,11):
    print(i)
for i in range(2,22,2):
    print(i)
total=0
for i in range(1,11):
    total+=i
print(total)
text="python"
print(text[::-1])  
text="madam"
if text[::-1]==text:
    print("palidrome")
else:
    print("not palidrome")
text="equcation"
count=0
for ch in text:
    if ch in "aeiou":
        count+=1
print(count)
tex="python"
print(len(tex))
print(tex.upper())
print(tex.lower())
print(tex.title())
print(tex.count("a"))
n=3
print(n**3)
print(type(n))
str=float(n)
print(str)
x="150"
y=int(x)
print(type(y))
age=16
if 13<=age<=19:
    print("Teenager")
else:
    print("not teenager")
a=10
b=20
c=30
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
year=2023
if year%4==0:
    print("leaf year")
else:
    print("not leaf year")
ch="a"
if ch.lower() in "aeiou":
    print("vowel")
else:
    print("not vowel")
price=800
if price>=1000:
    discount=price*0.10
else:
    discount=0
print(discount)
marks=89
income=13000
if marks>85 and income>20000:
    print("Eligible")
else:
    print("not eligible")
ch="A"
if ch.isupper():
    print("uppercSE")
else:
    print("noy uppercase")

n=75
if 50<=n<=100:
    print("range")
else:
    print("not range")
units=150
if units<=100:
    bill=units*5
else:
    bill=100*5+(units-100)*8
print(

