#input()
height=[20,7,23,19,10,15,25,8,13]

height.sort(reverse=True)
print(height)

origin=0
for i in height:
    origin+=i
#print(origin)

L=0
R=1
while L<7:
    if sum==100:
        del height[R]
        del height[L]
        break
    while R<8:
        sum=origin-height[R]-height[L]
        if sum==100:
            break
        R+=1
    L+=1

print(height)
