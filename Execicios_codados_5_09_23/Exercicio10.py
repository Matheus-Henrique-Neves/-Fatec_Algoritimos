produ01=float(input("Digite o Valor do 1º produto "));
produ02=float(input("Digite o Valor do 2º produto "));
produ03=float(input("Digite o Valor do 3º produto "));
produ04=float(input("Digite o Valor do 4º produto "));
produ05=float(input("Digite o Valor do 5º produto "));
valorTotal=(produ01+produ02+produ03+produ04+produ05);
print("O valor a ser pago é de ",valorTotal);
pagamento=float(input("Qual foi o valor pago pelo produtos"));
print("Nome: Matheus Henrique Almeida Vieira Neves --RA: 1050292321036")
print("O troco é de = ",round(pagamento-valorTotal,2)); 

