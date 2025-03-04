import os
import cv2
from deepface import DeepFace
from register import jsonregister

dataPath = "data/"

def train_faces():
    encodings = []
    names = []

    # Loop through all images in the data folder
    for file in os.listdir(dataPath):
        if file.endswith(".jpg") or file.endswith(".png"):
            name = file.split("_")[0]  # Extract name from filename
            img_path = os.path.join(dataPath, file)

            # Generate face embedding
            try:
                embedding = DeepFace.represent(img_path, model_name="Facenet", enforce_detection=False)
                if embedding:
                    encodings.append(embedding[0]["embedding"])
                    names.append(name)
                    print(f"Processed: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

    print(" Training complete")

train_faces()