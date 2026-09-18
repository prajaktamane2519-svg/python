name="pt"
age=45
print(name)
print(age)
print(type(age))
x="100"
print(int(x))
a=int(input("enter the number:"))
b=int(input("enter the number:"))
print("sum=",a+b)
a=56
b=5
sum=a+b
print(sum)
print(a%b)
n=3
print(n**2)
a=6
b=8
print(a==b)
n=78
if n>0:
    print("positive")
else:
    print("negtive")
n=12
if n%2==0:
    print("even number")
else:
    print("odd number")
a=25
b=56
if a>b:
    print("a is greather")
else:
    print("a is smallest")
marks=79
if marks>90:
    print("grade A")
elif marks >70:
    print("grade B")
elif marks>60:
    print("grade c")
else:
    print("grade D")
for i in range(1,11):
    print(i)
for i in range(1,20):
    if i%2==0:
        print(i)
for i in range(1,20,2):
    print(i)
total=0
for i in range(1,11):
    total=total+i
print(total)
n=5
for i in range(1,11):
    print(n,"*",i,"=",n*i)

s="i love python"
print(len(s))
print(s.upper())
print(s.lower())
print(s[::-1])
print(s.count("a"))
s="madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
a=["apple","bannna","guva"]
print(a)
a.append("grapes")
print(a)
a.remove("bannna")
print(a)
number=[10,20,40,50,60]
print(max(number))
print(min(number))

number=(10,39,29)
print(number)
print(number[0])
print(len(number))


number={10,10,20,30,30,40}
print(number)
number.add(69)
print(number)
a={1,3,5,7,8}
b={4,6,7,8,0}
print(a.intersection(b))
print(a.union(b))
student={"name":"pr",
"age":5}
print(student["name"])
student["city"]="pune"
print(student)
x=10
print(x)
x="python"
print(x)
x=29.5
print(type(x))
name="as"
print(type(name))
age=4
price=10.4
name="pt"
print(age,price,name)
a=10
b=3
print(a%b)
num=10
if num>0:
    print("positive")
else:
    print("negative")
for i in range(1,6):
    print(i)
for i in range(1,11):
    print(i)
for i in range(2,21,2):
    print(i)
for i in range(1,21,2):
    print(i)
for i in range(10,1,-1):
    print(i)
for  i in range(1,11):
    print(5*i)
total=0
for i in range(1,11):
    total=total+i
print(total)
fruit=["apple","Banana","grapes"]
for fruit in fruit:
    print(fruit)

