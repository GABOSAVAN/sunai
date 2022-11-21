import funciones

def main():

    fileDir = funciones.inicio()
    
    rutas = funciones.Listar_rutas(fileDir)

    energia_diaria = []

    for pat in rutas:    
        df = funciones.Leer_archivo(pat)
      
        df = funciones.Eliminar_vacias(df)
    
        df = funciones.Rellenar_nan(df)

        df = funciones.Limpiar_col(df)   

        funciones.Crear_carpetas_graficos()

        name = funciones.Graficar_df(df, pat)

        suma_active = funciones.Crear_vista(df)
        energia_diaria.append(suma_active)

        funciones.Obtener_ruta_grafico(name)

    #funciones.Energia_diaria(energia_diaria)

    print(f'\nSuma Total de Active Power de todas las plantas: {sum(energia_diaria)}\n')
    print('Proceso culminado exitosamente!!!\nEl archivo txt y la carpeta con las graficas \nquedo guardado en su capeta de ejecucion')  

main()