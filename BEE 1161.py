lista_a = []
lista_b = []

while True:
    entrada = input().strip()
    if not entrada:
        break

    a, b = map(int, entrada.split())

    fatorial_a = 1
    for i in range(1, a + 1):
        fatorial_a *= i

    fatorial_b = 1
    for j in range(1, b + 1):
        fatorial_b *= j

    lista_a.append(fatorial_a)
    lista_b.append(fatorial_b)

for i in range(len(lista_a)):
    print(lista_a[i] + lista_b[i])