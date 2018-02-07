from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from natsort import natsorted
import Reconocimiento
import numpy as np
import Deteccion
import random
import Matrix
import Menu
import time
import cv2
import os

def Preparar_Directorios(Directorios, Porcentaje, Detect_Op):
    """   Esta funcion se encarga de leer las imagenes que se encuentran
        en cada uno de los directorios que pertenezcan al directorio de
        entrada "Directorio" y retornar dos arrays, cada array contiene
        imagenes o rostros con sus respectivas clases o etiquetas.

        El argumento Porcentaje debera recibir un numero entre el 1 y el
        100, que represente el porcentaje de 1-100%  de imagenes a utlizar
        por SubDirectorio en el entrenamiento, el resto de imagenes se
        utilizaran en la prediccion.

        Este algoritmo escoje a las imagenes de forma aleatoria. Cada
        array corresponde al grupo de imagenes y etiquetas que se ocuparan
        en el entrenamiento y la prediccion.   """

    Directorio = os.listdir(Directorios)    #   Lista de los Directorios dentro de Directorios

    Directorio = natsorted(Directorio)      #   Ordenamos los Directorios

    Entrenamiento = []  #   Este array se retornara para el Entrenamiento
    Prediccion    = []  #   Este array se retornara para la Prediccion

    FaceE = []  #   En este array se guardaran los rostros de cada usuario para el entrenamiento
    LabeE = []  #   En este array se guardara el numero de directorio para el entrenamiento

    FaceP = []  #   En este array se guardaran los rostros de cada usuario para la prediccion
    LabeP = []  #   En este array se guardara el numero de directorio para la prediccion

    #   Se leera cada directorio y las imagenes en cada uno
    for Nombre_Directorio in Directorio:

        #   Si no hay ningun directorio que comienze con U
        #   el programa se cerrara
        if not Nombre_Directorio.startswith("U"):
            continue;


        etiqueta = int(Nombre_Directorio.replace("U", ""))      #   Se guardara el numero de U, eg U2 -->2
        SubDirectorio = Directorios + "/" + Nombre_Directorio   #   Directorios/U1, Directorios/U2...

        Imagenes = os.listdir(SubDirectorio)    #   Lista de las imagenes dentro del Subdirectorio U'n'...

        #print SubDirectorio
        I_E = len(Imagenes)
        I_E = round((I_E)*(Porcentaje/100.0))

        Contador = 0

        #   Se leera cada imagen en el SubDirectorio aleatoriamente
        random.shuffle(Imagenes)            #   Con esta linea nos aseguramos de tener imagenes aleatoriamente
        for Nombre_Imagen in Imagenes:

            SubImagen = SubDirectorio + "/" + Nombre_Imagen     #   Directorios/U1/1.jpg, Directorios/U1/2.jpg...
            #print Nombre_Imagen
            Image = SubImagen

            #   Detectamos el Rostro segun Detect_Op, puede ser: Haar cascades o LBP.
            if(Detect_Op == 1):
                rostro = Deteccion.Deteccion_Haar(Image)    #   Detector Haar Cascade
            else:
                rostro = Deteccion.Deteccion_LBP(Image)     #   Detector LBP

            #   Si se detecto un rostro este se concatenara al array
            #   faces y se le asigna al array labels correspondiente
            if rostro is not None:

                if Contador < I_E:
                    FaceE.append(np.asarray(rostro, dtype=np.uint8))
                    LabeE.append(etiqueta)
                    Contador = Contador + 1
                    #print Contador
                elif Contador >= I_E:
                    FaceP.append(np.asarray(rostro, dtype=np.uint8))
                    LabeP.append(etiqueta)

    Entrenamiento = [FaceE, LabeE]
    Prediccion = [FaceP, LabeP]

    return Entrenamiento, Prediccion

def Preparar_Ruido(Directorios, Detect_Op):

    Directorio = os.listdir(Directorios)    #   Lista de los Directorios dentro de Directorios

    Directorio = natsorted(Directorio)      #   Ordenamos los Directorios

    Entrenamiento = []  #   Este array se retornara para el Entrenamiento

    Face = []  #   En este array se guardaran los rostros de cada usuario para el entrenamiento

    #   Se leera cada directorio y las imagenes en cada uno
    for Nombre_Directorio in Directorio:

        #   Si no hay ningun directorio que comienze con U
        #   el programa se cerrara
        if not Nombre_Directorio.startswith("U"):
            continue;

        etiqueta = int(Nombre_Directorio.replace("U", ""))      #   Se guardara el numero de U, eg U2 -->2
        SubDirectorio = Directorios + "/" + Nombre_Directorio   #   Directorios/U1, Directorios/U2...

        Imagenes = os.listdir(SubDirectorio)    #   Lista de las imagenes dentro del Subdirectorio U'n'...

        for Nombre_Imagen in Imagenes:

            SubImagen = SubDirectorio + "/" + Nombre_Imagen     #   Directorios/U1/1.jpg, Directorios/U1/2.jpg...
            #print Nombre_Imagen
            Image = SubImagen

            #   Detectamos el Rostro segun Detect_Op, puede ser: Haar cascades o LBP.
            if(Detect_Op == 1):
                rostro = Deteccion.Deteccion_Haar(Image)    #   Detector Haar Cascade
            else:
                rostro = Deteccion.Deteccion_LBP(Image)     #   Detector LBP

            #   Si se detecto un rostro este se concatenara al array
            #   faces y se le asigna al array labels correspondiente
            if rostro is not None:
                Face.append(np.asarray(rostro, dtype=np.uint8))

    return Face

