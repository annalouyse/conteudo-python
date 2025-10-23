nota_1 = float(input("digite primeira a nota"))
nota_2 = float(input("digite a segunda nota: "))

media = (nota_1 + nota_2 ) / 2
conceito = ''
if media >= 9:
    if media >= 9 and media <= 10:
        conceito = 'a'
if media >= 7.5:
    if media >= 7.5 and media <= 9:
        conceito = 'b'
if media >= 6:
    if media >= 4 and media <= 6:
        conceito = 'c'
if media >= 4 :
    if media >= 4 and media <= 0:
        conceito = 'd'
else:
    conceito = 'e'
if conceito == 'a' or conceito == 'b' or conceito == 'c':
     situação = "aprovado"
else:
    situação = "reprovado"

print("a media do aluno é:", media)
print("a situação dele é:",situação)
