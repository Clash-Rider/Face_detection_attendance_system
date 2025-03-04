import os
import cv2
from deepface import DeepFace
from register import jsonregister

dataPath = "data/"

def recognize_faces():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Faster webcam access

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # Detect and compare face with stored images
            result = DeepFace.find(img_path=frame, db_path=dataPath, model_name="Facenet")

            names_detected = []
            if len(result) > 0 and not result[0].empty:
                for i, row in result[0].iterrows():
                    filename = os.path.basename(row["identity"])
                    detected_name = filename.split("_")[0]  # Extract name from filename
                    names_detected.append(detected_name)

            # Display result
            name_text = ", ".join(set(names_detected)) if names_detected else "Unknown"
            cv2.putText(frame, name_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print(f"Detected: {name_text}")
            jsonregister(names_detected)

        except Exception as e:
            print(f"Error detecting face: {e}")

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

recognize_faces()