def Predecir_Imagenes(fotos, etiquetas, algoritmo):
    A = []
    c = 0
    for i in fotos:
        a = Reconocimiento.Prediccion(i,algoritmo)
        A.append(a[0][0])
        print("Real: %s, Prediccion: %s, Distancia Euclidiana: %s, Algoritmo: %s" % (etiquetas[c], a[0][0], a[0][1], algoritmo))
        c = c+1
    return etiquetas, A

def Predecir_Imageness(fotos, algoritmo):
    P = [0,0]
    for i in fotos:
        a = Reconocimiento.Prediccion(i,algoritmo)
        print("Prediccion: %s, Distancia Euclidiana: %s, Algoritmo: %s" % (a[0][0], a[0][1], algoritmo))

        if(a[0][0] < 0):
            P[0] = P[0] + 1
        else:
            P[1] = P[1] + 1

    P[0] = (P[0] / float(len(fotos)))*100 # BIEN
    P[1] = (P[1] / float(len(fotos)))*100 # MAL

    return P

def Etiquetas(etiquetas):
    A = []
    B = len(etiquetas)
    a = etiquetas.count(etiquetas[0])
    c = a

    while(c <= B):
        A.append(etiquetas[c-1])
        c = c + a
    return A

def Normal():
    Op  = None
    BD  = None
    PO  = None
    CL  = None
    UM  = None
    CO  = None

    Entrenamiento = []
    Prediccion    = []
    while(True):
        Opciones = [BD,PO,CL,UM,CO]
        Op = Menu.Normal(Opciones)
        if(Op == '1'):
            BD = Menu.Base_Datos()
        elif(Op == '2'):
            PO = Menu.Porcentaje()
        elif(Op == '3'):
            CL = Menu.Clasifcador()
        elif(Op == '4'):
            UM = Menu.Umbral()
            Reconocimiento.Configurar_Umbrales(UM)
        elif(Op == '5'):
            CO = Menu.Componentes()
            Reconocimiento.Configurar_Componentes(CO)
        elif(Op == '6'):
            print('\n\t Preparando Directorios...')
            Entrenamiento, Prediccion = Preparar_Directorios(BD,PO,CL)
            print('\n\t Entrenado al Sistema...')
            Reconocimiento.Entrenamiento(Entrenamiento[0],Entrenamiento[1])

            real,pred=Predecir_Imagenes(Prediccion[0],Prediccion[1],'EigenFace')
            f=Etiquetas(real)
            cnf_matrix = confusion_matrix(real,pred)
            plt.figure()
            Matrix.plot_confusion_matrix(cnf_matrix, classes=f,
                                  title='EigenFace')

            real,pred=Predecir_Imagenes(Prediccion[0],Prediccion[1],'FisherFace')
            f=Etiquetas(real)
            cnf_matrix = confusion_matrix(real,pred)
            plt.figure()
            Matrix.plot_confusion_matrix(cnf_matrix, classes=f,
                                  title='FisherFace')

            real,pred=Predecir_Imagenes(Prediccion[0],Prediccion[1],'LBPH')
            cnf_matrix = confusion_matrix(real,pred)
            plt.figure()
            Matrix.plot_confusion_matrix(cnf_matrix, classes=f,
                                  title='LBPH')
            plt.show()

        elif(Op == 'E'):
            break

