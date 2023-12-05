text = input("enter text: ")
print("length of this text is:", len(text))
counts = dict()
words = text.split()
words.sort()
text.lower()
for word in words:  
    if word in counts:
       counts[word] += 1
    else:
       counts[word] = 1
    if len(word) <= 3:
       continue
    if counts[word] > 1:
       continue
    elif counts[word] == 1:
      print(word)