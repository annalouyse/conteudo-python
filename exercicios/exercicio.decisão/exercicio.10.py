turno = input("Em que turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ")

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("Opção inválida! Por favor, digite M, V ou N.")