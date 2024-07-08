def main():
    #Abrimos el archivo binario.
    archivo=open("JUEGOS.bin", "rb")

    opcion=input("¿Desea buscar los datos de algún jugador? (si/no): ")
    if opcion=="si":
        iden=input("Ingrese el identificador del usuario que desea buscar: ")
    
    linea=archivo.readline()  #Para leer línea por línea.
    lineaString=linea.decode("utf-8") #La convertimos a string
    
    while lineaString: 
        valor=BusquedaSec(lineaString, iden)
        linea=archivo.readline()
        lineaString=linea.decode("utf-8") #Inicializamos
    archivo.close()  

def BusquedaSec(lineaString, iden):
    lineaString=lineaString.split("/")
    for i in range(len(lineaString)-1):
       if lineaString[i]==iden:
           print("i") #En esta parte es donde se imprimen los datos del usuario. Se encuentra en el archivo "ReporteDatosBasicos"
       else:
            False
            
if __name__=="__main__":
    main()
