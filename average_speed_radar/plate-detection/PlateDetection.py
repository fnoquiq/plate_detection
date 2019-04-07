import os
from PIL import Image
import numpy as np
import tkinter
import pytesseract
import cv2
from copy import copy


class PlateDetection:
    PERIMETRO_CONTORNO = 150

    path = None
    imagem_limpa = None
    imagem_limitada = None
    imagem_cortada = None
    imagem_modificada = None
    imagem_saida = []
    contornos = None

    def __init__(self, path):
        self.path = path
        self.imagem_limpa = cv2.imread(path)
        self.detecta_placa()

    def detecta_placa(self):
        self.imagem_limpa = self.carrega_imagem()
        self.imagem_cortada = self.limita_imagem(self.imagem_limpa)
        self.imagem_modificada = self.processa_imagem_e_gera_contornos(self.imagem_cortada)
        self.__desenhaContornos(self.imagem_limpa)

    def carrega_imagem(self):
        return cv2.imread(self.path)

    def limita_imagem(self, imagem):

        # gera uma copia da imagem
        self.imagem_limitada = copy(imagem)
        # limite horizontal
        self.imagem_limitada = cv2.line(self.imagem_limitada, (0, 350), (860, 350), (0, 0, 255), 1)
        # limite vertical 1
        self.imagem_limitada = cv2.line(self.imagem_limitada, (220, 0), (220, 480), (0, 0, 255), 1)
        # limite vertical 2
        self.imagem_limitada = cv2.line(self.imagem_limitada, (500, 0), (500, 480), (0, 0, 255), 1)

        # região de busca
        #imagem = imagem[350:, 220:500]

        return imagem

    def processa_imagem_e_gera_contornos(self, imagem):

        # escala de cinza
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # limiarização
        ret, imagem = cv2.threshold(imagem, 90, 255, cv2.THRESH_BINARY)

        # desfoque
        imagem = cv2.GaussianBlur(imagem, (25, 25), 0)

        # lista os contornos
        self.contornos, hier = cv2.findContours(imagem, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        return imagem

    def __desenhaContornos(self, imagem):
        for c in self.contornos:
            # perimetro do contorno, verifica se o contorno é fechado
            perimetro = cv2.arcLength(c, True)
            if perimetro > self.PERIMETRO_CONTORNO:
                # aproxima os contornos da forma correspondente
                approx = cv2.approxPolyDP(c, 0.03 * perimetro, True)
                # verifica se é um quadrado ou retangulo de acordo com a qtd de vertices
                if len(approx) == 4:
                    # cv2.drawContours(imagem, [c], -1, (0, 255, 0), 1)
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

    def inteface_grafica_imagem_saida(self):
        for saida in self.imagem_saida:
            print('ola')
            cv2.imshow('Contornos' + self.path, saida)

    def interface_grafica_fechar_tudo(self):
        cv2.destroyAllWindows()


path = './sample_images/positive/'

images_paths = [os.path.join(path, f) for f in os.listdir(path)]
for image_path in images_paths:
    detection = PlateDetection(image_path)
    detection.detecta_placa()
    detection.inteface_grafica_imagem_limpa()
    detection.inteface_grafica_imagem_saida()
    cv2.waitKey(3000)
    detection.interface_grafica_fechar_tudo()
