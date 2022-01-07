import requests
import webbrowser
'''response = requests.get('http://pudim.com.br/')
try:
    requests.post

except:
    print('O site está fora do ar.')
else:
    print('Site ok!')
    print(requests.post)'''
try:
    webbrowser.open('http://pudim.com.br/')
except:
    print('Não rolou')
else:
    print('EEEEEEEEEE')


