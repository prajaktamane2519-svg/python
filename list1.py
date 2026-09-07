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
    