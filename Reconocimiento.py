import numpy as np
import Deteccion
import time
import cv2
import os

#   OPEN CV 3.3.0
EigenFace = cv2.face.EigenFaceRecognizer_create(num_components=80, threshold=50)
FisherFace = cv2.face.FisherFaceRecognizer_create(num_components=80, threshold=50)
Face_LBP = cv2.face.LBPHFaceRecognizer_create(threshold=50)

def Entrenamiento(faces, labels):
    #   Este metodo se encarga de entrenar al sistema en los tres diferentes
    #   metodos de deteccion de rostros.

    inicio = time.time()
    EigenFace.train(faces, np.array(labels))
    fin = time.time()
    tiempo = fin - inicio
    print 'FisherFace train: ', tiempo

    inicio = time.time()
    FisherFace.train(faces, np.array(labels))
    fin = time.time()
    tiempo = fin - inicio
    print 'EigenFace train: ', tiempo

    inicio = time.time()
    Face_LBP.train(faces, np.array(labels))
    fin = time.time()
    tiempo = fin - inicio
    print 'LBPH train: ', tiempo

def Prediccion(face,algoritmo):
    #    AQUI SE HACE LA MAGIA, PARA ELLO YA DEBIO DE HABERSE
    #    ENTRENADO AL SISTEMA :3

    Pre = []    #   Lista a retornar

    if(algoritmo == 'EigenFace'):
        label1 = EigenFace.predict(face)
        Pre.append(label1)

    elif(algoritmo == 'FisherFace'):
        label2 = FisherFace.predict(face)
        Pre.append(label2)

    elif(algoritmo == 'LBPH'):
        label3 = Face_LBP.predict(face)
        Pre.append(label3)

    return Pre

def Configurar_Umbrales(Umbral):
    EigenFace.setThreshold(Umbral)
    FisherFace.setThreshold(Umbral)
    Face_LBP.setThreshold(Umbral)

    T1 = EigenFace.getThreshold()
    T2 = FisherFace.getThreshold()
    T3 = Face_LBP.getThreshold()
    print('EigenFace:  %s' % T1)
    print('FisherFace: %s' % T2)
    print('LBPH:       %s' % T3)
    x = raw_input("Press Enter")

def Configurar_Componentes(Componente):
    EigenFace.setNumComponents(Componente)
    FisherFace.setNumComponents(Componente)

    print('EigenFace:  %s' % Componente)
    print('FisherFace: %s' % Componente)
    x = raw_input("Press Enter")
    #T1 = EigenFace.getNumComponents(Componente)
    #T2 = FisherFace.getNumComponents(Componente)
    #print(T1)
    #print(T2)
