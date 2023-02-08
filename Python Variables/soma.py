n1=int(input('Primeiro número = '))
n2=int(input('Segundo número = '))
#print(type(n1))   
s=n1+n2
sub=n1-n2
mult=n1*n2
d=n1/n2
di=n1//n2
dr=n1%n2
e=n1**n2
#print('A soma entre',n1,'e',n2,'vale ' '{}'.format(s)) #forma alternativa obsoleta
print('A soma entre {} e {} vale {}'.format(n1,n2,s),end=', ') 
print('A subtração  entre {} e {} vale {}'.format(n1,n2,sub),end=', ')
print('A multiplicação entre {} e {} vale {}'.format(n1,n2,mult),end=', ')
print('A divisão entre {} e {} vale {}'.format(n1,n2,d),end=', ')  
print('A divisão inteira entre {} e {} vale {}'.format(n1,n2,di),end=', ')
print('A divisão com resto entre {} e {} vale {}'.format(n1,n2,dr),end=', ')
print('{} elevado a {} vale {}'.format(n1,n2,e))