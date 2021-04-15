import csv
from faker import Faker

# Instanciando classe utilizada e configurando para pt-br
fake = Faker('pt_br')

# Abre/cria o arquivo no modo leitura
arquivo = open('arquiv0o.csv', 'w', newline='')

# informa para o csv qual arquivio vai ser escrito
escrever = csv.writer(arquivo)

# for para que o código seja repetido 20 vezes
for item in range(20):
    # Escrevendo no arquivo
    escrever.writerow(['Nome', f'{fake.name()}'])
    escrever.writerow(['Idade', f'{fake.random.randint(0, 100)}'])
    escrever.writerow(['Email', f'{fake.email()}'])
    escrever.writerow(['Telefone' f'{fake.phone_number()}'])

    escrever.writerow([f'{fake.name()}',f'{fake.random.randint(0, 100)}',f'{fake.email()}',f'{fake.phone_number()}\n'])
