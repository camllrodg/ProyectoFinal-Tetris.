#Reporte de los datos básicos del jugador.

#Lo primero q tenemos q hacer es leer el archivo binario "Juegos".

def main():

  archivoJuegos=open("JUEGOS.bin", "rb")

  #Supongamos que en el archivo juegos se encuentra en este orden los datos de la partida:
  #1) Código de juego
  #2) Identificador del jugador
  #3) Cantidad de puntos ganados

  linea=archivoJuegos.readline()  #Para leer línea por línea.
  lineaString=linea.decode("utf-8") #La convertimos a string

  FuncReporte(lineaString, archivoJuegos) #Le pasamos el identificador del usuario
  
  archivoJuegos.close()

  #Una vez leído, creamos el reporte.

def FuncReporte(lineaString, archivoJuegos):
  reporte=open("ReporteDatosBasicos", "w")  #Será un archivo txt.

  opcion=input("¿Desea buscar los datos de algún jugador? (si/no): ")
  if opcion=="si":
      iden=input("Ingrese el identificador del usuario que desea buscar: ")

  reporte.write("                                                                          Jugador                                                                            \n")
  reporte.write("Código de Juego                           Puntos ganados                    Fecha                      Hora           \n")
  reporte.write("  *******                                    *********                       ******                    *******                   \n")
  
  while lineaString:  #Con ya tener la variable "linea" un valor, ya de por sí es True.
    listaDatos=lineaString.split("/") #para eliminar la barra. Los datos los colocará en una lista.
    valor=0 
    #Aquí colocamos el condicional 
    valor=BusquedaSec(listaDatos, iden) 
    if valor==1: 
      reporte.write(f" {listaDatos[0]}                         {listaDatos[2]}                       {listaDatos[3]}                        {listaDatos[4]}")  
    lineaString=archivoJuegos.readline() #Inicializamos :).   
    lineaString=lineaString.decode("utf-8")

  reporte.close()

def BusquedaSec(listaDatos, iden):
  if listaDatos[1]==iden:
      return 1

if __name__=="__main__":
  main()