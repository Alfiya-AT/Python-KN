def rearrange(arr):
    p=[]
    n=[]
    for i in arr:
        if i<0:
            n.append(i)
        elif i>=0:
            p.append(i)
    print(f"n:{n}\np:{p}")
    lp=0
    ln=0
    j=0
    
    # for j in range(len(arr)):
    while j<len(arr) and lp<len(p) and ln<len(n):
        if j%2==0 and lp<len(p):
            arr[j]=(p[lp])
            lp+=1
        elif j%2!=0 and ln<len(n):
            arr[j]=(n[ln])
            ln+=1
        j+=1
    print("int arr:",arr)
    if lp<len(p):
        arr[j:]=p[lp:]
        j+=(len(p))
    if ln<len(n):
        arr[j:]=n[ln:]
    return arr
    

arr =  [9, 5, -2, -1, 5, 0, -5, -3, 2]
print("arr",arr)
# [9, -2, 5, -1, 5, -5, 0, -3, 2]
print(rearrange(arr))