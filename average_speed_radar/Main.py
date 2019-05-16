import cv2

from plate_detection.PlateDetection import PlateDetection
from camera_integration.CameraIntegration import get_camera

camera = get_camera()

while True:
    conectado, frame = camera.read()
    detection = PlateDetection(frame)
    cv2.imshow('Imagem com Limites', detection.original_image)
    cv2.imshow('Imagem Contornada', detection.ShapeDetector.image_with_shapes)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
