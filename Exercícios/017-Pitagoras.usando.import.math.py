from math import sqrt
catop=float(input('Cateto Oposto: \n'))
cataf=float(input('Cateto Adjacente: \n'))
hipotenusa=sqrt((catop**2+cataf**2))
print('Hipotenusa: {:.2f}'.format(hipotenusa))

'''from math import hypot
cataf = float(input('Cateto Adjacente: \n'))
catop = float(input('Cateto Oposto: \n'))
hipotenusa = hypot(cataf,catop)
print('Hipotenusa: {:.2f}'.format(hipotenusa))