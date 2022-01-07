from time import sleep
import emoji
for c in range(10,0, -1):
    print('\33[4;35m{}\33[m'.format(c))
    sleep(1)
print(emoji.emojize('\33[4;31;40m :hand: FELIZ ANO NOVO!!! \33[m', use_aliases=True))