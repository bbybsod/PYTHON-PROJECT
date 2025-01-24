import pyfiglet
text = pyfiglet.figlet_format('BANK BBYBSOD')
print(text)

print('\n==========EVALUASI PROGRESS==========')
data0 = str(input('masukan nama pengirim :'))
data1 = int(input('masukan nomor rekening :'))
data2 = int(input('masukan jumlah uang yang ingin dikirim :' 'Rp'))
data4 = str(input('masukan nama orang yang dituju :'))
data5 = int(input('masukan jumlah uang di rekening anda :' 'Rp'))

print('\n==========PROSES==========')
print('SELAMAT SDR', data0 , 'SUDAH BERHASIL MENGIRIM KE', data4, 'dengan berhasil')
print('sisa saldo :','Rp',data5 - data2)

print('\n=====Kalkulator pertambahan=====')
a = int(input('masukan angka :'))
b = int(input('masukan angka kedua :'))
c = a + b 
print('hasil =', c)

print('\n======Kalkulator perkalian=======')
a = int(input('masukan angka pertama :'))
b = int(input('masukan angka kedua :'))
c = a*b
print('hasil =', c)

print('\n======Kalkulator pengurangan=======')
a = int(input('masukan angka pertama :'))
b = int(input('masukan angka kedua :'))
c = a-b
print('hasil =', c)

print('\n======Kalkulator pembagian=======')
a = int(input('masukan angka pertama :'))
b = int(input('masukan angka kedua :'))
c = a/b
print('hasil =', c)

print('\n======Kalkulator modulus=======')
a = int(input('masukan angka pertama :'))
b = int(input('masukan angka kedua :'))
c = a%b
print('hasil =', c)

print('\nOR-----AND-----XOR-----NOT')
print('\n==========OR==========')
a = True
b = False
c = a or b
print(a, 'or', b, '=', c)

a = True
b = True
c = a or b
print(a, 'or', b, '=', c)

a = False
b = True
c = a or b
print(a, 'or', b, '=', c)

a = False
b = False
c = a or b
print(a, 'or', b, '=', c)