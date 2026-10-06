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
