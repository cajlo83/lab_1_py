from customtkinter import *

app = CTk()

def button_on_click():
    print("Vamos a aprender python!!")

button = CTkButton(master=app, text="Click me!", command=button_on_click)
button.grid()

app.mainloop()





'''
entrada = input("Ingresa un número decimal (positivo o negativo): ")

validar_numero_decimal = lambda x: (True, float(x)) if x.replace('.', '', 1).lstrip('-').isdigit() else (False, None)

es_numero_decimal, numero = validar_numero_decimal(entrada)

if es_numero_decimal:
    print(f"Has ingresado un número decimal válido: {numero}")
else:
    print("El valor ingresado no es un número decimal válido.")
'''

