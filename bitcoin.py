import urllib.request, json, time
from datetime import datetime
from colorama import Fore, Back, Style
import colorama

# Inicializa o colorama, permitindo string colorida no terminal
colorama.init(autoreset=True)

def obter_dolar():
	try:
		url = "https://api.coindesk.com/v1/bpi/currentprice/btc.json"
		with urllib.request.urlopen(url) as url:
			response = url.read()
			data = json.loads(response.decode('utf-8'))
			dolar = float(data['bpi']['USD']['rate'].replace(",", ""))
			return dolar
	except urllib.error.HTTPError:
		print('URL inexistente!')

def obter_real():
	try:
		url = "https://api.coindesk.com/v1/bpi/currentprice/brl.json"
		with urllib.request.urlopen(url) as url:
			response = url.read()
			data2 = json.loads(response.decode('utf-8'))
			real = float(data2['bpi']['BRL']['rate'].replace(",", ""))
			return real
	except urllib.error.HTTPError:
		print('URL inexistente!')

def obter_hora():
	data_e_hora_atuais = datetime.now()
	data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
	print(data_e_hora_em_texto)
	return data_e_hora_em_texto

def exibir_valores(tempo=1):
	# Realiza a requisição dos valores iniciais e salva nas variaveis
	dolar = obter_dolar()
	real = obter_real()
	# Seta a flag igual a True
	nova_cotacao = True
	# Inicializa o programa com a primeira cotação
	print(Style.BRIGHT+"Inicializando o sistema..."+Style.RESET_ALL)
	print(72*"=")
	obter_hora()
	print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +"---> Preço atual do Bitcoin: "+Style.RESET_ALL+"1 Bitcoin vale %f dólares!" % dolar)
	print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +"---> Preço atual do Bitcoin: "+Style.RESET_ALL+"1 Bitcoin vale %f reais!" % real)
	print(72*"=")

	# Loop para analisar a variação de valores
	while True:
		valor_atual_dolar = obter_dolar()
		valor_atual_real = obter_real()

		# Apresenta os valores de queda do Bitcoin
		if valor_atual_dolar < dolar and valor_atual_real < real:
			print(72*"=")
			obter_hora()
			print(Style.BRIGHT + Fore.RED +"---> Preço do Bitcoin caindo: "+Style.RESET_ALL+ "1 Bitcoin vale agora %f dólares!" % valor_atual_dolar)
			print(Style.BRIGHT + Fore.RED +"---> Preço do Bitcoin caindo: "+Style.RESET_ALL+ "1 Bitcoin vale agora %f reais!" % valor_atual_real)
			print(72*"=")
			nova_cotacao = True
		# Apresenta os valores de subida do Bitcoin
		elif valor_atual_dolar > dolar and valor_atual_real > real:
			print(72*"=")
			obter_hora()
			print(Style.BRIGHT + Fore.GREEN +"---> Preço do Bitcoin subindo: "+Style.RESET_ALL+ "1 Bitcoin vale agora %f dólares!" % valor_atual_dolar)
			print(Style.BRIGHT + Fore.GREEN +"---> Preço do Bitcoin subindo: "+Style.RESET_ALL+ "1 Bitcoin vale agora %f reais!" % valor_atual_real)
			print(72*"=")
			nova_cotacao = True
		# Trata o erro de demora de resposta do valor da moeda REAL e ignora caso houver uma resposta que obtenha um valor igual ao anterior
		elif (valor_atual_dolar < dolar and valor_atual_real == real) or (valor_atual_dolar > dolar and valor_atual_real == real):
			continue
		# Se a flag for igual a True, reinicia o processo de requisição de novos dados
		else:
			if nova_cotacao == True:
				print("\n"+Style.BRIGHT+"Aguardando uma nova cotação..."+Style.RESET_ALL)
				nova_cotacao = False
		# Reseta as minhas variaveis e obtem novos valores
		dolar = obter_dolar()
		real = obter_real()
		time.sleep(tempo)

exibir_valores()