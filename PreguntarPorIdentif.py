def BusquedaSec(lista, iden): 
    alerta=True
    for i in range(len(lista)-1):
        if lista[i]==iden:
            print(f"El número a buscar se encuentra en la posición: {i}.")
            alerta=False

    if alerta==True:
        print("El número no se encuentra en la lista.")
