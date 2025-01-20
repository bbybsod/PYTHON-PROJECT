import pyfiglet
text = pyfiglet.figlet_format('BBYBSOD BY RASYA')
print(text)
print("==========KONVERSI TEMPERATUR==========")

print("==========KONVERSI FAHRENHEIT==========")
fahrenheit = float(input("masukan suhu dalam fahrenheit : "))
print("suhu fahrenheit adalah =", fahrenheit, "fahrenheit")

kelvin = (fahrenheit - 32)*(5/9) + 273.15
print("suhu kelvin adalah =", kelvin, "kelvin")

celcius = (fahrenheit - 32)*(5/9)
print("suhu celcius adalah =", celcius, "celcius")

reamur = (fahrenheit -32)*(4/9)
print("suhu reamur adalah =", reamur, "reamur")


print("===========KONVERSI KELVIN==============")
kelvin = float(input("masukan suhu dalam kelvin :"))
print("suhu kelvin adalah =", kelvin, "kelvin")

fahrenheit = (kelvin -273.15)*(9/5) + 32
print("suhu fahrenheit adalah =", fahrenheit, "fahrenheit")

celsius = kelvin - 273.15
print("suhu celsius adalah =", celsius, "celcius")

reamur = (kelvin - 273.15)*(4/5)
print("suhu reamur adalah =", reamur, "reamur")

print("============KONVERSI CELCIUS==============")
celcius = float(input("masukan suhu dalam celcius :"))
print("suhu celcius adalah =", celcius, "celcius")

fahrenheit = (celcius*(9/5)) + 32
print("suhu fahrenheit adalah =", fahrenheit, "fahrenheit")

reamur = (4/5)* celcius
print("suhu reamur adalah =", reamur, "reamur")

kelvin = celcius + 273.15 
print("suhu kelvin adalah =", kelvin, "kelvin")

print("===============KONVERSI KELVIN==============")
kelvin = float(input("masukan suhu dalam kelvin :"))

celcius = kelvin - 273.15
print("suhu celcius adalah =", celcius, "celcius")

fahrenheit = (kelvin - 273.15)*(9/5) + 32
print("suhu fahrenheit adalah =", fahrenheit, "fahrenheit")

reamur = (4/5)* (kelvin -273)
print("suhu reamur adalah =",reamur, "reamur")

print("=====================2025 18 JANUARI====================")
