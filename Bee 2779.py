esp=int(input())
figs=int(input())
lista_fig=set()
cont=0
for i in range(0,figs):
    figs_comp=int(input())
    lista_fig.add(figs_comp)
calc=esp-len(lista_fig)
print(calc)


