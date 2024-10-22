import tkinter as tk
#colores 
fondo_inicio="#FF3131"
#ventana de eleccion de los modos de juego
def Modos_juegos():

   # configuracion de la pantalla
    ventana.withdraw()
    modos = tk.Toplevel()  
    modos.title("Modos de Juego")
    modos.geometry("500x500+500+50")
    modos.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file="modos.png")
    fondo1 = tk.Label(modos, image=fondo)
    fondo1.place(x=0, y=0, relheight=1, relwidth=1)
    
    
 

    #botones de eleccion de modo
    boton_movimiento = tk.Button(modos, text="Por Movimiento",command="", cursor="hand2", bg="#004AAD", width=12, relief="flat",
                  font=("Open Sans", 14, "bold"))
    boton_movimiento.place(x=70, y=380)


    boton_tiempo = tk.Button(modos,text="Por Tiempo",command="" , cursor="hand2", bg="#004AAD",width=12,relief="flat",
                  font=("Open Sans",14,"bold"))
    boton_tiempo.place(x=280,y=380)
    


    modos.mainloop()  

#ventana de inicio de session
def inicio_usuario():

    def salir():
        I_sesion.withdraw()
        ventana.deiconify()




    ventana.withdraw()
    I_sesion = tk.Toplevel()  
    I_sesion.title("inicio de usuario")
    I_sesion.geometry("500x500+500+50")
    I_sesion.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file="login.png")
    fondo1 = tk.Label(I_sesion, image=fondo)
    fondo1.place(x=0, y=0, relheight=1, relwidth=1)
    
    usuario=tk.StringVar
    contraseña=tk.StringVar
 #entrada de usuario y contraseña
    entrada_usuario=tk.Entry(I_sesion,textvariable=usuario,width=22,relief="flat",bg="#D9D9D9")
    entrada_usuario.place(x=215,y=215)
    entrada_contraseña=tk.Entry(I_sesion,show="*",textvariable=contraseña,width=22,relief="flat",bg="#D9D9D9")
    entrada_contraseña.place(x=215,y=280)

    #boton de entar y salir
    boton_entrar = tk.Button(I_sesion, text="ENTRAR", cursor="hand2", command=Modos_juegos , bg="#004AAD", width=12, relief="flat",
                  font=("Open Sans", 13, "bold"))
    boton_entrar.place(x=65, y=390)


    boton_salir = tk.Button(I_sesion,text="SALIR", cursor="hand2",command=salir, bg=fondo_inicio,width=12,relief="flat",
                  font=("Open Sans",13,"bold"))
    boton_salir.place(x=310,y=390)
    
    I_sesion.mainloop()  





# Crear la ventana del menu
ventana = tk.Tk()
ventana.title("Menu")
ventana.geometry("500x500+500+50")
ventana.resizable(width=False, height=False)

# Cargar la imagen de fondo del menu
fondo = tk.PhotoImage(file="menu.png")

fondo1 = tk.Label(ventana, image=fondo)
fondo1.place(x=0, y=0, relwidth=1, relheight=1)

#botones del menu

boton_inicio = tk.Button(ventana, text="INICIO", cursor="hand2", command=inicio_usuario , bg=fondo_inicio, width=12, relief="flat",
                  font=("Open Sans", 13, "bold"))
boton_inicio.place(x=60, y=360)


boton_registro = tk.Button(ventana,text="REGISTRO", cursor="hand2", bg=fondo_inicio,width=12,relief="flat",
                  font=("Open Sans",13,"bold"))
boton_registro.place(x=298,y=360)
ventana.mainloop()
 
