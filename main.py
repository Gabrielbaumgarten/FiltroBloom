# Autores: Gabriel Baumgarten e Henrique Da Gama
# Universidade Tecnológica Federal do Paraná
#===============================================================================

import sys
import numpy as np
import cv2
import cv
import math

#===============================================================================

INPUT_IMAGE =  'GT2.BMP'

def main ():
    img = cv2.imread (INPUT_IMAGE)
    if img is None:
        print ('Erro abrindo a imagem.\n')
        sys.exit ()
    cv2.imshow("imagem Padrão", img)
    imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS) #Transforma a immagem em HLS
    #cv2.imshow("imagemhsl", imgHLS)  
    Lchannel = imgHLS[:,:,1]    
    mask = cv2.inRange(Lchannel, 125, 255) #Bright-pass    
    res = cv2.bitwise_and(img,img, mask= mask) #Cria a máscara
    #cv2.imshow("Máscara", res)
    blur = cv2.GaussianBlur(res,(0,0),10) #Blur gaussiano
    '''blur=cv2.blur(res, (19,19)) #Blur com filtro da média
    for i in range (2): #Quantidade de vezes para realizar filtro da média
        blur=cv2.blur(blur, (19,19))'''
    #cv2.imshow("Imagem borrada", blur)
    end = cv2.addWeighted(img, 1, blur, 0.5, 0) #Imagem final juntando máscara e imagem
    cv2.imshow("Imagem Final", end)
    #cv2.imwrite('final.png', end)
    cv2.waitKey ()
    cv2.destroyAllWindows ()

if __name__ == '__main__':
    main ()
