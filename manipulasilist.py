import pyfiglet
text = pyfiglet.figlet_format('SEAN MYXZU')
print(text)

print(20*'=')
print('MANIPULASI DATA LIST')
print(20*'=')

data_orang = ["ucup","skibidi", "kocak", "anjay"]
data = [1,3,4,7,3,4,6,10,7,4,5,9,10,2,3,2,2]
print('data yang tersedia ->', data)

print(20*'=')
print("DATA ANGKA")
print(20*'=')
#data count
datahitung_1 = data.count(1)
datahitung_2 = data.count(2)
datahitung_3 = data.count(3)
datahitung_4 = data.count(4)
datahitung_5 = data.count(5)
datahitung_6 = data.count(6)
datahitung_7 = data.count(7)
datahitung_8 = data.count(8)
datahitung_9 = data.count(9)
datahitung_10 = data.count(10)

print(f'data 1 berjumlah -> {datahitung_1}')
print(f'data 2 berjumlah -> {datahitung_2}')
print(f'data 3 berjumlah -> {datahitung_3}')
print(f'data 4 berjumlah -> {datahitung_4}')
print(f'data 5 berjumlah -> {datahitung_5}')
print(f'data 6 berjumlah -> {datahitung_6}')
print(f'data 7 berjumlah -> {datahitung_7}')
print(f'data 8 berjumlah -> {datahitung_8}')
print(f'data 9 berjumlah -> {datahitung_9}')
print(f'data 10 berjumlah -> {datahitung_10}')

print('program berakhir')