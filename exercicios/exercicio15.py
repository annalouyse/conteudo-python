valor_hora = float(input("digite o valor do salario: "))
horas_trabalhadas = float(input("digite o tanto de horas trabalhadas: "))

salario_bruto = valor_hora / horas_trabalhadas

print("o valor que o trabalhador ganha por hora é igual a:",valor_hora)

#parte A
salario_bruto = valor_hora * horas_trabalhadas
print("o salario bruto do funcionario sera igual a :",salario_bruto)

# parte B
INSS = salario_bruto * 0.08
print("o valor que o funcionario pagará ao INSS será de:",INSS)

# parte C
sindicato = salario_bruto * 0.05
print(" o valor que o funcionario pagará ao sindicato será de:",sindicato)
ir = 0.11 * salario_bruto


# parte D
salario_liquido = salario_bruto - INSS - sindicato - ir
print("o salario liquido do funcionario será de:",salario_liquido)
