#kalkulator sederhana

print(20*"=")
print('kalkulator sederhana')
print(20*"=")

angka1 = float(input('masukan angka pertama : '))
operator = input('masukan operator ("+,-,x,/") : ')
angka2 = float(input('masukan angka kedua : '))

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil {hasil}")
elif operator == "x":
    hasil = angka1 * angka2
    print(f'hasil {hasil}')
elif operator == "/":
    hasil = angka1 / angka2
    print(f'hasil {hasil}')
else:
    print('command not found')

print('program berakhir')