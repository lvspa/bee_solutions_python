n = int(input())
for i in range(0, n):
    c = int(input())
    aux = 0
    while c > 0:
        calc = c // 2
        c = calc
        aux += 1
    print(f"{aux} dias")

    

