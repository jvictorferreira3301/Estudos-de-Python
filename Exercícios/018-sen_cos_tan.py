from math import sin, cos, tan, radians, ceil
an = float(input('Digite o ângulo: '))
seno = sin(radians(an))
coss = cos(radians(an))
tg = tan(radians(an))
print('o seno do ângulo {} é {:.2f};'.format(an,seno))
print('O cosseno do ângulo {} é {:.2f};'.format(an, coss))
print('A tangente do ângulo {} é {:.2f};'.format(an,tg))

print(f'O seno do ângulo {an, seno}')

