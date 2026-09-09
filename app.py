# Programa para calcular desconto baseado no valor da compra


valor_compra = float(input("Digite o valor da compra: ")) #entrada de valor da compra
if valor_compra < 200: #condição para aplicar desconto de 5%
    desconto = valor_compra * 0.05 #calculo do desconto
    valor_total = valor_compra - desconto #subtrai o desconto do valor total
    print(f"Desconto de 5% aplicado. Valor do desconto: R${desconto:.2f}. Valor total da compra: R${valor_total:.2f}") #saída do valor do desconto
elif valor_compra >= 200 and valor_compra < 300: #condição para aplicar desconto de 10%
    desconto = valor_compra * 0.10 #calculo do desconto
    valor_total = valor_compra - desconto #subtrai o desconto do valor total
    print(f"Desconto de 10% aplicado. Valor do desconto: R${desconto:.2f}. Valor total da compra: R${valor_total:.2f}") #saída do valor do desconto
elif valor_compra >= 300: #condição para aplicar desconto de 15%
    desconto = valor_compra * 0.15 #calculo do desconto
    valor_total = valor_compra - desconto #subtrai o desconto do valor total
    print(f"Desconto de 15% aplicado. Valor do desconto: R${desconto:.2f}. Valor total da compra: R${valor_total:.2f}") #saída do valor do desconto