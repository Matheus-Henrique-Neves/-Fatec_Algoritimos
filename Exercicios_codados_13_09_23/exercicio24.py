var1=int(input("Digite o primeiro numero: "))
var2=int(input("Digite o segundo numero: "))
def calculos(var1,var2):
    def mutiplicacao(var1,var2):
        return round((var1*var2),2)
    def soma(var1,var2):
        return round((var1+var2),2)
    def subtracao(var1,var2):
        return round((var1-var2),2)
    def divisao(var1,var2):
        return round((var1/var2),2)
    return "Os resutatos são \n mutiplicação: {} \n soma: {} \n subtração: {} \n divisão: {} ".format(mutiplicacao(var1,var2),soma(var1,var2),subtracao(var1,var2),divisao(var1,var2))
print("Nome: Matheus Henrique Almeida Vieira Neves --RA: 1050292321036")
print(calculos(var1,var2))