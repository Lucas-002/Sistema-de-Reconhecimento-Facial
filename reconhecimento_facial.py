
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Carregar modelo pré-treinado de detecção facial do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carregar modelo de reconhecimento facial treinado (exemplo)
model = load_model("modelo_reconhecimento.h5")

# Dicionário de nomes associados às classes
label_dict = {0: "Lucas", 1: "Maria", 2: "João"}

# Captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (100, 100)) / 255.0
        face = np.expand_dims(face, axis=0)

        prediction = model.predict(face)
        label = np.argmax(prediction)
        name = label_dict.get(label, "Desconhecido")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Reconhecimento Facial", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
