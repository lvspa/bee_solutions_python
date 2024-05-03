n=int(input())
calc=n*n
if n%2==0:
    calc_final=calc/2
    print(f"{calc_final:.0f} casas brancas e {calc_final:.0f} casas pretas")
else:
    calc_aux=calc//2
    print(f"{calc_aux+1} casas brancas e {calc_aux} casas pretas")

