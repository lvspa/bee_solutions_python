list=[]
while True:
    try:
        sa, so = map(int, input().split())
        calc = so - sa
        list.append(calc)
    except ValueError:
        break
    except EOFError:
        break

for i in range(0,len(list)):
    print(list[i])

