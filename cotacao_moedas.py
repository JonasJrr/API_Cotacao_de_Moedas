import requests
import time 

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") # Fazendo a solicitação HTTP e consumindo as informações dessa url

if requisicao.status_code == 200: # Verificando se está tudo ok com o status da consulta

    resposta = requisicao.json() # Colocando a resposta da consulta em formato json
    resultado = float(resposta['USDBRL']['bid']) # Filtrando a chave/valor desejado e transformando em float

    while True:
        option = input("Digite 1 para converter de real para dólar ou 2 para converter de dólar para real: ")

        try:
            if int(option) == 1: 
                entrada = input("Insira aqui o valor em real para converter para dólar: ") 
                moeda = float(entrada) / resultado
                print("Processando...")
                time.sleep(1)
                # print(entrada, "Reais equivale a", round(moeda, 2),"dolares")
                print(f"{entrada} reais equivale a {moeda:.2f} dolares")
                break
            elif int(option) == 2: 
                entrada = input("Insira aqui o valor em dólar para converter para real: ") 
                moeda = float(entrada) * resultado
                print("Processando...")
                time.sleep(1)
                # print(entrada, "Dolares equivale a", round(moeda, 2), "reais")
                print(f"{entrada} dolares equivale a {moeda:.2f} reais")
                break
            else:
                print("Tente novamente e selecione a opção 1 ou 2")  
        except: 
            print("Não foi possível dar prosseguimento, tente novamente.")
            break
else:
    print("A requisição falhou")        

