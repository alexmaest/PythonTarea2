print("")
print("Bienvenido")

print("")
print("Ejercicio 1")
Digito = int(input("Ingrese un número: "))
for i in range(Digito+1):
    print('*'*i)

print("")
print("Ejercicio 2")
Digito2 = int(input("Ingrese un número: "))
print(Digito2," ,",end='')
for i in range(1,Digito2+1):
    print(Digito2-i," ,",end='')

print("")
print("")
print("Ejercicio 3")
def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

# Probar
numero = int(input("Dame un número: "))
es_primo = primo(numero)
if es_primo:
	print("Es primo")
else:
	print("NO es primo")