import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''
'''
numero = 0
while numero == 0:
    numero = 1
    print("dentro del while")

print("fuera del while")

contador == 0
while contador < true:
    contador = + 1
    contador += 1

    if contador == 11:
        break
    print(f"{contador}- dentro del while)
    

    contador = 0
    acumulador = 0 
    bandera = 0
    i = 0
    
    while true:
    
        if bandera 0:
        print("primera vez")
        bandera = 2

        ingreso valor = input("ingrese valor: ")
        i += 1

        if i == 5
        break
        

    while contador < 10:
    
    contador += 1
    acumulador = acumulador + contador
    if contador % 2 == 0:
    
    contine
    print(f"{contador}- dentro del while")
print("fuera del while")
'''
'''
numero = 3
while numero > 0:
print(f"{numero} dentro del while")
numero = numero - 1
print("fuera del while")



dividendo = 10
divisor = input("ingrse su valor: ")

divisor = int(divisor)

while divisor == 0:
    divisor = input("error! ingrese un valor: ")
    divisor = int(divisor)
resultado = dividendo / divisor
print(f"el resultado es {resultado}")

salir por contiunar = "si"
while conyinuar "si":
    print(primera vez)
continuar = input("desea continuar)
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        variable = prompt("UTN", message="desea continuar?")
        print(variable)
        print(type(variable))
    
        '''
        Me ingresan 5 edades y debo calcular un promedio de edades.
        #los contadores, acumuladores se inicializan en 0.
        
        contador = 0
        acumulador = 0
                #0
    while contador < 5:
        edad_ingresada = prompt("UTN", "Ingrese su edad")
        edad_ingresada = int(edad_ingresada)
        
        #Suma de las edades
        acumulador = acumalador + edad_ingresada
        
        #contador +=1 es lo mismo que abajo.
        contador = contador + 1

                #suma edades / cantidad de edades
    promedio = acumulador / contador
    print(promedio)


    #me ingrsan edades hasta que el usuario quiera y debo calcular un promedio de edades

    contador = 0
    acumulador = 0
    respuesta = True #1, o un string "hola"
    #flag_principal = true

        #flag_principal
    while respuesta == true:
        edad_ingresada = prompt("UTN", "ingrese su edad")
        edad_ingresada = int(edad_ingresada)

        acumulador = acumulador + edad_ingresada

        contador = contador + 1
                    #en vez de "question" podemos usar "prompt" usando si / no.
        
        #si se usa flag se usa if en vez de respuesta
        #if respuesta == false
            #flag_principal = false
        
        respuesta = question("UTN", "Desea seguir ingresando edades?")
    promedio = acumulador / contador
    print(promedio)


    #while edad_ingresada.isdigit() == false
        edad_ingresada = prompt("UTN", promt="reingrsar edad")

        
    otro metodo con if

    while true:
        edad_ingresada = prompt("UTN", prompt="Ingresar edad")
        while edad_ingresada.isdigit() == False:
            edad_ingresada = prompt("UTN", prompt="reingrese su edad")

        edad_ingresada = int(edad_ingresada)
        acumulador = acumulador + edad_ingresada
        contador = contador + 1
        promedio = acumulador / contador
        print(promedio)    
        
        tp 5 si no es un numero usar insdigit()
        
        '''
        
        '''
        contador = 0
        acumulador = 0
        
        while contador < 5:
        edad_ingresada = prompt("UTN", "Ingrese su edad")
        edad_ingresada = int(edad_ingresada)
        
        #Suma de las edades
        acumulador = acumalador + edad_ingresada
        
        #contador +=1 es lo mismo que abajo.
        contador = contador + 1

                #suma edades / cantidad de edades
    promedio = acumulador / contador
    print(promedio)


    #while edad_ingresada < 18 oredad_ingresada > 90:
        edad_ingresada =prompt("UTN", prompt="reingrese su edad")
        edad_ingresada = int(edad_ingrsada)
        '''
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()