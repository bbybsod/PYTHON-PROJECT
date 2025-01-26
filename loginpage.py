import pyfiglet

pw = 123

#USER INTERFACE===========================
text = pyfiglet.figlet_format('bbybsod')
print(text)

print('==========SELAMAT DATANG==========')
print('github: github.com/bbybsod')
print('TikTok: sean.myxzu')
print('==================================')
print('\n============LOGIN===============')
#==========================================
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
    a2 = 17000000
    b2 = 56000000
    c2 = 34000000
    d3 = 633000000
    #PROSES INPUT DATA===================
    user_choice = str(input('Masukan id barang :'))
    user_stok = int(input('Masukan jumlah :'))
    user_money = int(input('masukan sisa uang kamu di rekening :'))
    #=====================================
    if user_choice == "a":
        print('barang Desert Eagle sebanyak', user_stok,'dengan harga', a2*user_stok, 'sukses di beli')
        print('sisa uang di rekening mu sisa :', user_money - a2)
        print('sisa stok desert eagle :', a1 - user_stok)
    elif user_choice == 'b':
        print('barang AK47 sebanyak', user_stok,'dengan harga', b2*user_stok,'sukses di beli')
        print('sisa uang di rekening mu sisa :', user_money - b2)
        print('sisa stok AK47 :', b1 - user_stok)
    elif user_choice == 'c': 
        print('barang M416 sebanyak', user_stok,'dengan harga', c2*user_stok ,'sukses di beli')
        print('sisa uang di rekening mu sisa :', user_money - c2)
        print('sisa stok M416 :', c1 - user_stok)
    elif user_choice == "d": 
        print('barang Bitcoin sebanyak', user_stok, 'dengan harga', d3*user_stok ,'sukses di beli')
        print('sisa uang di rekening mu sisa :', user_money - d3)
        print('sisa stok Bitcoin :', d1 - user_stok)
    else:
        print('kesalahan input')
    #======================================
else:
    print('password anda salah, ulangi lagi!')
    exit()
