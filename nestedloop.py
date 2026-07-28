for i in range(1,11):
    print(i)
for i in range(10,0,-1):
   print(i)
for i in range(2,21,2):
    print(i)
for i in range(1,20,2):
    print(i)
    total=0
for i in range(1,11):
    total+=i
print("sum =",total)
number=5
for i in range(1,11):
   print(number,"X",i,"=",number*i)
name="shaarvi"
for ch in name:
    print(ch)
    number=[10,20,56,89]
for num in number:
    print(num)
for num in range(1,101):
    if num%5==0:
        print(num)
for num in range(1,11):
    print(num,"square =",num*num)
    num=5
    fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial =",fact)
text=input("Enter a string: ")
count=0
for ch in text.lower():
   
    if ch in "aeiou":
        count +=1
print("vowels =",count)
numbers=[10,25,8,45,30]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print("laergest=",largest)
numbers=[10,5,46,78,98]
smallest=numbers[0]
for num in numbers:
    if num< smallest:
        smallest=num
        print("smallest=",smallest)
for num in range(2,101):
    for i in range(2,num):
         if num%i==0:
            break
    else:
           print(num)
     
for i in range(1,6):
    print("*"* i)
number=[10,20,30,40,0,60,70]
total=0
for num in number:
    total+=num
print("sum=",total)
for i in range(1,51):
    if i%3==0 and i%6
