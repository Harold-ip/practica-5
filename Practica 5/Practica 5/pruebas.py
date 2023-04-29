def filtrar_dia(datos, dia):
    datos_filtrados = []
    for fila in datos:
        if dia in fila:
            datos_filtrados.append(fila)
    return datos_filtrados

def filtrar_cabecera(datos, cabecera):
    cabecera_filtrada = []
    for fila in datos:
        if cabecera in fila:
            cabecera_filtrada.append(fila)
    return cabecera_filtrada

def estadisticas_dia(datos, dia):
    datos_filtrados = filtrar_dia(datos, dia)
    cabecera_filtrada = filtrar_cabecera(datos, 'ts')
    indice_temperatura_superficie = cabecera_filtrada[0].index('ts')
    temperaturas = []
    for fila in datos_filtrados[1:]:
        temperaturas.append(float(fila[indice_temperatura_superficie]))
    maximo = max(temperaturas)
    minimo = min(temperaturas)
    promedio = round(sum(temperaturas) / len(temperaturas), 1)
    return (minimo, maximo, promedio)


dia = '2023-04-27'
datos_filtrados = filtrar_dia(datos, dia)
print('Datos filtrados para el día', dia)
for fila in datos_filtrados:
    print(fila)





estadisticas = estadisticas_dia(datos, dia)
print('Estadísticas diarias para el día', dia)
print('Temperatura mínima:', estadisticas[0])
print('Temperatura máxima:', estadisticas[1])
print('Temperatura promedio:', estadisticas[2])



def filtrar_cabecera(datos, filtro):
    # datos: la lista con los datos leidos desde el archivo csv
    # filtro: una variable 'str' con el nombre de cabecera que se desea filtrar
    # retorna: una lista con todas las filas de 'datos', pero conteniendo únicamente los datos bajo el nombre 'filtro'.
    #          Los datos que representan números están en formato numérico correspondiente (int o float)
    index = datos_registrados(datos).index(filtro)
    datos_filtrados = []
    for fila in datos:
        valor = fila.split(';')[index]
        if valor.isnumeric():
            valor = int(valor)
        else:
            try:
                valor = float(valor)
            except:
                pass

        datos_filtrados.append(valor)
    return datos_filtrados


#Prueba 1 para estadisticas dia
    datos_temp = []
    tmax = []
    tmin = []
    tmedia = []
    datos_archivo = leer_archivo('330075_202303_Temperatura.csv')
    index = datos_registrados(datos_archivo).index('ts')
    temp_max = filtrar_dia(datos_archivo,dia)
    temp_min = filtrar_dia(datos_archivo,dia)

    for linea in datos:
        if dia in datos_archivo:
            if dia in linea:
                datos_temp.append(linea)
            if temp_max.isnumeric():
                tmax.append(linea)
            if temp_min.isnumeric():
                tmin.append(linea)

#Pruebas para las estadisticas_dia
def estadisticas_dia(datos, dia):
    # Buscamos las posiciones de las columnas que nos interesan
    cabecera = datos[0]
    fecha_idx = cabecera.index('fecha')
    temp_max_idx = cabecera.index('tmax')
    temp_min_idx = cabecera.index('tmin')
    
    # Filtramos las filas que corresponden al día buscado
    filas_filtradas = [fila for fila in datos[1:] if fila[fecha_idx] == dia]
    
    # Calculamos las estadísticas
    n = len(filas_filtradas)
    if n > 0:
        temp_max = max(float(fila[temp_max_idx]) for fila in filas_filtradas)
        temp_min = min(float(fila[temp_min_idx]) for fila in filas_filtradas)
        temp_media = sum(float(fila[temp_max_idx]) for fila in filas_filtradas) / n
    else:
        temp_max = temp_min = temp_media = None
        
    return temp_max, temp_min, temp_media

tmax, tmin, tmedia = estadisticas_dia(datos, '2023-04-27')
