import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Se o ângulo mede {}º, seu seno será {:.2f}, seu cosseno será {:.2f} e sua hipotenusa será {:.2f}'.format(ang, sen, cos, tan))
