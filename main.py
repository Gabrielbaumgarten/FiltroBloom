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
X = 2 #Passadas de blur (começando em 0)

def main ():
    img = cv2.imread (INPUT_IMAGE)
    if img is None:
        print ('Erro abrindo a imagem.\n')
        sys.exit ()
    cv2.imshow("imagem Padrão", img)

    #Transforma a immagem em HLS
    imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS) 

    #Bright-pass  
    Lchannel = imgHLS[:,:,1]        

    #Cria a máscara
    mask = cv2.inRange(Lchannel,128.5,255)  
    res = cv2.bitwise_and(img,img,mask=mask) 
    cv2.imshow("Máscara", res)

    #Blur gaussiano
    sig=10       
    blur = cv2.GaussianBlur(res,(0,0),sig) 
    for i in range (X): #Quantidade de vezes para realizar filtro gaussiano        
        sig*=2
        blur2 = cv2.GaussianBlur(res,(0,0),sig)
        blur = cv2.addWeighted(blur, 1, blur2, 1, 0) 
        #cv2.imshow(("Imagem borrada de " + str(i)), blur)
    
    #Blur com filtro da média
    '''r=19; c=19
    blur = cv2.blur(res,(r,c))
    for i in range (X): #Quantidade de vezes para realizar filtro da média
        r*=2
        c*=2  
        for j in range(2): #Range 2 pois pelos slides com janela 19 o equivalente é 3x
            blur2=cv2.blur(res,(r,c))
        blur=cv2.addWeighted(blur, 1, blur2, 1, 0)'''

    cv2.imshow("Imagem borrada", blur)

    #Imagem final juntando máscara (com peso 0.5) e imagem
    end = cv2.addWeighted(img, 1, blur, 0.5, 0) 
    cv2.imshow("Imagem Final", end)
    #cv2.imwrite('final.png', end)

    cv2.waitKey ()
    cv2.destroyAllWindows ()

if __name__ == '__main__':
    main ()
