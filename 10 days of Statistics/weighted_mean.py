n = int(input())
X = map(int,input().strip().split())
W = map(int,input().strip().split())
# n = 5
# X = [10, 40, 30, 50, 20]
# W = [1, 2, 3, 4, 5]
numer = den = 0
for x,w in zip(X,W):
    numer += (x*w)
    den += w
print(round(numer/den,1))