import cv2

from plate_detection.PlateDetection import PlateDetection

video = cv2.VideoCapture(0)

while True:
    conectado, frame = video.read()
    detection = PlateDetection(frame)
    cv2.imshow('Imagem com Limites', detection.original_image)
    cv2.imshow('Imagem Contornada', detection.ShapeDetector.image_with_shapes)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
