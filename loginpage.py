import pyfiglet

pw = 123


text = pyfiglet.figlet_format('bbybsod')
print(text)

print('==========SELAMAT DATANG==========')
print('github: github.com/bbybsod')
print('TikTok: sean.myxzu')
print('==================================')
print('\n============LOGIN===============')

nama = str(input('username :'))
password = int(input('password :'))

if password == pw: 

    print('\n============================DARK WEB=============================')
    print('\nLIST MENU')
    print('___________________________________________________________________________')
    print('| id |   NAMA BARANG      |     MERK       |     STOK     |     HARGA     |')
    print('___________________________________________________________________________')
    print('| a. |    Desert Eagle    |    unknown     |     183      |  Rp17.000.000 |')
    print('| b. |      AK47          |    PINDAD      |     450      |  Rp56.000.000 |')
    print('| c. |      M416          |    unknown     |     198      |  Rp34.465.000 |')
    print('| d. |    Bitcoin         |    satoshi     |      3       | Rp633.000.000 |')
    print('_________________________________________________________________________')

    #NAMA BARANG======================
    a = 'Desert Eagle'
    b = 'AK47'
    c = 'M416'
    d = 'Bitcoin'
    #STOK=============================
    a1 = 183
    b1 = 450 
    c1 = 198 
    d1 = 3 
    #HARGA==============================
    a2 = 17,000,000
    b2 = 56,000,000
    c2 = 34,000,000
    d3 = 633,000,000

    user_choice = str(input('Masukan id barang :'))
    user_stok = int(input('Masukan jumlah :'))
    if user_choice == a:
        print('barang', a, 'sebanyak', user_stok,'sukses di beli')
    elif user_choice == b:
        print('barang', b, 'sebanyak', user_stok,'sukses di beli')
    elif user_choice == c: 
        print('barang', c, 'sebanyak', user_stok,'sukses di beli')
    elif user_choice == d: 
        print('barang', d, 'sebanyak', user_stok,'sukses di beli')
    else:
        print('kesalahan input')

else:
    print('password anda salah, ulangi lagi!')
    exit()