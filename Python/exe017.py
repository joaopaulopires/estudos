import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = math.hypot(co, ca)
print('Considerando os valores desses catetos, o comprimento da hipotenusa desse triângulo retângulo é {:.2f}'.format(hip))