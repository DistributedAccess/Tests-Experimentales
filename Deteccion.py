import crop_face
import math
import cv2

Recorte = None

#   USAR EL ESTANDAR ISO/IEC 19794-5
#   ALINEAR Y NORMALIZAR
#   UTULIZAR EL ALGORITMO PROPUESTO POR OPENCV EL DE ARNOLD SWATCWADSADASER JAJAJA :3

def Deteccion_Haar(Imagen):
    #   Esta_Funcion detecta los rostros de la Imagen de Entrada y regresa
    #   el array del numero de rostros y la ubicacion de cada uno

    global Recorte
    #   Cargamos la imagen
    Image = cv2.imread(Imagen)

    #   Convertimos a escala de grises
    Gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    #   Cargamos el clasificador
    haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    #   Detectamos rostros, algunos rostros podran estar mas cercanos a la camara
    faces = haar_face_cascade.detectMultiScale(Gray, scaleFactor=1.1, minNeighbors=5);
    #return faces
    for (x,y,w,h) in faces:
        Recorte = Gray[y:y+w, x:x+h]

    return Recorte

def Deteccion_LBP(Imagen):
    #   Esta_Funcion detecta los rostros de la Imagen de Entrada y regresa
    #   el array del numero de rostros y la ubicacion de cada uno

    global Recorte
    #   Cargamos la imagen
    Image = cv2.imread(Imagen)

    #   Convertimos a escala de grises
    Gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    #   Cargamos el clasificador
    lbp_face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

    #   Detectamos rostros
    faces = lbp_face_cascade.detectMultiScale(Gray, scaleFactor=1.1, minNeighbors=5);
    #return faces
    for (x,y,w,h) in faces:
        Recorte = Gray[y:y+w, x:x+h]

    return Recorte

def Deteccion_LBP2(Imagen):
    #   Esta_Funcion detecta los rostros de la Imagen de Entrada y regresa
    #   el array del numero de rostros y la ubicacion de cada uno

    global Recorte
    #   Cargamos la imagen

    #   Convertimos a escala de grises

    #   Cargamos el clasificador
    lbp_face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

    #   Detectamos rostros
    faces = lbp_face_cascade.detectMultiScale(Imagen, scaleFactor=1.1, minNeighbors=5);
    #return faces
    for (x,y,w,h) in faces:
        Recorte = Imagen[y:y+w, x:x+h]

    return Recorte

def Recort(Gray,faces):
    Recte = None
    for (x,y,w,h) in faces:
        Recte = Gray[y:y+w, x:x+h]    #Rostro Recort
    return Recte

