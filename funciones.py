import pandas as pd
import matplotlib.pyplot as plt
import os
from os import path

def inicio():
    #Solicitar la ruta absoluta de la carpeta con los archivos de inversores
    fileDir = input("Bienvenido, por favor introduzca la ruta absoluta de la carpeta con los archivos de los inversores:  ")
    return fileDir

def Listar_rutas(fileDir):
    #listar las rutas abolutas de los archivos xlxs ubicados en la carpeta especifica
    rutas = [os.path.join(fileDir, _) for _ in os.listdir(fileDir) if _.endswith(r".xlsx")]
    return rutas

def Listar_nombres_archivos(fileDir):
    #lista los nombres del archivo excel de cada inversor
    archivos = [_ for _ in os.listdir(fileDir) if _.endswith(r".xlsx")]
    return archivos

def Leer_archivo(pat):
    #lectura del archivo
    df = pd.read_excel(pat)
    return df

def Eliminar_vacias(df):
    #Eliminar columnas vacias
    for col in df.columns:
        if df[col].nunique()==0:
            del(df[col])
    return df

def Ruta_grafico_name(archivos):
    #Genera la ruta unica para cada grafico
    carpeta = '/graficos/'
    for nombre in archivos:
        nombre_grafico = carpeta + nombre
    return nombre_grafico
    
def Graficar_df(df, pat):   
    name = list(os.path.split(pat))[1]#Genera nombre dinamico del grafico
    #Generar y guardar grafica
    plt.plot(df['fecha_im'], df['active_power_im'], color='black')
    plt.title('Active Power Diario')
    plt.xlabel('fecha')
    plt.ylabel('active power')
    plt.savefig(f'./graficos/inversor_{name}.jpeg', bbox_inches=None)
    #print("Grafico Generado")
    return name

def Obtener_ruta_grafico(name):
    #obtener ruta absoluta de la grafica
    file = open("./vistas.txt", "a")
    imagen = f'./graficos/inversor_{name}.jpeg'
    ruta_grafica = path.abspath(imagen)
    file.write("Ruta de la Grafica:  "+str(ruta_grafica) + os.linesep *2)
    file.close()
    #print("Ruta de grafico guardada en archivo vistas.txt")
    return ruta_grafica

def Crear_vista(df):
    # Crear y guardar vista en txt
    suma_active = int(df['active_power_im'].sum())
    maximo_active  = df['active_energy_im'].max() 
    minimo_active = df['active_energy_im'].min()
    file = open("./vistas.txt", "a")
    file.write(f'suma active power {suma_active}\nmaximo active energy {maximo_active}\nminimo active energy {minimo_active}\n')
    file.close()
    #print("Vista generada")
    return suma_active

def Limpiar_col(df):
    #Eliminar las filas con datos errados
    df = df.drop(df[df['active_power_im']=='data_faltante'].index)
    return df

def Rellenar_nan(df):
    #rellena los datos nan con 0
    df = df.fillna(0)
    return df

def Crear_carpetas_graficos():
    #Crear las carpetas para guardas los graficos
    while(True):
        if os.path.exists("graficos") == True:
            pass
        else: 
            os.mkdir("graficos")
            continue
        break