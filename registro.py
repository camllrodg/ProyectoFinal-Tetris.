try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

import re#verificador email

def registro():
    # BASE DE VENTANA Y FONDO
    raiz= tk.Tk()
    raiz.geometry("400x500+500+50")
    raiz.resizable(width=False, height=False)
    raiz.title("Registro")
    fondoreg= tk.PhotoImage(file= "fondoregistro.png")
    fondoreg1= tk.Label(raiz, image=fondoreg)
    fondoreg1.place(x=0, y=0, relwidth=1, relheight=1)
    bienvenida= tk.Label(raiz, text="Crea una cuenta de Tetris",bg="#FFFFFF",font=("Arial.ttf, 16"))
    bienvenida.place(x=70,y=20)
    # CASILLAS DE TEXTO
    nombreaux= tk.StringVar()
    contrasenaaux= tk.StringVar()
    emailaux= tk.StringVar()
    estadoaux= tk.StringVar()
    codigoaux= tk.IntVar()
    
    def guardar_jugadores(nombre,contrasena,email,estado,codigo):
        jugadores=open("JUGADORES.dat","ab")
        jugadores.write(nombre.encode('utf-8'))
        jugadores.write(b"#")
        jugadores.write(contrasena.encode('utf-8'))
        jugadores.write(b"#")
        jugadores.write(email.encode('utf-8'))
        jugadores.write(b"#")
        jugadores.write(estado.encode('utf-8'))
        jugadores.write(b"#")
        codigo=str(codigo)
        jugadores.write(codigo.encode('utf-8'))
        jugadores.write(b"\n")
        jugadores.close()
        
    def subir_registro():
        nombre = nombreaux.get()
        contrasena= contrasenaaux.get()
        email= emailaux.get()
        estado = estadoaux.get()
        codigo= codigoaux.get()
        if (nombre and estado and email and contrasena and codigo != ""):
            analisis= verificar_registro(nombre,contrasena,email,codigo)
            if analisis==True:
                return guardar_jugadores(nombre,contrasena,email,estado,codigo), raiz.destroy() #Junto a inicio del juego
            if analisis==False:
                return None
        else:
            errorcasillas= tk.Label(raiz, text="Por favor, rellene todas las casillas")
            errorcasillas.place(x=90,y=380)
            raiz.after(5000,errorcasillas.destroy)
            return

        
    def verificar_registro(nombre,contrasena,email,codigo):

        def verificar_recurrencia(codigo):
            codigo=str(codigo)
            temp_codigo=""
            for i in range (4):
                temp_codigo+= str(codigo[i])
            temp_codigo+="\n"
            temp_codigo= temp_codigo.encode('utf-8')
            try:
                jugadores=open("JUGADORES.dat","rb")
                encontrado=False
                for linea in jugadores:
                    campo=linea.split(b"#")
                    if campo[4]==temp_codigo:
                        encontrado=True
                        if encontrado==True:
                            errorcodigo= tk.Label(raiz, text="* Código ingresado ya existente.",bg="#FFFFFF",font="console, 9",fg="#F50743")
                            errorcodigo.place(x=90,y=302)
                            raiz.after(5000,errorcodigo.destroy)
                            return False
                if encontrado==False:
                    return True
            except FileNotFoundError:
                return True


        def verificar_codigo(codigo):
            codigo=str(codigo)
            if len(codigo) > 4:
                casillacodigo.configure(bg="#F50743")
                return False
            elif len(codigo)<4:
                casillacodigo.configure(bg="#F50743")
                return False
            else:
                repetido= verificar_recurrencia(codigo)
                if repetido==False:
                    casillacodigo.configure(bg="#F50743")
                    return False
                else:
                    casillacodigo.configure(bg="#8efd99")
                    return True
            
        def verificar_nombre(nombre):
            if nombre.isalpha()==True:
                if len(nombre)<16:
                    casillanombre.configure(bg="#8efd99")
                    return True
                else:
                    casillanombre.configure(bg="#F50743")
                    return False
            else:
                casillanombre.configure(bg="#F50743")
                return False


        def verificar_contrasena(contrasena,caracter,i,conta,errores):
            if len(contrasena)>=8 and len(contrasena)<=10:
                if i<len(contrasena):
                    error_ñ=False
                    error_repetidos=False
                    error_especiales=False
                    caracteraux=caracter
                    caracter=contrasena[i]
                    if caracter==caracteraux:
                        conta+=1
                        if conta>3:
                            error_repetidos=True
                    if (caracter.isalpha()==True):
                        if caracter=="ñ" or caracter=="Ñ":
                            error_ñ= True
                    if caracter!="-" and caracter!="*" and caracter!="." and (caracter.isalpha()==False):
                        error_especiales= True
                    i+=1
                    erroresaux=errores or(error_repetidos or error_ñ or error_especiales)
                    return verificar_contrasena(contrasena,caracter,i,conta,erroresaux)
                else:
                    if errores==True:
                        casillacontrasena.configure(bg="#F50743")
                        return False
                    else:
                        casillacontrasena.configure(bg="#8efd99")
                        return True
            else:
                casillacontrasena.configure(bg="#F50743")
                return False

        def verificar_email(email):
            patron_email= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-0.-]+\.[a-zA-Z]{2,}$'
            if re.match(patron_email,email):
                casillaemail.configure(bg="#8efd99")
                return True
            else:
                casillaemail.configure(bg="#F50743")
                return False
        resultado= verificar_codigo(codigo) * verificar_nombre(nombre) * verificar_contrasena(contrasena,"\0",0,0,False)* verificar_email(email)
        return resultado





    def requisitos_contrasena():
        raizaux=tk.Tk()
        raizaux.geometry("220x200+600+300")
        raizaux.resizable(width=False, height=False)
        raizaux.title("Requisitos contraseña")
        titulo= tk.Label(raizaux,text="Requisitos:")
        titulo.place(x=80,y=10)
        texto= tk.Label(raizaux,justify="left",
                        text=
                        "*No debe llevar la letra Ñ. \n*Simbolos especiales permitidos:\n ( * ), ( - ), [ . ]\n*Tamaño entre 8 a 10 caracteres.\n*No puede tener el mismo caracter\nrepetido más de 4 veces",font="console, 9")
        texto.place(x=0,y=30)
        raizaux.mainloop()
        
    indicadornombre= tk.Label(raiz, text="Nombre de usuario:",bg="#FFFFFF")
    indicadornombre.place(x=30,y=70)
    casillanombre = tk.Entry(raiz, textvariable = nombreaux,bg="#dcdcdc")
    casillanombre.place(x=30,y=90)
    ayudanombre=tk.Label(raiz, text="* Máximo 16 caracteres\n usar únicamente letras",bg="#FFFFFF",font="console, 9",fg="#246eea")
    ayudanombre.place(x=180,y=86)

    indicadorcontrasena= tk.Label(raiz, text="Contraseña:",bg="#FFFFFF")
    indicadorcontrasena.place(x=30,y=120)
    casillacontrasena=tk.Entry(raiz,textvariable =contrasenaaux, show= "•",bg="#dcdcdc")
    casillacontrasena.place(x=30,y=140)
    ayudacontrasena=tk.Button(raiz, text="Pulse aquí para ver los criterios\n de contraseña",command=requisitos_contrasena,bg="#FFFFFF")
    ayudacontrasena.place(x=180,y=130)
    

    indicadoremail= tk.Label(raiz, text="Correo electrónico:",bg="#FFFFFF")
    indicadoremail.place(x=30,y=170)
    casillaemail=tk.Entry(raiz,textvariable =emailaux,bg="#dcdcdc")
    casillaemail.place(x=30,y=190)
    ayudaemail=tk.Label(raiz, text="* ejemplo@email.com",bg="#FFFFFF",font="console, 9",fg="#246eea")
    ayudaemail.place(x=180,y=186)
    
    indicadorcodigo= tk.Label(raiz, text="Código de usuario:",bg="#FFFFFF")
    indicadorcodigo.place(x=30,y=260)
    casillacodigo= tk.Entry(raiz, textvariable=codigoaux, width= 4,bg="#dcdcdc")
    casillacodigo.place(x=60,y=282)
    ayudacodigo=tk.Label(raiz, text="* 4 números enteros",bg="#FFFFFF",font="console, 9",fg="#246eea")
    ayudacodigo.place(x=90,y=282)
    # BOTONES Y FUNCIONES
    indicadorestado=tk.Label(raiz, text="Seleccione su estado de procedencia:",bg="#FFFFFF")
    indicadorestado.place(x=30,y=210)
    seleccion_estado=ttk.Combobox(raiz,state="readonly",textvariable= estadoaux,)
    seleccion_estado['values']= ("Amazonas", "Anzoátegui", "Apure", "Aragua", "Barinas", "Bolívar", "Carabobo", "Cojedes",
                                   "Delta Amacuro", "Distrito Capital", "Falcón", "Guárico","Islas Federales", "La Guaira", "Lara",
                                   "Mérida", "Miranda", "Monagas", "Nueva Esparta", "Portuguesa", "Sucre", "Táchira",
                                   "Trujillo", "Yaracuy", "Zulia")
    seleccion_estado.place(x=30,y=235)

    
    ingresar = tk.Button(raiz, text="Ingresar", activebackground="#F50743",height=2, command=subir_registro)
    ingresar.place(x=255, y=430)
    regresar = tk.Button(raiz, text="Regresar", activebackground="#F50743", height=2, command=raiz.destroy)
    regresar.place(x=88, y=430)
    #BUCLE DE ACTUALIZACIÓN
    raiz.mainloop()
registro()