def Ruido():
    Op  = None
    BD  = None
    BDD = None
    PO  = None
    CL  = None
    UM  = None
    CO  = None

    Entrenamiento = []
    Prediccion    = []
    while(True):
        Opciones = [BD,BDD,PO,CL,UM,CO]
        Op = Menu.Ruido(Opciones)
        if(Op == '1'):
            BD = Menu.Base_Datos()
        elif(Op == '2'):
            BDD = Menu.Base_Datos()
        elif(Op == '3'):
            PO = Menu.Porcentaje()
        elif(Op == '4'):
            CL = Menu.Clasifcador()
        elif(Op == '5'):
            UM = Menu.Umbral()
            Reconocimiento.Configurar_Umbrales(UM)
        elif(Op == '6'):
            CO = Menu.Componentes()
            Reconocimiento.Configurar_Componentes(CO)
        elif(Op == '7'):
            print('\n\t Preparando Directorios...')
            Entrenamiento, Prediccion = Preparar_Directorios(BD,PO,CL)
            DESCONOCIDOS = Preparar_Ruido(BDD,CL)
            print('\n\t Entrenado al Sistema...')
            Reconocimiento.Entrenamiento(Entrenamiento[0],Entrenamiento[1])
            PE=Predecir_Imageness(DESCONOCIDOS,'EigenFace')
            PF=Predecir_Imageness(DESCONOCIDOS,'FisherFace')
            PL=Predecir_Imageness(DESCONOCIDOS,'LBPH')
            print ("Imagenes: %s, Desconocidos(Funciona Bien): %s %%, Equivocados: %s %%" % (len(DESCONOCIDOS),PE[0],PE[1]))
            print ("Imagenes: %s, Desconocidos(Funciona Bien): %s %%, Equivocados: %s %%" % (len(DESCONOCIDOS),PF[0],PF[1]))
            print ("Imagenes: %s, Desconocidos(Funciona Bien): %s %%, Equivocados: %s %%" % (len(DESCONOCIDOS),PL[0],PL[1]))

        elif(Op == 'E'):
            break

def Experimental():
    Op  = None
    BD  = None
    CL  = None

    Entrenamiento = []
    Prediccion    = []
    while(True):
        Opciones = [BD,CL]
        Op = Menu.Experimento(Opciones)
        if(Op == '1'):
            BD = Menu.Base_Datos()
        elif(Op == '2'):
            CL = Menu.Clasifcador()
        elif(Op == '3'):
            print ("Creando Directorios y SubDirectorios...")
            path = Crear_Directorios_P()
            print ("COASDA...")
            La_Magia(path, BD, CL)

        elif(Op == 'E'):
            break

def La_Magia(path,bd,cl):

    d = ["EigenFace","FisherFace","LBPH"]
    c = [1,10,50,100,500,1000,5000,10000]

    for i in d:
        darth = path + "/" +i    #Escogemos al directorio, EigenFaces, FisherFaces... RECUERDA REINICIAR

        for j in c:
            vader = darth + "/" +str(j)  #Escogemos los SubDirectorios, 1, 10, 50...       RECUERDA REINICIAR

            for k in range(1,10):
                po = k*10#Percentage: 10, 20, 30, and so on and so forth
                print("Preparando Directorios con... Entrenamiento: %s %%, Desconocidos: %s %%" %(po,(100-po)))
                Entr,Pred = Preparar_Directorios(bd,po,cl)
                print("Entrenado al Sistema con... Base_Datos: %s, Porcentaje: %s %%, Clasifcador: %s, Componentes: %s, Umbral: %s " %(bd,po,cl,j,j))
                Reconocimiento.Configurar_Componentes(j)
                Reconocimiento.Configurar_Umbrales(j)
                Reconocimiento.Entrenamiento(Entr[0],Entr[1])
                print("Prediciendo imagenes desconocidas")
                real,pred=Predecir_Imagenes(Pred[0],Pred[1],i)
                f=Etiquetas(real)
                cnf_matrix = confusion_matrix(real,pred)
                anakin = vader + "/" + str(po) + "%"
                Matrix.plot_confusion_matrix(cnf_matrix, classes=f, title=i, save=True, path=anakin)

            vader = ""#REINICIO
        darth = ""#REINICIO


def Crear_Directorios_P():
    Directorio = os.listdir("/home/verriva/Detection_Recognition/Pruebas")
    a = "/Prueba" + str(len(Directorio) + 1)
    path = "/home/verriva/Detection_Recognition/Pruebas"+a
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        Directorio = natsorted(Directorio)           #   Ordenamos los Directorios
        a = Directorio.pop()                         #   Ultimo directorio
        b = "/Prueba" + str(int(a.replace("Prueba", ""))+1)      #   Se guarda el numero del dir
        path = "/home/verriva/Detection_Recognition/Pruebas"+b
        os.mkdir(path)

    d = ["EigenFace","FisherFace","LBPH"]
    c = [1,10,50,100,500,1000,5000,10000]

    for i in d:
        darth = path+"/"+i
        if not os.path.exists(darth):
            os.mkdir(darth)
        for j in c:
            vader = darth+"/"+str(j)
            if not os.path.exists(vader):
                os.mkdir(vader)

    return path

if __name__ == "__main__":

    while(True):
        Op = Menu.Inicio()
        if(Op == '1'):
            Normal()
        elif(Op == '2'):
            Ruido()
        elif(Op == '3'):
            Experimental()
        elif(Op == 'E'):
            print("\n\t BYE!")
            break
