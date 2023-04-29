import meteodatos as mtd

mtd.leer_archivo('330075_202303_temperatura.csv')

def filtrar_dia(datos, dia):
    # datos: una lista cuyas filas contienen los datos agrupados como una cadena de texto
    # dia:   el día que se desea filtrar, en formato 'AAAA-MM-DD', ejemplo: '2023-03-01'
    # retorna: la misma lista 'datos', pero conteniendo únicamente las filas
    #          que coinciden con 'dia' y manteniendo la cabecera
    
    # TODO: Escriba su código aquí
    # ---------------------------------------------

    # ---------------------------------------------
    
    return []  # reemplace la lista vacía [] por el resultado de su código


def estadisticas_dia(datos, dia):
    # datos: una lista con datos leidos desde la base de datos meteorológicos,
    #        mediante la función 'leer_archivo()'
    # dia:   el día que se desea reportar, en formato 'AAAA-MM-DD', ejemplo: '2023-03-01'
    # retorna: tmax, tmin, tmedia, la temperatura máxima, mínima y promedio para el día.
    tmax = tmin = tmedia = 0
    
    # TODO: Escriba su código aquí
    # ---------------------------------------------

    # ---------------------------------------------
    # Su código termina aquí, luego se retornan los datos calculados
    
    return tmax, tmin, tmedia
    
  