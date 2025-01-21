import pyfiglet
text = pyfiglet.figlet_format('BBYBSOD ')
print(text)
print('OPERASI LOGIKA OR,NOT,AND,XOR')
print('============NOT==============')
a  = True 
b  = not a 
print('data a =' , a)
print('data c =', b)

print('==========OR==========')
a = True
b = False
c = a or b 
print(a, 'or' , b ,'=', c, )
a = True
b = True
c = a or b
print(a, 'or', b, '=', c)
a = False
b = True
c = a or b
print(a, 'or', b, '=', c)
a = False
b = False
c = a or b
print(a, 'or', b, '=', c)

print('==========AND==========')
a = True
b = False
c = a and b 
print(a, 'and' , b ,'=', c, )
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)

print('==========XOR==========')
a = True
b = False
c = a ^ b 
print(a, 'xor' , b ,'=', c, )
a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)