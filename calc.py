data_1 = float(input('masukan angka pertama : '))
operator = input('masukan operator "+,/,-,x": ')
data_2 = float(input('masukan angka kedua : '))

if operator == '+':
    hasil = data_1 + data_2
    print(f'hasilnya adalah {hasil}')
elif operator == 'x':
    hasil = data_1 * data_2
    print(f'hasilnya adalah {hasil}')
elif operator == '-': 
    hasil = data_1 - data_2
    print(f'hasilnya adalah {hasil}')
elif operator == '/': 
    hasil = data_1 / data_2
    print(f'hasilnya adalah {hasil}')
else: 
    print('invalid command')