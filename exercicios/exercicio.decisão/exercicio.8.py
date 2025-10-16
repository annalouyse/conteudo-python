produto_1 = float(input("qual o valor do produto1 ?"))
produto_2 = float(input("qual o valor do produto2? "))
pruduto_3 = float(input("qual o valor do produto3? "))

if produto_1 < produto_2:
    if produto_1<pruduto_3:
        print("você deve comprar o produto_1 que custa:",produto_1)
    else:
        print("você deve comprar o produto_3 que custa:",pruduto_3)
elif produto_2 < produto_1:
   if produto_2 < pruduto_3:
        print("você deve comprar o produto_2 que custa: ",produto_2)
   else:
       print("você deve comprar o produto_1 que custa: ", pruduto_3)
