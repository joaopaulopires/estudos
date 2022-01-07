print('{:#^50}'.format(' DETRAN SP '))
print('='*50)
corrida = float(input('Km/h: '))
if corrida > 80:
    multa = (corrida - 80)*7
    print('Você foi multado. O limite é 80km/h e o radar indicou {} km/h. Portanto, pagará R$ {:.2f} pela infração.'.format(corrida, multa))
else:
    print('Você está dentro do limite de velocidade.')
print('Tenha um bom dia!')