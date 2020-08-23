facts = [1,1,2,6,24,120,720]
def fact(n) :
    if n<len(facts) :
        return facts[n]
    else :
        for i in range(len(facts),n+1) :
            facts.append(facts[-1]*i)
        return facts[-1]

def permute(di, word) :
    if sum(di.values()) < 1 :
        print(word)
    else :
        for (k,v) in sorted(di.items()) :
            new_di = di.copy()
            if v < 1 :
                continue
            new_di[k] -= 1
            word += k
            permute(new_di,word)
            new_di[k] += 1
            word = word[:-1]
s = input()
di = {}
for ch in s :
    di[ch] = di.get(ch,0) + 1
numways = fact(len(s))
for v in di.values() :
    numways//=fact(v)
print(numways)
permute(di,'')