def LBP_Normalizado(Imagen):
    global Recorte
    #   Cargamos la imagen
    Image = cv2.imread(Imagen)
    Size = Image.shape #GUARDA EL TAMANO DEL ROSTRO
    #   Convertimos a escala de grises
    Gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    #   Cargamos el clasificador
    lbp_face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

    #   Detectamos rostros
    faces = lbp_face_cascade.detectMultiScale(Gray, scaleFactor=1.1, minNeighbors=5);


    for (x,y,w,h) in faces:
        Recorte = Gray[y:y+w, x:x+h]    #Rostro Recortado
    #Recorte = Recort(Gray,faces)
    #print Recorte

    Derecho, Izquier = Eye_Detect(Recorte)  #Ojo Derecho y Izquierdo

    if(Derecho or Izquier):    #SIGNIFICA QUE DETECTO OJITOS

        #   DISTANCIA ENTRE LOS OJOS PARA POSTERIOR AJUSTE
        Hipotenusa = math.sqrt(math.pow((Derecho[0]-Izquier[0]),2)+math.pow((Derecho[1]-Izquier[1]),2))  #HIPOTENUSA
        CatAdyacen = Derecho[0] - Izquier[0]    #   CATETO ADYACENTE
        CatOpuesto = Derecho[1] - Izquier[1]    #   CATETO OPUESTO
        Angulo = math.acos(CatAdyacen/Hipotenusa)
        #   ANGULO EN RADIANES
        Angulo = math.degrees(Angulo)   #   ANGULO EN GRADOS
        print Angulo
        if(Derecho[1] > Izquier[1]):   # CON ESTA RUTINA ASEGURAMOS ARREGLAR LA IMAGEN
            Angulo = Angulo * (1)
        elif(Izquier[1] > Derecho[1]):
            Angulo = Angulo * (-1)
        print Hipotenusa, CatAdyacen, CatOpuesto, Angulo
        #   ROTACION DE LA IMAGEN OJO IZQUIERDO COMO ORIGEN
        Rotate = cv2.getRotationMatrix2D((Izquier[0],Izquier[1]),Angulo,1)   #ROTACION
        dst = cv2.warpAffine(Gray,Rotate,(Size[1],Size[0]))         #SE APLICA , cols, rows

        #   ESCALAMOS LA DISTANCIA A 96 PIXELES ENTRE LOS OJITOS
        Escala = 90 / Hipotenusa
        print "ESCALA ojos"
        print (Escala * Hipotenusa), Hipotenusa
        print type(Escala)
        print type(Size[0])
        Rows = float(Size[0]) * Escala #ROWS
        Cols = float(Size[1]) * Escala #COLS
        print "tamano de la imagen real y,x"
        print Size[0],Size[1]
        print "Escala chidorina y,x"
        print Rows, Cols
        Resizis = cv2.resize(dst, (int(Cols), int(Rows)))

        #   DETECTAMOS EL ROSTRO OTRAVEZ...
        Feis = Deteccion_LBP2(Resizis)
        Seix = Feis.shape #GUARDA EL TAMANO DEL ROSTRO
        print "Rostro Cuadro x,y"
        print Seix[0],Seix[1]
        if(Seix[0] < 192):#CASO EXTREMO, EL CUADRO DEL ROSTRO ES MENOR QUE LA RESOLUCION REQUERIDA
            Feis = cv2.resize(Feis, (192,192))
            Seix = Feis.shape #GUARDA EL TAMANO DEL ROSTRO
            print "Rostro Cuadro Resizido x,y"
            print Seix[0],Seix[1]

        #   YA CASI, AHORA RECORTAMOS A 168X192
        centroy = Seix[0]/2
        centrox = Seix[1]/2
        Chop = Feis[(centroy-96):(centroy+96),(centrox-84):(centrox+84)]
        Chap = Chop.shape
        print "REcorte"
        print Chap[0], Chap[1]

        #   ECUALIZAMOS Y SHA <3
        Equ = cv2.equalizeHist(Chop)

        cv2.imshow("Normal",Gray)
        cv2.imshow("Giro",dst)
        cv2.imshow("Resize",Resizis)
        cv2.imshow("Rostro, Casi normal",Feis)
        cv2.imshow("Rostro, Recprtado",Chop)
        cv2.imshow("Esta es la chida",Equ)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:           #SIGNIFICA QUE NO DETECTO NINGUN OJO

        #   ESCALAMOS LA DISTANCIA A 192x192
        Resizis = cv2.resize(Recorte, (192, 192))

        #   YA CASI, AHORA RECORTAMOS A 168X192
        Chip = Resizis[0:192,12:180]
        Chap = Chip.shape
        print Chap[0], Chap[1]

        #   ECUALIZAMOS Y SHA <3
        Equ = cv2.equalizeHist(Chip)

        cv2.imshow("Normal",Gray)
        cv2.imshow("Rostro",Recorte)
        cv2.imshow("ESCALAMOS A 192x192",Resizis)
        cv2.imshow("Rostro, Recprtado",Chip)
        cv2.imshow("Esta es la chida",Equ)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return "OK"



def Eye_Detect(Rostro):
    haar_eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    eye = haar_eye_cascade.detectMultiScale(Rostro, scaleFactor=1.1, minNeighbors=5);


    #eye[:,2:] += eye[:,:2]  #PASO DE LA MUERTE
    Derecho = []
    Izquier = []

    #   UBICACION DEL OJO DERECHO Y IZQUIERDO
    if (len(eye) == 2):
        eye[:,2:] += eye[:,:2]  #PASO DE LA MUERTE

        a = eye[0][0] + ((eye[0][2] - eye[0][0])/2)
        b = eye[0][1] + ((eye[0][3] - eye[0][1])/2)

        c = eye[1][0] + ((eye[1][2] - eye[1][0])/2)
        d = eye[1][1] + ((eye[1][3] - eye[1][1])/2)

        if(a<c):    #IZQUIERDO
            Izquier = [a,b]
            Derecho = [c,d]
        else:       #DERECHO
            Izquier = [c,d]
            Derecho = [a,b]

    return Derecho, Izquier




