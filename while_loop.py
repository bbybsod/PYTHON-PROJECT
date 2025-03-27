import pyfiglet
banner = pyfiglet.figlet_format('SEAN MYXZU')
print(banner)

print(20*'=')
print('DDOS ATTACK by Sean')
print(20*'=')

sites = input('masukan domain : ')
botnet = int(input('masukan jumlah botnet: '))
start = 1

if sites == sites:
    while start < botnet:
        start += 1
        print(f'{start}. [+] Serangan ke {sites} berhasil')
else:
    print('failed, try again')

print('program berakhir')