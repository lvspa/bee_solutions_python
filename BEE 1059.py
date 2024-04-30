def calcular_garrafas(T):
    for _ in range(T):
        N, K = map(int, input().split())  # Lendo N e K para cada caso de teste
        garrafas_cheias = N  # Inicialmente, o cliente tem N garrafas cheias
        garrafas_vazias = N  # Inicialmente, o cliente tem N garrafas vazias

        # Enquanto o cliente tiver garrafas vazias suficientes para trocar por uma cheia
        while garrafas_vazias >= K:
            garrafas_cheias += 1  # Troca K garrafas vazias por uma cheia
            garrafas_vazias -= K  # Atualiza o número de garrafas vazias

            # O cliente agora tem uma garrafa cheia adicional
            garrafas_vazias += 1

        print(garrafas_cheias)  # Imprime o total de garrafas cheias no segundo dia


# Lendo o número de casos de teste
T = int(input())

# Chamando a função para calcular o número de garrafas para cada caso de teste
calcular_garrafas(T)

