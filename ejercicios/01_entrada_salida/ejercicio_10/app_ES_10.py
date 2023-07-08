import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(
            master=self, text="% de Descuento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_descuento = customtkinter.CTkEntry(master=self)
        self.txt_descuento.grid(row=1, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        importe = self.txt_importe.get()
        descuento = self.txt_descuento.get()

        importe = float(importe)
        descuento = float(descuento)

        pago = importe - (importe * (descuento / 100))

        alert("Descuento", f"El importe a pagar era {importe} con el descuento es: {pago:.2f}")

        
        '''
        importe = self.txt_iporte.get()
        importe = float(importe)
        descuento = self.txt_descuento.get()
        descuento = int(descuento)

        importe_descuento = importe - (importe * descuento / 100)
        importe_total = importe - importe_descuento 
        alert("utn", importe_total)
        mensaje = f"Ud debera pagar: {importe_total}. Se aplico un descuento de: {importe_descuento}"
        alert("UTN", mensaje)

        self.txt_total.delete(0, 100)
        
        self.txt_total.delete(0, len(self.txt_importe.get()))
        self.txt_total.delete(0, tkinter.end)
        self.txt_total.delete(0, "end")
        self.txt_total.insert(0, importe_total)
        
        alert("utn", "descuento: {0}".format(importe descuento))
        alert("utn", f"descuento: {importe_descuento}")
        '''


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
