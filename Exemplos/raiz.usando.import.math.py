import math 
#from math import sqrt, floor #importar função específica de uma lib #obs1
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
#raiz=srqt(num) #obs1 quando importo uma função especifica posso chamar a função sem botar a lib na frente
print('A raiz de {} é {}'.format(num,raiz))
#print('A raiz de {} é {}'.format(num,math.ceil(raiz))) #exemplo  usando a função ceil da bib math para arredondar a raiz
#print('A raiz de {} é {}'.format(num,math.floor(raiz))) #outro exemplo com outra função
#print('A raiz de {} é {:.2f}'.format(num,raiz)) #{:.2f} deixa com duas casas depois da vírgula 
#ver https://docs.python.org/3/library/index.html para ver as libs nativas de python