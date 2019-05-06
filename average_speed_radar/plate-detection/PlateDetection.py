import os
from PIL import Image
import numpy as np
import tkinter
import pytesseract
import cv2
from copy import copy


class PlateDetection:

    path = None
    imagem_limpa = None
    imagem_limitada = None
    imagem_cortada = None
    imagem_descolorida = None
    imagem_limiarizada = None
    imagem_desfocada = None
    imagem_modificada = None
    imagem_contornada = None
    imagem_saida = []
    contornos = None

    def __init__(self, path):
        self.path = path
        self.detecta_placa()

    def detecta_placa(self):
        self.imagem_limpa = self.carrega_imagem()
        self.imagem_cortada = self.limita_imagem(self.imagem_limpa)
        self.imagem_modificada = self.processa_imagem(self.imagem_cortada)
        self.geraContornos(self.imagem_modificada)
        self.imagem_contornada = self.__desenhaContornos(self.imagem_cortada)

    def carrega_imagem(self):
        return cv2.imread(self.path)

    def limita_imagem(self, imagem):

        x = 200  #linha horizontal
        y = 150  #primeira linha vertical
        z = 1200 #segunda linha vertical

        height, width, channels = imagem.shape #Largura e Altura da imagem

        # Desenha na imagem os limites onde ela sera cortada
        self.imagem_limitada = copy(imagem)
        self.imagem_limitada = cv2.line(self.imagem_limitada, (0, x), (width, x), (0, 0, 255), 1)
        self.imagem_limitada = cv2.line(self.imagem_limitada, (y, width), (y, 0), (0, 0, 255), 1)
        self.imagem_limitada = cv2.line(self.imagem_limitada, (z, width), (z, 0), (0, 0, 255), 1)

        # região de busca
        return imagem[x:, y:z]

    def processa_imagem(self, imagem_parametro):

        # escala de cinza
        self.imagem_descolorida = cv2.cvtColor(copy(imagem_parametro), cv2.COLOR_BGR2GRAY)

        # limiarização
        ret, self.imagem_limiarizada = cv2.threshold(copy(self.imagem_descolorida), 90, 255, cv2.THRESH_BINARY)

        # desfoque
        self.imagem_desfocada = cv2.GaussianBlur(copy(self.imagem_limiarizada), (25, 25), 0)

        return self.imagem_desfocada

    def geraContornos(self, imagem_parametro):
        # lista os contornos
        self.contornos, hier = cv2.findContours(copy(imagem_parametro), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    def __desenhaContornos(self, imagem_parametro):
        imagem = copy(imagem_parametro)

        for c in self.contornos:
            # perimetro do contorno, verifica se o contorno é fechado
            perimetro = cv2.arcLength(c, True)
            if perimetro > 10:
                # aproxima os contornos da forma correspondente
                approx = cv2.approxPolyDP(c, 0.03 * perimetro, True)
                # verifica se é um quadrado ou retangulo de acordo com a qtd de vertices
                if len(approx) == 4:
                    cv2.drawContours(imagem, [c], -1, (0, 255, 0), 1)
                    (x, y, a, l) = cv2.boundingRect(c)
                    cv2.rectangle(imagem, (x, y), (x + a, y + l), (0, 255, 0), 2)
                    roi = imagem[y:y + l, x:x + a]

                    self.imagem_saida.append(roi)

        return imagem

    def inteface_grafica_imagem_limpa(self):
        cv2.imshow('Imagem Limpa' + self.path, self.imagem_limpa)

    def inteface_grafica_imagem_limitada(self):
        cv2.imshow('Imagem Limitada' + self.path, self.imagem_limitada)

    def inteface_grafica_imagem_modificada(self):
        cv2.imshow('Imagem Modificada' + self.path, self.imagem_modificada)

    def inteface_grafica_imagem_descolorida(self):
        cv2.imshow('Imagem Descolorida' + self.path, self.imagem_descolorida)

    def inteface_grafica_imagem_desfocada(self):
        cv2.imshow('Imagem Desfocada' + self.path, self.imagem_desfocada)

    def inteface_grafica_imagem_cortada(self):
        cv2.imshow('Imagem Cortada' + self.path, self.imagem_cortada)

    def inteface_grafica_imagem_contornada(self):
        cv2.imshow('Imagem com Contornos' + self.path, self.imagem_contornada)

    def inteface_grafica_imagem_limiariazada(self):
        cv2.imshow('Imagem com Limiarização' + self.path, self.imagem_limiarizada)

    def inteface_grafica_imagem_saida(self):
        for saida in self.imagem_saida:
            cv2.imshow('Contornos' + self.path, saida)

    def interface_grafica_fechar_tudo(self):
        cv2.destroyAllWindows()


#path = './sample_images/positive/'

#images_paths = [os.path.join(path, f) for f in os.listdir(path)]
#for image_path in images_paths:
    #detection = PlateDetection(image_path)
    #detection.detecta_placa()
    #detection.inteface_grafica_imagem_limpa()
    #detection.inteface_grafica_imagem_saida()
    #cv2.waitKey(3000)
    #detection.interface_grafica_fechar_tudo()

detection = PlateDetection("./sample_images/positive/EBX-5983.jpg")
detection.detecta_placa()
detection.inteface_grafica_imagem_limpa()
detection.inteface_grafica_imagem_limitada()
detection.inteface_grafica_imagem_cortada()
detection.inteface_grafica_imagem_descolorida()
detection.inteface_grafica_imagem_limiariazada()
detection.inteface_grafica_imagem_desfocada()
detection.inteface_grafica_imagem_modificada()
detection.inteface_grafica_imagem_contornada()
detection.inteface_grafica_imagem_saida()
cv2.waitKey(100000)
