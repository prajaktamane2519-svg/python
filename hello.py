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