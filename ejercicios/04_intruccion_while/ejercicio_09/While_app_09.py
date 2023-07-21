import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        
        #maximo = 0
        #minimo= 1000
        
        #numero = int(prompt("UTN", "ingresar un numero"))
        #maximo = numero
        #minimo = numero no le copa a german

        maximo = 0
        minimo = 0

        bandera_primer_ingreso = False

        #seguir = True no sirve de nada poner asi
        
        while True: #esto es un bucle infinito 
            #Entradas
            numero = prompt("UTN", "Ingrese un numero")
            #nuermo = int(prompt("UTN", "Ingrese un numero")) #prompt devuelve un string o None
            
            if numero == None:
                break

            numero = int(numero)

            #Procesos: Buscar maximo y minimo.
            
            if bandera_primer_ingreso == False:
                maximo = numero
                maximo = numero
                bandera_primer_ingreso= True
            else:
                if numero > maximo:
                    maximo = numero
                if numero < minimo:
                    minimo = numero 
        
            #############################

            if numero > maximo or bandera_primer_ingreso == False:
                maximo = numero
            if numero < minimo or bandera_primer_ingreso == False:
                minimo = numero
            bandera_primer_ingreso = True    

            #seguir = question("UTN", "Desea seguir?")


        #end while

        #Salida
        self.txt_maximo.delete(0, "end")
        self.txt_maximo.insert(0, str(maximo))

        self.txt_minimo.delete(0, "end")
        self.txt_minimo.insert(0, str(minimo))
        

'''
if numero == None or numero > maximo:
                maximo = numero
            if numero == None or numero < minimo:
                minimo = numero

'''
'''

'''

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
