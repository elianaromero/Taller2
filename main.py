from imageShape import *
import cv2
import numpy as np

if __name__=='__main__':
    image_width = int(input('Introduzca el ancho de la imagen que desea generar: ')) #Pide al usuario el ancho de la imagen.
    image_height = int(input('Introduzca el alto de la imagen que desea generar: ')) #Pide al usuario el ancho de la imagen.
    properties = imageShape(image_width, image_height) #Guarda el ancho y alto en la clase imageShape.
    properties.GenerateShape() #Llama a GenerateShape.
    properties.ShowShape() #Llama a ShowShape.
    receive_image,string = properties.GetShape() #Retorna la imagen y un string del nombre de la imagen desde GetShape.
    #print(String)
    image_name = properties.WhatShape(receive_image) #
    #print(ImageName)

    if image_name == string:
        print('La clasificación es correcta')
    else:
        print('La clasificación no es correcta')


