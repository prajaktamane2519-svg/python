text="pytthon"
r=text[::-1]
print(text)
text="python"
count=0
for i in text.lower():
    if i in "aeiou":
        count+=1
print(count)
text="python"
print(text.upper())
print(text.lower())
print(text.count("o"))
text="madam"
if text==text[::-1]:
    print("palidrome")
else:
    print("not palidrome")
number=[10,20,30,40]
print(number)
number=[1,2,5,7]
number.append(8)
print(number)
number.remove(7)
print(number)
a=int(input("enter the numbe:"))
b=int(input("enter the numbe :"))
sum=a+b
print(sum)