print('____konverter suhu thomas shelby____')
print('1. Celcius ke Fahrenheit')
print('2. Fahrenheit ke Celcius')
print('3. farenhit ke kelvin ')
print('4. kelbin ke farenhit')
print('5. celsius ke kelvin')
print('6. kevin ke celsius ')
print('='* 30)

pilihan= int(input('pilihlah angka 1 sampai 5'))

if pilihan == 1:
    celcius = float(input('masukkan suhu celcius: '))
    farenhit = (celcius* 9/5)+ 32
    print(f'{celcius} c setara dengan {farenhit}')
elif pilihan == 2 :
    farenhit = float(input('masukkan suhu farenhit: '))
    celcius = (farenhit - 32) * 5/9
    print(f'{farenhit} f setara dengan {celcius} c')
elif pilihan == 3 :
    farenhit = float(input('masukkan suhu farenhit: '))
    kelvin = (farenhit - 32) * 5/9 + 273
    print(f'{farenhit} f setara dengan {kelvin} k')
elif pilihan == 4:
    kelvin = float(input('masukkan suhu kelvin: '))
    farenhit = (kelvin - 273) * 9/5 + 32
    print(f'{kelvin} k setara dengan {farenhit} f')
elif pilihan == 5 :
    celcius = float(input('masukkan sushu  celcius: '))
    kelvin = celcius + 273
    print(f'{celcius} C setara dengan {kelvin}')
elif pilihan == 6 :
    kelvin = float(input('masukkan sushu kelvin : '))
    celsius = kelvin - 273
    print(f'{kelvin} c itu setara dengan {celsius}')
else :
    print(' pilihan tidak ada masukkan angka hanya mulai dari 1 hingga 6')