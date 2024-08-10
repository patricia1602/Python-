import cv2
from cvzone.HandTrackingModule import HandDetector

# inicializa a webcam
webcam = cv2.VideoCapture(2)

# verificar se a webcam foi aberta corretamente
if not webcam.isOpened():
   print("Erro: Não foi possível acessar a câmera.")
   exit()

# inicializa o rastreador de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcam.read()

    # verifica se a captura da imagem foi bem-sucedida
    if not sucesso or imagem is None:
        print("Erro: Não foi possível ler a imagem da câmera.")
        break

# Se a imagem foi capturada corretamnete, prossiga com a convenção e dectação
    hands, imagem_maos = rastreador.findHands(imagem)

# mostra a iamgem com as mãos dectadas
    cv2.imshow("Projeto 4 - IA", imagem_maos)

# se qualquer tecla for pressionada, sai do loop
    if cv2.waitKey(1) != -1: 
        break

# Libera a camera e fecha as janelas
    webcam.release()
    cv2.destroyAllWindows()
