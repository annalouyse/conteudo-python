from exercicios.exercicio15 import salario_liquido

valor_hora = float(input("digite o valor de cada hora trabalhada: " ))
horas_trabalhadas = float(input("digite o tanto de horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <=  1500:
    ir = (salario_bruto * 0.05)
elif salario_bruto <= 2500:
    ir = (salario_bruto * 0.10)
elif salario_bruto > 2500 :
    ir = (salario_bruto * 0.20)

sindicato = salario_bruto * 0.03

FGTS = salario_bruto * 0.11

descontos = ir + FGTS

salario_liquido = salario_bruto - descontos

print("o salario bruto é:"valor_hora * horas_trabalhadas)
print("o salario com o desconto do ir fica:", ir)
print("o salario com o desconto do sindicato fica:",sindicato)
print("o salario com o desconto do FGTS fica:", FGTS)
print("o salario liquido é de: ", salario_liquido)
