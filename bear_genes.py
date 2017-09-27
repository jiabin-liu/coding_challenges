import fileinput
lines=[line.strip() for line in fileinput.input()]
N, genes = int(lines[0]), list(lines[1])
from collections import defaultdict
letters = defaultdict(int)
for g in genes:
    letters[g]+=1
letter_toomany={}
for k,v in letters.items():
    v = v-N/4
    if v > 0:
        letter_toomany[k] = v
substring_min = int(sum(letter_toomany.values()))

p1, p2 = 0, substring_min #pointers to the sub-string we examine
sub_now = genes[p1:p2]
min_len = N

dict_sub=defaultdict(int)
for s in sub_now:
    dict_sub[s]+=1
    
def ismatch(dictsub):
    for l,v in letter_toomany.items():
        if l not in dictsub:
            return False
        elif dictsub[l] < v:
            return False
    return True

while True:
    sub_now = genes[p1:p2]
    if ismatch(dict_sub): #substring satisfy
        min_len = min(min_len,len(sub_now))
        dict_sub[genes[p1]] -= 1
        p1 += 1 #move left pointer forward
    elif p2 < N: #substring not satisfy; can extend right-end
        dict_sub[genes[p2]] += 1
        p2 += 1
    else: #substring not satisfy; cannot extend right-end
        break

print(min_len)