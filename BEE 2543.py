n,i=map(int,input().split())
cont=0
for k in range(0,n):
    id,gp=map(int,input("").split())
    if id==i and gp==0:
        cont+=1

print(cont)