import cv2

from plate_detection.PlateDetection import PlateDetection
from plate_detection.PlateFormatter import is_plate_format
from camera_integration.CameraIntegration import get_camera
from character_recognition.CharacterRecognition import CharacterRecognition

camera = get_camera()

while camera.isOpened():
    conectado, frame = camera.read()
    detection = PlateDetection(frame)
    ocr = CharacterRecognition()
    text = ocr.recognition(detection.ShapeDetector.shape_detected)

    if is_plate_format(text):
        print("Placa detectada: ", text)

    cv2.imshow("Camera", detection.ShapeDetector.image_with_shapes)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
