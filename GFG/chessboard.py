def chess(ip):
    i=0
    d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    var2=int(ip[1])
    if (d.get(ip[0]) + var2)%2==0:
        return "Black"
    else:
        return "White"


ip="b1"
print(chess(ip))