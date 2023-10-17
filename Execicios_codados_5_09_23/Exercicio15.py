from datetime import datetime;
dataNacimento = input("Digite Sua data de Nacimento (dd/mm/aaaa) ");
dataNacimento = datetime.strptime(dataNacimento , "%d/%m/%Y");
dataAtual=datetime.now();
diferencaData= dataAtual-dataNacimento;
idadeemDias=diferencaData.days
print("Nome: Matheus Henrique Almeida Vieira Neves --RA: 1050292321036")
print(f"Voce tem um total de {idadeemDias} dias de vida ")