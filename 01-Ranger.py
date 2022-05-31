from random import randint, shuffle
print('# Lista randomica a ser impressa usando o range')
lista_randomica = []
for i in range(0,10):
    lista_randomica.append(randint(0,100))
print('Lista Original', lista_randomica)
print()

print('# Para inverter a  ordem da lista usamos a função reverse()')
lista_randomica.reverse()
print('Lista original', lista_randomica)
print()

print('#Para ordenar a lista usamos a função sort()')
lista_randomica.sort()
print('Lista Ordenada',lista_randomica)
print()

print('Máximo elemento da lista com a função max()',max(lista_randomica))
print()

print('Minimo elemento da lista com a função mix()', min(lista_randomica))
print()

print('#Trabalhando com entrada de dados usando a função input()')
acao = input('Insira um simbolo de uma ação. Ex: MGLU3')
print(f'O cliente deseja comprar a ação {acao}')
print()

print('#Quebrando String em lista List Comprehension')
lista_caracteres = []
for i in acao:
    lista_caracteres.append(i)
print(lista_caracteres)
print()

print('# Inserindo partes a elemento de uma lista com a função append()')
ativos = ['VALE','MGLU','PETRO','RIOF','BEEF']
ativos_alterados = []
for ativo in ativos:
    ativos_alterados.append(ativo + '3')
print(ativos_alterados)
print()




