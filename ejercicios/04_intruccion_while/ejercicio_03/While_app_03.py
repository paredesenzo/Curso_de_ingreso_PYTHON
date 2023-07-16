import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volverla a solicitar hasta que coincidan
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        clave_ingresada = prompt("UTN", "ingrese su contraseña")

        while clave_ingresada != "utn750":
            clave_ingresada = prompt("UTN", "Reingrese su contraseña")
            

        alert("UTN", "Se ha ingresado con exito")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    como se busca un maximo?

    contador = 0
    acumulador_notas = 0
    nota_maxima = None # "0" mal
    nota_minima = none

    while contador < 5:
        #nombre = prompt("UTN", "Ingrese el nombre del alumno")
        nota = prompt("UTN", "ingrsar nota")
        nota = int(nota)
        #genero_ingresado = prompt("UTN", "ingrese el genero del alumno "M" / "F")

        if genero_ingresado == "M"
        if nota_maxima == None or nota_maxima < nota:
        nota_maxima = nota

        if nota_minima == none or nota_minima > nota
        nota_minima = nota

        contador += 1
        acumulador_notas = acumulador_notas + nota

    promedio = acumulador_notas / contador

    alert("UTN", f"El promedio de las notas es: {promedio} \n La nota mas alta es: {nota_maxima} y la nota minima es: {nota_minima}")

    '''
    '''
    cantidad_perros = 5
    cantidad_gatos = 3
    cantidad_loros = 7

    if cantidad_perros > cantidad_gatos and cantidad_perros > cantidad_loros:
        print("Fueron mas perros que gatos y loros")
    elif cantidad_loros > cantidad_loros
        print("Fueron mas loros que gatos y perros)
    else:
        print("Fueron mas gatos que perros y loros)
    '''
    '''
    Bandera o flag es un concepto

    '''

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()