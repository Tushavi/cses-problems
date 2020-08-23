dna = input()
max_length = 0
length = 0
last = None
for d in dna :
    if d == last :
        length += 1
        continue
    elif length>max_length :
        max_length = length
    last = d
    length = 1
if length>max_length :
    max_length = length
print(max_length)
