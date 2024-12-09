import random

site = 'https://iancoleman.io/bip39/'

entropy = 256

#Base Binario
print('Base Binario')
#c = 0
for c in range(0,entropy+1):
    numero = random.randint(0,1)
    print(numero, end='')
    #c = c + 1
#print(c)

print('\n')

#Base 6
print('Base 6')
for c in range(0,entropy+1):
    numero = random.randint(0,5)
    print(numero, end='')

print('\n')

#Dados
print('Dados')
for c in range(0,entropy+1):
    numero = random.randint(1,6)
    print(numero, end='')

print('\n')

#Base 10
print('Base 10')
for c in range(0,entropy+1):
    numero = random.randint(0,9)
    print(numero, end='')

print('\n')

#Hexadecimal [0-9A-F]
print('Hexadecimal')
Entopy_Hexa = '0123456879ABCDEF'
for c in range(0,entropy+1):
    numero = random.choice(Entopy_Hexa)
    print(numero, end='')
