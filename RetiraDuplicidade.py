import csv
from csv import reader

newlist = []
key = ["email"] # Header do csv para identificação do insert no banco 

print("\n\n-=== SCRIPT PARA RETIRAR E-MAILS DUPLICADOS -=== \n")

nome_lista_antiga = str(input("Digite o nome da lista que contém todos os e-mails -> "))
nome_lista_nova = str(input("\nDigite o nome para a nova lista a ser gerada -> "))

print("\n\n Processando...")

with open('csv/' + nome_lista_antiga + '.csv', 'r') as csv_file1:
    csv_reader1 = reader(csv_file1, delimiter = '\t')
    lista1 = list(csv_reader1)

for element in lista1:
    if element not in newlist:
        newlist.append(element)

f = open('csv/' + nome_lista_nova + '.csv', 'w', newline='', encoding='utf-8')
w = csv.writer(f)   

w.writerow(key) # Adiciona o Header no CSV

for c in newlist:           
    w.writerow(c)

print("\n")
print("========================================\n")
print("Sucesso, a lista foi gerada! \n")
print(f"Total de e-mails da lista antiga -> [{len(lista1)}]")
print(f"Total de e-mails na nova lista -> [{len(newlist)}]")
print(f"Total de e-mails duplicados -> [{len(lista1) - len(newlist)}]")
print("\n========================================\n\n")

