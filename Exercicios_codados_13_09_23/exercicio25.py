altura=float(input("Digite a altura: "))
def pesoIdeal(altura):
    def alturamen(altura): 
       return round((72.7*altura)-58,2)
    def alturamul(altura):
       return round((62.1*altura)-44.7,2)
    mensagem="O peso ideal para homens é de {} e para mulheres é de {}".format(alturamen(altura),alturamul(altura))
    return mensagem
print("Nome: Matheus Henrique Almeida Vieira Neves --RA: 1050292321036")
print(pesoIdeal(altura))