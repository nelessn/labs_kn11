text = input("enter text: ")
print("length of this text is:", len(text))
counts = dict()
words = text.split()
text.lower()
for word in words: 
    for i in word:
        if i.isalpha():
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
for k, v in counts.items():
    print(k,v)
