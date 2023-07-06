
#FORMATO GENERADO POR REDES NEURONALES
#clases = {"Anorak":[120,40,90]}
#atributos = {120:[0,1,1,1,0,0,1],40:[1,0,1,0,1,1,0],70:[1,0,1,0,1,1,0],90:[1,0,1,1,1,0,0]}

def imagenesSimilares(clases,atributos):

    #write in a new csv file with colums id and Expected
    archivo = open("similitudes.csv","w")
    archivo.write("Id,Expected\n")

    for clase in clases.keys():
        ids_clase = clases[clase]

        for id_busqueda in ids_clase:
            if id_busqueda != 8782 and id_busqueda != 45571 and id_busqueda != 54157:
                similitudes = buscarSimilitud(id_busqueda,ids_clase,atributos) #FUNCION QUE DEVUELVE 100 IMAGENES MAS SIMILARES
                similitudesSTR = " ".join(str(x) for x in similitudes)
                archivo.write(str(id_busqueda) + "," + similitudesSTR + "\n")
    archivo.close()            

def posicionesDondeHayUnos(lista):
    posiciones =[]
    for i in range(0,len(lista)):
        if lista[i] == 1:
            posiciones.append(i)
    return posiciones

def cantidadDeUnos(posiciones, lista):
    cantidad = 0
    for pos in posiciones:
        if lista[pos] == 1:
            cantidad += 1
    return cantidad

def buscarSimilitud(id_busqueda,ids_clase,atributos):
    similitud = {}
    posAtributosImagen = posicionesDondeHayUnos(atributos[id_busqueda])

    for id_imagen in ids_clase:
        if id_imagen != id_busqueda:
            similitud[id_imagen] = cantidadDeUnos(posAtributosImagen,atributos[id_imagen])
        
    similitud = dict(sorted(similitud.items(), key=lambda item: item[1], reverse=True))
    lista_similitud = list(similitud)
    if len(lista_similitud) > 100:
        lista_similitud = lista_similitud[:100]
    else:
        print("LA CLASE ES MUY CHICA, LLENAR")

    return lista_similitud

#imagenesSimilares(clases,atributos)