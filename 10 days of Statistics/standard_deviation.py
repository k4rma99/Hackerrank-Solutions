t = int(input())
arr = map(int,input().strip().split())

x = set(ar)
count = 0
for i in x:
    s = ar.count(i)
    if s == 2:
        count += 1
        continue
    if s%2 == 0:
        count += 2
    else:
        if (s-1)%2 == 0 and s!=1:
            count += 2
print(count)

print(sd)

