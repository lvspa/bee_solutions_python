list=[]
n=int(input())
for i in range(n):
    prime=int(input())
    cont=0
    for j in range(1, prime + 1):
        if prime % j == 0:
            cont += 1
    if cont == 2:
        print("Prime")
    else:
        print("Not Prime")
