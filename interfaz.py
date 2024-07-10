try:
    import tkinter  as tk
except ValueError:
    import Tkinter as tk

#Creamos los botones.


def buscador_puntaje():
    ventana=tk.Tk()
    ventana.geometry("500x500")
    opcion=tk.Label(ventana, text="Código de Usuario:", bg="white")
    opcion.place(x=190,y=30)
    cod=tk.StringVar()
    def generar_reporte():
        iden=cod.get()
        def FuncReporte(iden):
            archivoJuegos=open("Downloads/JUEGOS.bin", "rb")
            linea=archivoJuegos.readline()  #Para leer línea por línea.
            lineaString=linea.decode("utf-8") #La convertimos a string
            reporte=open("ReporteDatosBasicos.txt", "w")  #Será un archivo txt.
            bandera=False
            reporte.write("Código de Juego                        Puntos ganados                    Fecha                        Hora           \n")
            while lineaString:  #Con ya tener la variable "linea" un valor, ya de por sí es True.
                listaDatos=lineaString.split("/") #para eliminar la barra. Los datos los colocará en una lista.
                valor=0 
                #Aquí colocamos el condicional 
                valor=BusquedaSec(listaDatos, iden) 
                if valor==1: 
                    bandera=True
                    reporte.write(f"            {listaDatos[0]}                                        {listaDatos[2]}                                     {listaDatos[3]}                               {listaDatos[4]}")  
                lineaString=archivoJuegos.readline() #Inicializamos :).   
                lineaString=lineaString.decode("utf-8")
            reporte.close()
            reporte=open("ReporteDatosBasicos.txt", "r")
            
            if bandera==False:
                cajaTexto.configure(bg="red")
                ventana.after(4000,lambda:[cajaTexto.configure(bg="white")])
            else:
                texto_reporte=tk.Label(text=reporte.read(),justify="left")
                texto_reporte.place(x=10,y=80)
            archivoJuegos.close()
            reporte.close()
        FuncReporte(iden)
    def BusquedaSec(listaDatos, iden):
        if listaDatos[1]==iden:
            return 1
    cajaTexto=tk.Entry(ventana,bg="#d9d9d9",textvariable=cod)
    cajaTexto.place(x=180,y=60)
    buscar=tk.Button(ventana, text="Buscar", command=generar_reporte)
    buscar.place(x=140,y=460)
    salir=tk.Button(ventana, text="Salir", command=lambda:[ventana.destroy()],width=6)
    salir.place(x=320,y=460)

    ventana.mainloop()