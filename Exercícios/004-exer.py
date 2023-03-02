e=input('Insira algo:')
print('o tipo de var é',type(e))
print('{} é um decimal?'.format(e),e.isdecimal())
print('{} é alfanumérico?'.format(e),e.isalnum())