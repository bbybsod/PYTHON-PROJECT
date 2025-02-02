import pyfiglet

print('___________________________________________')
text = pyfiglet.figlet_format('SPAM WA')
print(text)

input_no = str(input('masukan nomor yang ingin di tuju : '))
input_name = str(input('masukan nama kamu : '))

if input_name == 'yetno':
    print(f'selamat datang {input_name} di tools spam wa')
    print(f'{input_name} mengirim serangan spam wa ke {input_no}')
    print(f'serangan berhasil')
elif input_name == 'bakron':
    print(f'selamat datang ({input_name} di tools spam wa')
    print(f'{input_name} mengirim serangan spam wa ke {input_no}')
    print(f'serangan berhasil')
else:
    print(f'kontol')
