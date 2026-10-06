n=10
if n%2==0:
    print("even")
else:
    print("odd")
n=int(input("enter the number:"))
if n>0:
    print("positive number")
else:
    print("negative number")
a,b,c=10,25,56
if a>=b and a>=c:
    print(a)
elif b>=c:
    print(b)
else:
    print(c)
if a>b and a>c:
    print(a)
elif b>=c:
    print(b)
else:
    print(c)
num=18
if num>0:
    print("positive")
else:
    print("negative")
num=int(input("enter the number: "))  
if num%2==0:
    print("Even")
else:
    print("odd")
num=20
if num%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")
username="abc"
password="12346"
if username=="abc" and password=="12346":
    print("login successful")
else:
    print("Invalid login")
n=24
if n%2==0 and n%3==0:
    print("divible both")
else:
    print("not divisible")
n=30
if n%5==0 and n%6==0:
    print("divible both")
else:
    print("divible not")
n=56
if n>=10 and n<=50:
    print("between 10 and 28")
else:
    print("not between")
a=20
b=10
c=15
if a>b and a>c:
    print("a is largest")
elif b>c:
    print("b is largest")
else:
    print("c is largest")
name="sharvi"
if name in "aeiou":
    print("Vowel")
else:
    print("consonant")
num=20
if num%2==0:
    print("even number")
else:
    print("odd number")
num=29
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("Zero number")
for i in range(1,10):
    print(i)
total=0
for i in range(1,100):
    total+=i
print(total)
text="python"
print(text[::-1])
print(len(text))
print(text.upper())
print(text.lower())
print(text[1])
print(text[-1])
print(text[1:6])
print(text.count("a"))
print(text.find("o"))
print(text.replace("p","i"))
print(text.isalpha())
text="python"
count=0
for ch in text:
    count+=1
print(count)