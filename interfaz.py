import tkinter 

ventana=tkinter.Tk()
ventana.geometry("500x500")

opcion=tkinter.Label(ventana, text="¿Desea buscar los datos de algún jugador? (si/no): ", bg="blue")
opcion.pack()

#Creamos los botones.

def yes():
    cajaTexto=tkinter.Entry(ventana)
    iden=input("Ingrese el identificador del usuario que desea buscar: ")
    
si=tkinter.Button(ventana, text="Si", command=yes)
si.pack()

def nop():
    print("Está bien, muchas gracias.")

no=tkinter.Button(ventana, text="No", command=nop)
no.pack()

ventana.mainloop()