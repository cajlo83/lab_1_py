'''
carlo morici

Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.


'''
#creo lista
lista_enteros = list()

#inicializo contadores y valores fuera del bucle
contador_pares = 0
contador_impares = 0
suma_positivos = 0
producto_negativos = 1
menor_numero = int()
bandera_negativos = False



#bucle para rellener 5 lugares de la lista
indice = 0
while indice < 5:
    entrada = input("posicion numero " + str(indice) + " . Ingrese un numero entero distinto de 0\n")
    entrada = int(entrada)
    if (entrada == 0):
        print ("ha ingresado 0, reintnete")
    else:
        lista_enteros.append(entrada)
        

        # a)
        if (entrada % 2 == 0):
            contador_pares += 1

            # c)
            if (contador_pares == 1):
                mayor_par = entrada
            elif(contador_pares > 1 and mayor_par < entrada):
                mayor_par = entrada
            
        else:
            contador_impares += 1

        # b)
        if (indice == 0):
            menor_numero = entrada
        else:
            if (menor_numero > entrada):
                menor_numero = entrada
        
        

        # d)
    
        if (entrada > 0):
            suma_positivos += entrada

        # e)
        if (entrada < 0):
            bandera_negativos = True
            producto_negativos *= entrada
        
        indice += 1







#imprimo lista
print(lista_enteros)

#a
print("pares: " + str(contador_pares) + " || impares: " + str(contador_impares)) 
#b
print("menor numero ingresado: " + str(menor_numero))
#c
print("mayor numero par ingrsado: " + str(mayor_par))
#d
print("suma de los positivos: " + str(suma_positivos))
#d
if (bandera_negativos == True):
    print("producto de los negativos: " + str(producto_negativos))
else:
    print("no ingresaron numeros negativos")



'''
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.

'''