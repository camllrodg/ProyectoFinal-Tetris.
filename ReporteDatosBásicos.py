#reporte de los datos básicos del jugador.

#Lo primero q tenemos q hacer es leer el archivo binario "Juegos".

def main():
  archivoJuegos=open("JUEGOS", "rb")

  #Supongamos que en el archivo juegos se encuentra en este orden los datos de la partida:
  #1) Código de juego
  #2) Identificador del jugador
  #3) Cantidad de puntos ganados

  linea=archivoJuegos.readline()  #Para leer línea por línea.
  lineaString=linea.decode("utf-8") #La convertimos a string

  FuncReporte(linea)
  
  archivoJuegos.close()

  #Una vez leído, creamos el reporte.

def FuncReporte(lineaString, archivoJuegos):
  reporte=open("ReporteDatosBasicos", "w")  #Será un archivo txt.

  reporte.write("                                             Jugadores                                                 \n")
  reporte.write("Código de Juego                             Identificador                               Puntos ganados  \n")
  reporte.write("*******                                        ******                                     *********           \n")

  while lineaString:  #Con ya tener la variable "linea" un valor, ya de por sí es True.
    listaDatos=lineaString.split("/") #para eliminar la barra. Los datos los colocará en una lista. MODIFICAR.
    reporte.write(f"{listaDatos[0]}                      {listaDatos[1]}                               {listaDatos[4]}         ")
    lineaString=archivoJuegos.readline() #Inicializamos :).

  reporte.close()

if __name__=="__main__":
  main()