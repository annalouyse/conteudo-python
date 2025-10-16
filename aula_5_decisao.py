nm_1 = int(input("digite o valor da nota: "))
nm_2 = int(input("digite o valor da nota: "))
nm_3 = int(input("digite o valor da nota: "))
nm_4 = int(input("digite o valor da nota: "))

media = (nm_1 + nm_2 + nm_3 + nm_4) / 4
if media <= 10:
    if media >= 0:
        if media >= 7:
            print("o aluno está aprovado")
        elif media >= 3:
            print("o aluno está em exame")
        else :
            print("o aluno está reprovado")


