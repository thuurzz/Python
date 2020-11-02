# URI Online Judge | 1251
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1251

Cont = 0
while True:

    try:

        Texto = input()
        Caracteres = [x for x in Texto]

        Caracteres.sort(reverse=True)

        Memoria = {}
        
        for i in range(len(Caracteres)):

            if Caracteres[i] in Memoria:
                
                Memoria[Caracteres[i]] = Memoria[Caracteres[i]]+1

            else:

                Memoria.update({Caracteres[i]:1})

        if len(Caracteres) != 0 and Cont != 0:
            print()
                
        for j in sorted(Memoria, key=Memoria.get):
            
            print(ord(j), Memoria[j])

        Cont += 1
        
    except EOFError:

        break