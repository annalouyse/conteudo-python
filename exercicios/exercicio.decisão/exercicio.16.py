a = float(input(" digite o valor de a: "))
if a == 0:
    print("não é uma equação do segundo grau")
else:
    b = float(input(" digite o valor de b: "))
    c = float(input(" digite o valor de c: "))
    delta =( b**2 )- (4*a)*c
    print(" delta é:",delta)

    if delta < 0:
        print("a equeção não possui raízes reais")
    elif delta == 0 :
        x = -b / (2*a)
        print("a equação possui raízes reais")

    else:
        x1 = (-b + delta ) / 2*a
        x2 = ( -b - delta ) / 2*a
        print("o x1 dessa equação é ",x1)
        print(" o x2 dessa equação é",x2)