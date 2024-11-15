import pandas as pd
import numpy as np


while True :
    print('===welcome===')
    print('1. melihat daftar to go list')
    print('2. menambahkan tugas baru')
    print('3. exit')

    inputan = int(input('pilih opsi'))
    if inputan == 1:
        print('===daftar to go list===')
        with open('to_go_list.csv' , mode = 'r') as file:
            data = file.read()
        print(data)
    elif inputan == 2:
        nama_tugas = input('masukkan tugas baru : ')
        with open('to_go_list.csv' , mode = 'a') as file:
            data =file.write(nama_tugas + '\n')
            print(data)
    elif inputan == 3:
        print('terima kasih selamat datang kembali  :D')
        break
    else :
        print('gak liat cuman ada 3 ?')
        

