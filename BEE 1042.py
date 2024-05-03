a, b, c = map(int, input().split())
lista = [a, b, c]
for i in range(len(lista)-1):
    for j in range(len(lista)-1-i):
        if lista[j] > lista[j + 1]:
           lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(f"{lista[0]}\n{lista[1]}\n{lista[2]}\n")
print()
print(f"{a}\n{b}\n{c}\n")
