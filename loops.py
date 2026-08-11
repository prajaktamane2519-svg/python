for i in range(1,11):
    print(i)
for i in range(10,0,-1):
        print(i)
for i in range(1,40,2):
    print(i)
for i in range(2,51,2):
    print(i)
for i in range(1,11):
    print(5*i)
a=int(input("enter the number : "))
for i in range(1,11):
    print(a*i)
for i in range(1,11):
    print(i**2)
for i in range(1,11):
    print(i**3)
for i in range(11):
    print("Hello")
for i in range(1, 100):
    if i%5==0:
        print(i)  
for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i)
total=0
for i in range(1,11):
    total+=i
print(total)
for i in range(2,101,2):
    total+=i
print(total)

count=0
for i in range(1,101):
    if i%7==0:
        count+=1
print(count)
for i in range(1,10):
    if i%2==0:
        print(i,"even number")
    else:
        print(i,"odd number")
number=[10,23,5,78]  
largest=number[0]
for i in number:
    if i>largest:
        largest=i
    print(largest)   
i=1
while i<=10:
    print(i)
    i+=1
i =10
while i>=1:
    print(i)
    i-=1
i=2
while i<=50:
    print(i)
    i+=2
i=1
while i<=50:
    print(i)
    i+=2
