import pyfiglet
text = pyfiglet.figlet_format('BBYBSOD')
print(text)
data = int(input("masukan data :"))
print("data ini adalah =", data, ",type =", type(data))
data_bool = bool(data)
data_float = float(data)
data_str = str(data)
print("data ini adalah =", data_bool, ",type =", type(data_bool))
print("data ini adalah =", data_float, ",type =", type(data_float))
print("data ini adalah =", data_str, ",type =", type(data_str))