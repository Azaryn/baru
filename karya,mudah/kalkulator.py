print('====KALKULAATOR CIHUY====')
print('-' * 30)
print('1. penjumlahan')
print('2. pengurangan')
print('3. perkalian')
print('4. pembagian')

print('-' * 30)
pilihan = int(input('pilih metode aritmatika : '))
angak1 = float(input('masukkan angka pertama: '))
angka2 = float(input('masukkan angka kedua: '))

if pilihan == 1:
    print(f'{angak1} + {angka2} = {angak1 + angka2}')
elif pilihan == 2:
    print(f'{angak1} - {angka2} = {angak1 - angka2}')
elif pilihan == 3:
    print(f'{angak1} * {angka2} = {angak1 * angka2}')
elif pilihan == 4 :
    if angka2 != 0:
        print(f'{angak1} / {angka2} = {angak1 / angka2}')
    else : 
        print('Angka yang dibagi dengan nol tidak terdefinisi, artinya tidak menghasilkan hasil')
else :
    print('hanya masukkan angak 1 sampai 4')