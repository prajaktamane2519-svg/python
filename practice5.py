name="praj"
city="Pune"
print(name)
print(city)
a=int(input("enter the numberr :"))
b=int(input("enter the numberr :"))
print("sum :",a+b)
a=10
b=10.5
a,b=b,a
print(a)
print(b)
num=70
print(num>50)
num=12
if num%2==0:
    print("even number")
else:
    print("odd number")
marks=int(input("enter the marks :"))
if marks>35:
    print("pass")
else:
    print("fail")
marks=76
if marks>=90:
    print("A grade")
elif marks >=70:
    print("B grade")
elif marks>50:
    print("c grade")
else:
    print("D grade")
for i in range(1,11):
    print(i)
num=6
for i in range(1,11):
    print(num*i)
i=1
while i<=5:
    print(i)
    i+=1
i=2
while i<=10:
    print(i)
    i+=2
for i in range(1,11):
    if i==5:
        break
    print(i)
for i in range(1,100):
    if i%5==0:
        break
    print(i)
for i in range(1,11):
    if i==5:
        continue
    print(i) 
for i in range(1,50):
    if i%2==0:
        continue
    print(i)
text="python"
print(text[::-1])