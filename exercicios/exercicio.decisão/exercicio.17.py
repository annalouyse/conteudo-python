saque = int(input(" digite o valor a ser sacado: "))

if saque < 10 or saque > 600:
    print("não é possivel sacar o valor informado")
    exit(1)

qts_cem = 0
qts_cinquenta = 0
qtd_dez = 0
qtd_cinco = 0
qtd_um = 0


if saque >= 100:
    qts_cem = saque // 100
    saque = saque - (qts_cem * 100)

if saque >= 50:
      qts_cinquenta = saque // 50
      saque = saque - (qts_cinquenta * 50)

if saque >= 10:
      qtd_dez = saque // 10
      saque = saque - (qtd_dez * 10)

if saque >= 5:
      qtd_cinco = saque // 5
      saque = saque - (qtd_cinco * 5)

qtd_um = saque

print("notas:")
print(f"{qts_cem}notas de 100")
print(f"{qts_cinquenta} notas de 50")
print(f"{qtd_dez} notas de 10")
print(f"{qtd_cinco} notas de 5")
print(f"{qtd_um} notas de 1")
