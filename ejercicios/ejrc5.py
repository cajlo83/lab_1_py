
lista_empleados = [{"nombre":"Ale","apellido":"Heidenreich","dni":33},
                   {"nombre":"Eze","apellido":"Taboada","dni":22},
                   {"nombre":"Ger","apellido":"Scarafilo","dni":11}]


'''
for i in range(3):
    dic_empleado = {}
    dic_empleado["nombre"] = input("Ingrese el nombre: ")
    dic_empleado["apellido"] = input("Ingrese el apellido: ")
    dic_empleado["dni"] = input("Ingrese el dni: ")
    lista_empleados.append(dic_empleado)
 '''


for empleado in lista_empleados:
    print("{0} - {1} - {2}".format(empleado["apellido"], empleado["nombre"], empleado["dni"]))

print("")
print(lista_empleados)
    
    