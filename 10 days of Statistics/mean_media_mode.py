
t = int(input())
arr = sorted(map(int,input().strip().split()))
mean = sum(arr)/t
if t % 2 == 0: 
    median = (arr[t//2]  + arr[t//2 - 1] )/2
else: 
    median = arr[t//2] 
occurences =  set([arr.count(i) for i in arr])
if len(occurences) == 1:
    mode = min(arr)
else:
    for i in arr: 
        if arr.count(i) == max(occurences):
            mode = i
            break

print(mean)
print(median)
print(mode)