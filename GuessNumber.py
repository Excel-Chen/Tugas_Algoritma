import random
import os

plays = 0
win = 0
lose = 0

while True:
    os.system('cls')
    ra = random.randint(1,10)
    print('Angka teracak = n')
    for i in range(1,4):
        try:
            angka = int(input(f'\nAngka tebakan anda [ Percobaan ke {i} ] = '))
            if angka < 1 or angka > 10 :
                raise Exception()
        except :
            print('Err : Anda hanya boleh input bil bulat (1 - 10) bro')
        else :
            if angka < ra :
                print('nay, tebakan anda terlalu rendah')
            elif angka > ra:
                print('nay, tebakan anda terlalu tinggi')
            elif angka == ra:
                print('Yes, You Win')
                win += 1
                plays += 1
                break
    if angka != ra :
        print('Sorry,You Lose')
        lose += 1
        plays += 1
    while True:
        ulang = input('\nContinue ? (y/n) ')
        if ulang in ('y','n'):
            break
    if ulang in ('n'):
        print("\nSummary :")
        print('---------')
        print('Banyak permainan =',plays)
        print('Banyak menang =',win)
        print('Banyak kalah =',lose)
        break