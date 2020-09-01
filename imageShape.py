import numpy as np
import cv2
import random
import math
import time

class imageShape:

    def __init__(self, image_width, image_height):
        self.image_width = image_width #Guarda el ancho de la imágen.
        self.image_height = image_height #Guarda el alto de la imágen.

    def GenerateShape(self):
        self.image = np.zeros((self.image_width,self.image_height,3), np.uint8) #Genera una matriz de ceros de tamaño (width,height)
        self.random_vector = random.randrange(4) #Se crea un vector aleatorio entre 0 y 3, escogiendo un número
        #print(random_vector)


        #Square
        if self.random_vector == 0:
            side = int(min(self.image_width, self.image_height)/2) #Lado
            self.image_center = (int(self.image_width / 2), int(self.image_height / 2))  #Centro del círculo.
            x_1 = int(side / 2)  #Posición en x del punto superior izquierdo del rectángulo.
            x_2 = int(x_1 + side)  #Posición en x del punto inferior derecho del rectángulo.
            y_1 = int(side / 2)  #Posición en y del punto superior izquierdo del rectángulo.
            y_2 = int(y_1 + side)  #Posición en x del punto inferior derecho del rectángulo.
            self.shape = cv2.rectangle(self.image, (x_1, y_1), (x_2, y_2), (255, 255, 0), -1)  #Se genera el cuadrado.
            M = cv2.getRotationMatrix2D(self.image_center, 45, 1) #Calcula una matriz afin de rotación en 2D.
            self.shape = cv2.warpAffine(self.shape, M, (self.image_width, self.image_height)) #Se rota la imágen.

        #Triangle
        elif self.random_vector == 1: #Compara si random_vector es igual a 1.
            width_center = int(self.image_width / 2) #Calcula la mitad del ancho de la imagen.
            height_center = int(self.image_height / 2) #Calcula la mitad del alto de la imagen.
            triangle_side = int(min(self.image_width, self.image_height) / 2) # Selecciona el minimo entre el ancho y el alto y lo divide en 2.
            division = math.sqrt(3)/2 # Soluciona la operación : raíz de 3 entre 2.
            triangle_height = int (division * triangle_side) #Calcula la altura del triángulo.
            p1_y = int(height_center - (triangle_height / 2)) #Posición en y del punto superior del triángulo.
            point_1 = (width_center, p1_y) #Posición en (x,y) del punto superior del triángulo.
            p2_x = int(width_center + (triangle_side / 2)) #Posición en x del punto inferior izquierdo.
            p2_y = int(height_center + (triangle_height / 2)) #Posición en y del punto inferior izquierdo.
            point_2 = (p2_x, p2_y) #Posición en (x,y) del punto inferior izquierdo del triángulo.
            p3_x = int(width_center - (triangle_side / 2)) #Posición en x del punto inferior derecho.
            p3_y = int(height_center + (triangle_height / 2))#Posición en y del punto inferior derecho.
            point_3 = (p3_x, p3_y) #Posición en (x,y) del punto inferior derecho del triángulo.
            self.triangle_cnt = np.array([point_1, point_2, point_3]) #Forma un arreglo con los puntos del triángulo.
            self.shape = cv2.drawContours(self.image, [self.triangle_cnt], 0, (255, 255, 0), -1) #Se genera el triángulo centrado.

        #Rectangle
        elif self.random_vector == 2: #Compara si random_vector es igual a 2.
            horizontal_side = int(self.image_width/2) #Calcula la mitad del ancho de la imagen.
            vertical_side = int(self.image_height/2) #Calcula la mitad del alto de la imagen.
            x_1 = int(horizontal_side/2) #Posición en x del punto superior izquierdo del rectángulo.
            x_2 = int(x_1+horizontal_side) #Posición en x del punto inferior derecho del rectángulo.
            y_1 = int(vertical_side/2) #Posición en y del punto superior izquierdo del rectángulo.
            y_2 = int(y_1+vertical_side) #Posición en x del punto inferior derecho del rectángulo.
            self.shape = cv2.rectangle(self.image,(x_1,y_1),(x_2,y_2),(255,255,0),-1) #Se genera el rectángulo centrado.

        #Circle
        elif self.random_vector == 3: #Compara si random_vector es igual a 3.
            image_center= (int(self.image_width/2), int(self.image_height/2)) #Centro del círculo.
            image_radius = int(min(self.image_width, self.image_height)/4) #Radio del círculo.
            self.shape = cv2.circle(self.image,image_center,image_radius,(255,255,0),-1) #Se genera el círculo centrado.



    def ShowShape(self):

        if self.random_vector == 0: #Compara si random_vector es igual a 1.
            cv2.imshow('Square', self.shape) #Muestra el triángulo en la pantalla.
            cv2.waitKey(5000) #Se muestra la imagen durante 5 segundos.
            self.figure_type = 'Square'

        elif self.random_vector == 1: #Compara si random_vector es igual a 1.
            cv2.imshow('Triangle', self.shape) #Muestra el triángulo en la pantalla.
            cv2.waitKey(5000) #Se muestra la imagen durante 5 segundos.
            self.figure_type = 'Triangle'

        elif self.random_vector == 2: #Compara si random_vector es igual a 2.
            self.shape = cv2.rectangle(self.image,(x_1,y_1),(x_2,y_2),(255,255,0),-1) #Se genera el rectángulo centrado.
            cv2.imshow('Rectangle', self.shape) #Muestra el rectangulo en la pantalla.
            cv2.waitKey(5000) #Se muestra la imagen durante 5 segundos.
            self.figure_type = 'Rectangle'

        elif self.random_vector == 3: #Compara si random_vector es igual a 3.
            cv2.imshow('Circle', self.shape) #Muestra el circulo en la pantalla.
            cv2.waitKey(5000) #Se muestra la imagen durante 5 segundos.
            self.figure_type = 'Circle'

        else:
            cv2.imshow('Black', self.image)  # Muestra una imágen negra en la pantalla.
            cv2.waitKey(5000) #Se muestra la imagen durante 5 segundos.



    def GetShape(self):
        return self.shape, self.figure_type #Retorna la imagen seleccionada anteriormente y el nombre de la figura


    def WhatShape(self,receive_image):
        self.receive_image = receive_image #Imagen de entrada.
        image_draw = self.receive_image.copy() #Se crea una copia de la imágen.
        image_gray = cv2.cvtColor(image_draw, cv2.COLOR_BGR2GRAY) #Se convierte a escala de grises la copia de la imágen.
        ret, Ibw_shapes = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Se umbraliza la imágen con el metodo de OTSU.
        contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #Se hallan los contornos como una lista con el metodo chain_approx_simple

        for cnt in contours:#Inicialización de un for para analizar los contornos y determinar la figura
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #Con la funcion approxPoly se hallan los vertices.
            x, y, w, h = cv2.boundingRect(approx) #Con la función boundingRect se permitirá diferenciar entre un cuadrado y un rectángulo.

            if len(approx) == 3: #Compara si la imagen tiene 3 vértices.
                self.image_name = 'Triangle' #Se clasifica la imágen como un triangulo.

            elif len(approx) == 4: #Compara si la imagen tiene 4 vértices.
                aspect_ratio = float(w) / h #Se halla la relación entre el ancho y alto de la imágen.
                if aspect_ratio == 1: #Compara si aspect_ratio es igual a 1.
                    self.image_name = 'Square' #Se clasifica la imágen como un cuadrado.
                else:
                    self.image_name = 'Rectangle'#Se clasifica la imágen como un rectángulo.

            elif len(approx) > 10: #Compara si la imagen es mayor a 10 vértices.
                self.image_name = 'Circle' #Se clasifica la imágen como un circulo.


        return(self.image_name) #Retorna la clasificación de la imágen.


