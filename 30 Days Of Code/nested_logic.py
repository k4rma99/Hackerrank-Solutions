x,y = "31 8 2004","20 1 2004"
da,ma,ya = map(int,x.strip().split())
de,me,ye = map(int,y.strip().split())

hackos = 0

if ye < ya:
    hackos = 10000
elif ya == ye:
    if ma > me:
        hackos = (ma - me) * 500
    elif ma == me and da > de:
        hackos = (da - de) * 15


print(hackos)