number=[10,20,34,56,76]
print(number)
number=[10,20,30,40,50]
print(number[0])
print(number[-1])
print(len(number))
number.append(56)
print(number)
number.insert(45,78)
print(number)
number.remove(20)
print(number)
print(max(number))
print(sum(number))
for i in number:
    print(i)
for i in number:
    if i%2==0:
        print(i)
for i in number:
    if i%2!=0:
        PRINT(i)
number=[10,20,30,40]    
print(number)
number.append(50)
print(number)
number.extend([60,70])
print(number)
number.insert(1,67)
print(number)
number.remove(30)
print(number)
print(len(number))
print(max(number))
print(min(number))
number.sort()
print(number)
number.reverse()
print(number)
numuber=[19,4,5,7,5]
duplicates=[]
for x in number:
    if number.count(x)>1 and x not in duplicates:
        duplicates.append(x)
print(duplicates)
