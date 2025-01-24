import random
import pyfiglet

text = pyfiglet.figlet_format('bbybsod')
botolrandom = random.randint(1,4)

print(text)
print('github : github.com/bbybsod')
print('facebook : Rasya Kentang Skibidi')
print('\nWelcome to my early game from python programming language')
print('ini game pertama gw dari python bro, suatu saat gw bakal jadi jago ngoding wkwkwk')
print('made in 2025 24 januari')

print('\n================================================')
a = input('masukan nama mu :')

print('selamat datang', a , 'di game gw')

main = "ya"
b = str(input('mau main? ya/no :'))
if b == main:
     print('ok', a ,'game dimulai')
else:
    print('sialan lo', a)

print('\n===================GAME START==================== ')

pilihan = int(input('[] [] [] [], anggap saja itu adalah 4 botol, menurut kamu dimana botol yang berisi air berada? '))
if pilihan == botolrandom:
        print('selamat', a, 'kamu benar')
else:
        print(a, 'tolol awokwokwok, salah bego, yang bener tuh di botol', botolrandom)