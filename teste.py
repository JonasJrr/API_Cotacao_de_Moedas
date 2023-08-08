#COTAÇÃO DE MOEDAS

import requests #Importando o módulo requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") #Fazendo a solicitação HTTP e consumindo as informações dessa url

if requisicao.status_code == 200:
    resposta = requisicao.json() #transformando a resposta em formato json
    resultado = float(resposta['USDBRL']['bid']) #filtrando a chave/valor que desejado e transformando em float
else:
    print("A requisição falhou.")    

option = input("Digite 1 para converter de real para dólar ou 2 para converter de dólar para real: ") #opção do usuário

if int(option) == 1: 
    entrada = input("Insira aqui o valor em real para converter para dólar: ") 
    moeda = float(entrada) / resultado
    print(entrada, "Reais equivale a", round(moeda, 2),"dolares")
elif int(option) == 2: 
    entrada = input("Insira aqui o valor em dólar para converter para real: ") 
    moeda = float(entrada) * resultado
    print(entrada, "Dolares equivale a", round(moeda, 2), "reais")
else: 
    print("Insira um valor válido.")

