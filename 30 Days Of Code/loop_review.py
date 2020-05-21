# Enter your code here. Read input from STDIN. Print output to STDOUT

def func(s):
    s1 = s2 = ""
    s1 = s[::2]
    s2 = s[1::2]
    return(s1 + " " + s2)
    pass

t = int(input())
for i in range(t):
    s = input()
    print(func(s))
