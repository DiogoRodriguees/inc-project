import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self):
        # Inicializar MediaPipe Hand Detection
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.2, min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

    def track_hands(self, frame):
        # Converta a imagem BGR para RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Processar a imagem
        result = self.hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Desenhar as landmarks das mãos
                self.mp_drawing.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )

                # Extraindo e retornando a posição das landmarks (se necessário)
                landmarks = []
                for landmark in hand_landmarks.landmark:
                    landmarks.append(
                        (landmark.x, landmark.y, landmark.z)
                    )  # Normalizado
                return landmarks
        return None

    def capture(self):
        # Iniciar a captura de vídeo
        cap = cv2.VideoCapture(0)  # 0 para webcam padrão

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Trackear as mãos e capturar as landmarks
            landmarks = self.track_hands(frame)

            # Exibir a imagem com as landmarks
            cv2.imshow("Hand Tracking", frame)

            # Se a tecla 'q' for pressionada, sair do loop
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
