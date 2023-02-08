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
#print('A soma entre',n1,'e',n2,'vale ' '{}'.format(s)) 
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
print('A subtração  entre {} e {} vale {}'.format(n1,n2,sub))
print('A multiplicação entre {} e {} vale {}'.format(n1,n2,mult))
print('A divisão entre {} e {} vale {}'.format(n1,n2,d))  
print('A divisão inteira entre {} e {} vale {}'.format(n1,n2,di))
print('A divisão com resto entre {} e {} vale {}'.format(n1,n2,dr))
print('{} elevado a {} vale {}'.format(n1,n2,e))