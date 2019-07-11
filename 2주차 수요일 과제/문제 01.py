input=['hawaii', 'happy', 'doge']

min=input[0]
for i in input:
    if len(i)<len(min):
        min=i

min=list(min)
first=list(input[0])
jeop=[]

for k in range(len(first)):
    if min[k]==first[k]:
        jeop.append(first[k])
    if min[k]!=first[k]:
        break

for j in input:
    temp=jeop.copy()
    jeop.clear()
    tempJ=list(j)
    
    for k in range(len(temp)):
        if temp[k]==tempJ[k]:
            jeop.append(temp[k])
        if temp[k]!=tempJ[k]:
            break
    jeop=temp.copy()

head=""
for i in range(len(jeop)):
    head+=jeop[i]
    
print(head)
