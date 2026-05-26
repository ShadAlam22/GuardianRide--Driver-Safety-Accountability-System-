import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def facerecog():
    try:
        # Load the data
        data = np.load(r"faces.npy")

        cap = cv2.VideoCapture(1)
        classifier = cv2.CascadeClassifier(r"web\FaceRecog.py")

        X = data[:, 1:].astype(int)
        y = data[:, 0]

        model = KNeighborsClassifier(n_neighbors=4)
        model.fit(X, y)

        predicted_name = None

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame from camera/stream end")
                break

            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = classifier.detectMultiScale(gray)

            for (x, y, w, h) in faces:
                face_img = gray[y:y + h, x:x + w]
                face_img = cv2.resize(face_img, (100, 100))

                flat = face_img.flatten()
                res = model.predict([flat])
                label = str(res[0])
                
                predicted_name = label

                # Draw rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Display the predicted name
                cv2.putText(frame, predicted_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

            cv2.imshow('Face Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        return predicted_name

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
