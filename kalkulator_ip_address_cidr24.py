import pyfiglet
text = pyfiglet.figlet_format('BBYBSOD')
print(text)
print("========================KALKULATOR IP ADDRESS CIDR 24==========================")
print("NOTE : GUNAKANLAH ANGKA YANG GENAP DAN TIDAK MEMILIKI KOMA AGAR HASILNYA AKURAT")
  
a = int(input('masukan octate pertama ='))
b = int(input('masukan octate kedua ='))
c = int(input('masukan ocatate ketiga ='))
d = int(input('masukan octate keempat ='))
e = int(input('masukan cidr ='))

jumlah_cidr = 32 - e;
print("jumlah cidr = 2 pangkat", jumlah_cidr ,)
jumlah_ip = (2**jumlah_cidr)
print("jumlah ip =", jumlah_ip, )
ip_host = jumlah_ip - 2
print("jumlah ip = host =", ip_host, )

range_ip = (d/jumlah_ip)*jumlah_ip 
print("range ip pertama =", range_ip, )
range_ip2 = (range_ip + jumlah_ip) - 1 
print("range ip kedua =", range_ip2,)
range_ipreal = range_ip
range_ipreal2 = range_ip2

print("range ip =",a,".",b,".",c,".",range_ipreal,"-",a,".",b,".",c,".",range_ipreal2, )

print("range ip host =", a,".",b,".",c,".", range_ip - 1, "-" , a,".",b,".",c,".",range_ip2 - 1 )
print("ip network =" ,a,".",b,".",c,".",range_ipreal )
print("ip broadcast =", a,".",b,".",c,".",range_ipreal2,)
print("subnetmask =", "255.255.255" , 256 - jumlah_ip)

print("=========================19 JANUARI 2025 XII TKJ 1=========================")
