from exercicios.exercicio8 import horas_trabalhadas

salario_bruto = float(input("digite o valor do salario: "))
horas_trabalhadas = float(input("digite o tanto de horas trabalhadas: "))

valor_hora = salario_bruto / horas_trabalhadas

print("o valor que o trabalhador ganha por hora é igual a:",valor_hora)

#parte A
salario_bruto = valor_hora * horas_trabalhadas
print("o salario bruto do funcionario sera igual a :",salario_bruto)

# parte B
pagou_INSS = salario_bruto * 0.08
print("o valor que o funcionario pagará ao INSS será de:",pagou_INSS)

# parte C
pagou_sindicato = salario_bruto * 0.05
print(" o valor que o funcionario pagará ao sindicato será de:",pagou_sindicato)

# parte D
salario_liquido = salario_bruto - pagou_INSS - pagou_sindicato
print("o salario liquido do funcionario será de:",salario_liquido)
