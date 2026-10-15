g=9
h=float(g)
print(type(h))
g="12"
h=int(g)
print(h)
text="python"
result=text[::-1]
print(result)
text="madam"
if text==text[::-1]:
    print("palidrom")
else:
    print("non palidrom")
text="prajakta"
print(len(text))
print(text[0])
print(text[-1])
print(text[::-1])
print(text.upper())
print(text.lower())
print("x" in text)
print(text.replace("a","E"))
print(text.strip())
print(text.count("t"))
text="i love python"
count=0
for ch in text.lower():
    if ch in "aeiou":
        count+=1
print(count)
text="i love python"
count=0
for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count+=1
    print(count)
text="python is easy to learn"
print(len(text.split()))
text="python is easy"
print(text.title())
text="py th on"
print(text.replace(" ",""))
text="12345"
print(text.isdigit())
text="python"
print(text.upper())
print(text.find("h"))
print(text.lower())