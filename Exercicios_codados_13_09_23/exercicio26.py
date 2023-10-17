import math
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
area_com_folga = area_a_pintar * 1.1
quantidade_de_tinta = area_com_folga * (1/6)

# Cálculo da quantidade de latas e galões
# math.ceil() arredonda para cima
latas_18_litros = math.ceil(quantidade_de_tinta / 18)
galoes_3_6_litros = math.ceil(quantidade_de_tinta / 3.6)

# Cálculo dos preços
preco_lata_18_litros = latas_18_litros * 80
preco_galao_3_6_litros = galoes_3_6_litros * 35

# Comprar latas e galões de forma que o preço seja o menor 
# math.floor() arredonda para baixo para que em caso de sobra de tinta,tipo de 4,2 latas de tinta 
# ele arredonde para 4 latas e o resto vira galão
latas_minimas = math.floor(quantidade_de_tinta / 18)
resto_tinta = quantidade_de_tinta - (latas_minimas * 18)
galoes_minimos = math.ceil(resto_tinta / 3.6)
preco_latas_e_galoes = (latas_minimas * 80) + (galoes_minimos * 35)

print("Nome: Matheus Henrique Almeida Vieira Neves --RA: 1050292321036")
print(f"Quantidade de tinta necessária: {quantidade_de_tinta:.2f} litros")
print(f"Comprar apenas latas de 18 litros: {latas_18_litros} latas por R$ {preco_lata_18_litros:.2f}")
print(f"Comprar apenas galões de 3,6 litros: {galoes_3_6_litros} galões por R$ {preco_galao_3_6_litros:.2f}")
print(f"Comprar latas e galões: {latas_minimas} latas e {galoes_minimos} galões por R$ {preco_latas_e_galoes:.2f}")
