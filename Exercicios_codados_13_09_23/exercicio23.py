valorCompra = float(input("Digite o valor da compra: "))
def desconto(valorCompra):
    if valorCompra >= 100 and valorCompra < 200:
        return round(valorCompra*0.9,2)
    elif  valorCompra >= 200 and valorCompra < 300:
        return round(valorCompra*0.85,2)
    elif valorCompra>= 300:
        return round(valorCompra*0.8,2)
    else:
        return valorCompra
print("Nome: Matheus Henrique Almeida Vieira Neves --RA: 1050292321036")
print("O valor da compra é de ",desconto(valorCompra))