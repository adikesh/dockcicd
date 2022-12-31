
def replace_null(a,c):
    b=[]
    for i in range(len(a)):
        if a[i]=='null':
            b=b+c
        else:
            b.append(a[i])
    return b
a=[10,'amar','null','karan','null','null']
c=['info','vision','labs']
print(replace_null(a,c))