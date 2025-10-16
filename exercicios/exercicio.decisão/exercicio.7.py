numero_1 = int(input("digite o primeiro numero: "))
numero_2 = int(input("digite o segundo numero: "))
numero_3 = int(input("digite o terceiro numero: "))

if numero_1 > numero_2:
    if numero_1>numero_3:
        print("o maior é o numero",numero_1)
    else:
        print("o maior é o numero", numero_3)
elif numero_2 > numero_1:
   if numero_2 > numero_3:
        print("o maior é o numero",numero_2)
   else:
       print("o maior é o numero", numero_3)

if numero_1 < numero_2:
    if numero_1< numero_3:
        print("o menor é o numero",numero_1)
    else:
        print("o menor é o numero", numero_3)
elif numero_2 < numero_1:
   if numero_2 < numero_3:
        print("o menor é o numero",numero_2)
   else:
       print("o menor é o numero", numero_3)