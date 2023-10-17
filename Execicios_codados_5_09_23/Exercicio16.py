
dataNaciEmDias = int(input("Digite Sua quantidade de dias "));
anos=dataNaciEmDias//365;
meses=(dataNaciEmDias % 365) //30
dias=(dataNaciEmDias %365) %30
print(f"Voce tem um total de {anos} anos , {meses} meses e {dias} dias de Vida")