nome = 'Precision Time Protocol'
print(nome.count('o'))
print(nome.upper)
print(len(nome.strip())) 
nome = (nome.replace('Precision','Network')) #só mudará de fato após a atribuição feita na linha abaixo
print(nome)
print('Time' in nome)
print(nome.find('Time'))
fracionado = nome.split()
print(fracionado[2][3])