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
