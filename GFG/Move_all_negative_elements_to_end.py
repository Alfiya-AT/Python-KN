def move(arr):
    p=[]
    n=[]
    for i in arr:
        if i<0:
            n.append(i)
        else:
            p.append(i)

    return p+n


arr= [1, -1, 3, 2, -7, -5, 11, 6 ]
print(move(arr))
# Output : [1, 3, 2, 11, 6, -1, -7, -5]