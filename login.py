import tkinter as tk
#Colores 
fondo_inicio="#FF3131"


#Ventana de inicio de sesión
def inicio_usuario():

    def salir():
        I_sesion.withdraw()
        ventana.deiconify()

    

    ventana.withdraw()
    I_sesion = tk.Toplevel()  
    I_sesion.title("inicio de usuario")
    I_sesion.geometry("500x500+500+50")
    I_sesion.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file="2.png")
    fondo1 = tk.Label(I_sesion, image=fondo)
    fondo1.place(x=0, y=0, relheight=1, relwidth=1)
    
    usuario=tk.StringVar
    contraseña=tk.StringVar
 #Entrada de usuario y contraseña
    entrada_usuario=tk.Entry(I_sesion,textvariable=usuario,width=22,relief="flat",bg="#D9D9D9")
    entrada_usuario.place(x=215,y=215)
    entrada_contraseña=tk.Entry(I_sesion,show="*",textvariable=contraseña,width=22,relief="flat",bg="#D9D9D9")
    entrada_contraseña.place(x=215,y=280)

    #Botón de entrar y salir
    boton_entrar = tk.Button(I_sesion, text="ENTRAR", cursor="hand2", command=salir , bg="#004AAD", width=12, relief="flat",
                  font=("Open Sans", 13, "bold"))
    boton_entrar.place(x=65, y=390)


    boton_salir = tk.Button(I_sesion,text="SALIR", cursor="hand2",command=salir, bg=fondo_inicio,width=12,relief="flat",
                  font=("Open Sans",13,"bold"))
    boton_salir.place(x=310,y=390)
    


    I_sesion.mainloop()  



#Crear la ventana del menú
ventana = tk.Tk()
ventana.title("Menú")
ventana.geometry("500x500+500+50")
ventana.resizable(width=False, height=False)

#Cargar la imagen de fondo del menú
fondo = tk.PhotoImage(file="1.png")

fondo1 = tk.Label(ventana, image=fondo)
fondo1.place(x=0, y=0, relwidth=1, relheight=1)

#Botones del menú

boton_inicio = tk.Button(ventana, text="INICIO", cursor="hand2", command=inicio_usuario , bg=fondo_inicio, width=12, relief="flat",
                  font=("Open Sans", 13, "bold"))
boton_inicio.place(x=60, y=360)


boton_registro = tk.Button(ventana,text="REGISTRO", cursor="hand2", bg=fondo_inicio,width=12,relief="flat",
                  font=("Open Sans",13,"bold"))
boton_registro.place(x=300,y=360)
ventana.mainloop()


    
    
 