"""def Deteccion_Eye(Rostro):

    Size = Rostro.shape #GUARDA EL TAMANO DEL ROSTRO

    haar_eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    eye = haar_eye_cascade.detectMultiScale(Rostro, scaleFactor=1.1, minNeighbors=5);

    eye[:,2:] += eye[:,:2]  #PASO DE LA MUERTE

    Derecho = []
    Izquier = []

    #   UBICACION DEL OJO DERECHO Y IZQUIERDO
    if (len(eye) == 2):
        a = eye[0][0] + ((eye[0][2] - eye[0][0])/2)
        b = eye[0][1] + ((eye[0][3] - eye[0][1])/2)

        c = eye[1][0] + ((eye[1][2] - eye[1][0])/2)
        d = eye[1][1] + ((eye[1][3] - eye[1][1])/2)

        if(a<c):    #IZQUIERDO
            Izquier = [a,b]
            Derecho = [c,d]
        else:       #DERECHO
            Izquier = [c,d]
            Derecho = [a,b]

    #   DISTANCIA ENTRE LOS OJOS PARA POSTERIOR AJUSTE
    Hipotenusa = math.sqrt(math.pow((Derecho[0]-Izquier[0]),2)+math.pow((Derecho[1]-Izquier[1]),2))  #HIPOTENUSA
    CatAdyacen = Derecho[0] - Izquier[0]    #   CATETO ADYACENTE
    CatOpuesto = Derecho[1] - Izquier[1]    #   CATETO OPUESTO
    Angulo = math.acos(CatAdyacen/Hipotenusa)   or python
    #   ANGULO EN RADIANES
    Angulo = math.degrees(Angulo)   #   ANGULO EN GRADOS
    if((Angulo > 0) or (Angulo < 0)):   # CON ESTA RUTINA ASEGURAMOS ARREGLAR LA IMAGEN
        Angulo = Angulo * (-1)
    print Hipotenusa, CatAdyacen, CatOpuesto, Angulo
    #   ROTACION DE LA IMAGEN OJO IZQUIERDO COMO ORIGEN
    Rotate = cv2.getRotationMatrix2D((Izquier[0],Izquier[1]),Angulo,1)   #ROTACION
    dst = cv2.warpAffine(Rostro,Rotate,(Size[1],Size[0]))         #SE APLICA

    cv2.imshow("Normal",Rostro)
    cv2.imshow("Giro",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    return Izquier, Derecho"""

def Normalizar(image, Algoritmo):

    if(Algoritmo == "LBP"):
        Rostro=Deteccion_LBP(image)     #OBTENEMOS EL ROSTRO DE LA IMAGEN
        D,I = Deteccion_Eye(Rostro)
        Norm = crop_face.CropFace(Rostro, eye_left=(I[0],I[1]), eye_right=(D[0],D[1]), offset_pct=(0.3,0.3), dest_sz=(200,200))
        Norm = numpy.array(Norm)
        return Norm

    elif(Algoritmo == "Haar"):
        Rostro=Deteccion_Haar(image)     #OBTENEMOS EL ROSTRO DE LA IMAGEN
        D,I = Deteccion_Eye(Rostro)
        Norm = crop_face.CropFace(Rostro, eye_left=(I[0],I[1]), eye_right=(D[0],D[1]), offset_pct=(0.2,0.2), dest_sz=(168,192))
        Norm = numpy.array(Norm)
        return Norm

def Dibujar_Rectangulos(Faces, Image):
    for (x, y, w, h) in Faces:
        cv2.rectangle(Image, (x,y), (x+w,y+h), (0, 255, 0), 2)

    cv2.imshow('Rostros',Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Dibujar_Ojos(D,I,Imagen):
    cv2.circle(Imagen, (D[0],D[1]), 5, (0,255,0),2)
    cv2.circle(Imagen, (I[0],I[1]), 5, (255,0,0),2)
    cv2.imshow("wao",Imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Recortar_Rostros(Img, faces):
    for (x,y,w,h) in faces:
        return Img[y:y+w, x:x+h]

def Ajustar_Rostro(Face, Ancho, Alto):
    #Gris = cv2.cvtColor(Face, cv2.COLOR_RGB2GRAY)
    #Gris = cv2.equalizeHist(Recorte)
    #Ajuste = cv2.resize(Face, (Ancho, Alto))
    #return Ajuste
    return cv2.resize(Face, (Ancho, Alto))
