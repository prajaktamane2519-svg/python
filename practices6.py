a=int(input("enter the number: "))
b=int(input("enter the number: "))
print(a+b)
print(a-b)
print(a*b)
print("queotient",a//b)
print("remainder",a%b)
num=234
print(num%2==0)
age=20
if age>=18 and age <=60:
    print("valid")
else:
    print("invalid")
num=30
if num%3==0 and num%5==0:
    print("divisible")
else:
    print("not divisible")
num=10
if num>0:
    print("positive")
else:
    print("negative")
num=7
if num%2==0:
    print("even")
else:
    print("odd")
age=20
if age>=18:
    print("votes eligible")
else:
    print("votes not eligible")
a=25
b=40
c=67
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
marks=78
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>60:
    print("c")
else:
    print("Fail")