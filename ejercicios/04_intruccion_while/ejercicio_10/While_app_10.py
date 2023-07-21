import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        acumulador_negativo = 0
        acumulador_positivo = 0
        
        contador_positivos = 0
        contador_negativos = 0

        conatdor_ceros = 0


        while True:
            numero = prompt("UTN", "Ingresa numero")
            if numero == None:
                break
                
            numero = int(numero)

            if numero < 0:
                acumulador_negativo += numero
                contador_negativos += 1
            else:
                if numero > 0:
                    acumulador_positivo += numero
                    contador_positivos += 1
                else:
                    conatdor_ceros += 1

        #end while
        
        diferencia = contador_negativos - contador_positivos
        if diferencia < 0:
            
            diferencia = diferencia * (-1)
            mensaje = diferencia
        alert("UTN", f"La suma acumulada de los negativos es: {acumulador_negativo} \n La acumulacion de los numeros positivos es: {acumulador_positivo} \n La diferencia seria {mensaje}")

        #abs()

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
