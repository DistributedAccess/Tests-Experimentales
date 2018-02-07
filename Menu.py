from time import sleep
import os
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def Inicio():
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t\t\t\t{0}MENU PRINCIPAL\n').format(GREEN)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}Configure las opciones del Menu:\n\n').format(WHITE)
    sleep(0.2)
    print('''\t\t\t\t\t{0}[{1}1{2}]{3} Deteccion Normal:         {4}Realiza la deteccion de rostros con los algoritmos de: EigenFaces,
             \t\t\t\t\t\t              FisherFaces y LBPH sobre una base de datos de determinada. Se modifican parametros como:
             \t\t\t\t\t\t              Porcentaje de Entrenamiento, Componentes, Umbral y Detector de Rostros. Se obtienen mapas
             \t\t\t\t\t\t              de confusion normalizadas por cada algoritmo de reconocimiento\n''').format(YELLOW, RED, YELLOW, WHITE, GREEN)
    sleep(0.2)
    print('''\n\t\t\t\t\t{0}[{1}2{2}]{3} Deteccion Ruido:          {4}Realiza la deteccion de rostros con los algoritmos de: EigenFaces,
             \t\t\t\t\t\t              FisherFaces y LBPH sobre una base de datos totalmente desconocida a la base de datos de
             \t\t\t\t\t\t              que se utilizo para el entrenamiento. Se modifican parametros como: Porcentaje de
             \t\t\t\t\t\t              Entrenamiento, Componentes, Umbral y Detector de Rostros. Se obtienen mapas una lista de
             \t\t\t\t\t\t              de los resultados de la Prediccion\n''').format(YELLOW, RED, YELLOW, WHITE, GREEN)
    sleep(0.2)
    print('''\n\t\t\t\t\t{0}[{1}3{2}]{3} Deteccion Experimental:   {4}Realiza la deteccion de rostros con los algoritmos de: EigenFaces,
             \t\t\t\t\t\t              FisherFaces y LBPH sobre una base de datos determinada. A exepcion de las detecciones anterioes
             \t\t\t\t\t\t              esta opcion se encarga de realizar una deteccion general del 10'%'-90'%' de la base de Datos
             \t\t\t\t\t\t              escogida almacenando los mapas de confusion por cada algoritmo y porcentaje, ademas de una
             \t\t\t\t\t\t              grafica del rendimiento por algoritmo en la deteccion.''').format(YELLOW, RED, YELLOW, WHITE, GREEN)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}E{2}]{3} Salir\n\n\n').format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    etiqueta = ('\t\t\t\t\t{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Op

def Normal(Opciones):
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t\t\t\t{0}DETECCION NORMAL\n').format(GREEN)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}Configure las opciones del Menu:\n\n').format(WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}1{2}]{3} Escojer Base de Datos..................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[0])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}2{2}]{3} Escojer Porcentaje.....................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[1])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}3{2}]{3} Escojer Clasifcador....................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[2])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}4{2}]{3} Configurar Umbral......................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[3])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}5{2}]{3} Configurar Componentes.................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[4])
    sleep(0.2)
    print("\n\t\t\t\t\t{0}[{1}6{2}]{3} Let's Rock {4}(Comenzar Prediccion)").format(YELLOW, RED, YELLOW, RED,WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}E{2}]{3} Regresar al Menu Principal\n\n\n').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('\t\t\t\t\t{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Op

def Ruido(Opciones):
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t\t\t\t{0}DETECCION RUIDO\n').format(GREEN)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}Escoja una opcion del Menu:\n\n').format(WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}1{2}]{3} Escojer Base de Datos..................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[0])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}2{2}]{3} Escojer Base de Datos Desconocida......................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[1])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}3{2}]{3} Escojer Porcentaje.....................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[2])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}4{2}]{3} Escojer Clasifcador....................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[3])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}5{2}]{3} Configurar Umbral......................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[4])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}6{2}]{3} Configurar Componentes.................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[5])
    sleep(0.2)
    print("\n\t\t\t\t\t{0}[{1}7{2}]{3} Let's Rock {4}(Comenzar Prediccion)").format(YELLOW, RED, YELLOW, RED, WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}E{2}]{3} Regresar al Menu Principal\n\n\n').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('\t\t\t\t\t{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Op

def Experimento(Opciones):
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t\t\t\t{0}PRUEBA EXPERIMENTAL\n').format(GREEN)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}Configure las opciones del Menu:\n\n').format(WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}1{2}]{3} Escojer Base de Datos..................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[0])
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}2{2}]{3} Escojer Clasifcador....................................................{4}{5}').format(YELLOW, RED, YELLOW, WHITE, GREEN, Opciones[1])
    sleep(0.2)
    print("\n\t\t\t\t\t{0}[{1}3{2}]{3} Let's Rock {4}(Comenzar Prediccion)").format(YELLOW, RED, YELLOW, RED, WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}E{2}]{3} Regresar al Menu Principal\n\n\n').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('\t\t\t\t\t{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Op

def Base_Datos():
    os.system("clear||cls")
    Dir = next(os.walk('/home/verriva/Detection_Recognition'))[1]
    print('\n\t\t\t\t\t\t\t\t\t\t{0}Escoja una Base de Datos \n\n\n\n').format(GREEN)
    Cont = 0
    for N_Dir in Dir:
        sleep(0.2)
        print('\n\t\t\t\t\t{0}[{1}{5}{2}]{3} Base de Datos {4}').format(YELLOW, RED, YELLOW, WHITE, N_Dir, Cont)
        Cont = Cont + 1
    sleep(0.2)
    #print('\t{0}[{1}E{2}]{3} Regresar al Menu Principal\n').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('\n\t\t\t\t\t{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Dir[int(Op)]

def Porcentaje():
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t{0}Del 1 al 100 escriba el porcentaje de imagenes que utilizara para el Entrenamiento \n\n\n\n').format(GREEN)
    print('\n\t\t\t\t\t\t\t{0}NOTA: El porcentaje restante sera utilizado en la Prediccion \n').format(GREEN)

    etiqueta = ('\n\t\t\t\t\t\t\t{0}Porcentaje{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)

def Clasifcador():
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t\t\t\t{0}Escoja un clasificador').format(GREEN)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}2{2}]{3} Haar Cascade').format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    print('\n\t\t\t\t\t{0}[{1}3{2}]{3} Local Binary Pattern LBP').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('\n\t\t\t\t\t{0}Clasifcador{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)

def Umbral():
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t\t\t{0}Ingrese el Umbral a Utilizar en la Deteccion').format(GREEN)

    etiqueta = ('\n\t\t\t\t\t{0}Umbral{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)

def Componentes():
    os.system("clear||cls")
    print('\n\t\t\t\t\t\t\t{0}Ingrese el numero de Componentes a Utilizar en EigenFace y FisherFace').format(GREEN)

    etiqueta = ('\n\t\t\t\t\t{0}Componentes{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)
