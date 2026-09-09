name="pt"
age=56
city='karad'
print(name)
print(city)
print(age)
x=78
print(type(x))
a=28
b=67
a,b=b,a
print(a)
print(b)
s="100"
y=int(s)
print(s)
print(type(s))
length=30
width=10
area=length*width
print(area)
a=10
b=20
sum=a+b
print(sum)
r=a%b
print(r)
num=24
if num%2==0:
    print("even")
else:
    print("odd")
a=10
b=20
if a>b:
    print("largest")
else:
    print("smallest")
a=100
r=5
t=2
si=(a*r*t)/100
print(si)
a=int(input("enter the number"))
if a>0:
    print("positive")
else:
    print("negative")
a=int(input("enter the number"))
if a%2==0:
    print("even")
else:
    print("odd")
marks=78
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=60:
    print("c")
else:
    print("D")
for i in range(1,11):
    print(i)
num=5
for i in range(1,11):
    print(num*i)
total=0
for i in range(1,101):
  total=total+i
print(total)
for i in range(1,51):
    if i%2==0:
     print(i)
text="python"
print(text[::-1])
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(len(text))
text="madam"
if text==text[::-1]:
    print("palidrram")
else:
    print("non palidram")
text="i love python"
count=0
for i in text:
    if i in"aeiou":
        count+=1
print(count)