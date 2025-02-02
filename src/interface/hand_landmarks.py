import cv2
import mediapipe as mp
import math


class HandTracker:
    def __init__(self):
        # Inicializar MediaPipe Hand Detection
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.2, min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

        # Definir o tamanho da grid 8x8
        self.grid_size = 8
        self.screen_width = 500  # Largura da tela quadrada
        self.screen_height = 500  # Altura da tela quadrada

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

                # Extraindo as landmarks
                landmarks = hand_landmarks.landmark

                # Encontrar a posição da palma da mão (landmark 0)
                palm_position = landmarks[0]  # Landmark 0 é a base da palma
                return palm_position

        return None

    def calculate_grid_position(self, palm_position):
        """
        Calcula a posição da mão na grid 8x8, baseada na posição relativa da palma da mão.
        """
        # Obter a posição normalizada da palma (usando as coordenadas x e y)
        x, y = palm_position.x, palm_position.y

        # Convertendo as coordenadas normalizadas para a escala da tela
        x_pixel = int(x * self.screen_width)
        y_pixel = int(y * self.screen_height)

        # Calcular a linha e a coluna na grid 8x8
        row = int(y_pixel / (self.screen_height / self.grid_size))
        col = int(x_pixel / (self.screen_width / self.grid_size))

        return row, col

    def draw_grid(self, frame):
        """
        Desenha a grid 8x8 na tela.
        """
        step_x = self.screen_width // self.grid_size
        step_y = self.screen_height // self.grid_size

        for i in range(1, self.grid_size):
            cv2.line(
                frame,
                (i * step_x, 0),
                (i * step_x, self.screen_height),
                (255, 255, 255),
                2,
            )
            cv2.line(
                frame,
                (0, i * step_y),
                (self.screen_width, i * step_y),
                (255, 255, 255),
                2,
            )

    def capture(self):
        # Iniciar a captura de vídeo
        cap = cv2.VideoCapture(0)  # 0 para webcam padrão

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Redimensionar para manter a proporção quadrada
            frame = cv2.resize(frame, (self.screen_width, self.screen_height))

            # Trackear as mãos e capturar a posição da palma
            palm_position = self.track_hands(frame)

            # Desenhar a grid 8x8
            self.draw_grid(frame)

            # Se a palma da mão foi detectada
            if palm_position:
                # Calcular a posição na grid
                row, col = self.calculate_grid_position(palm_position)

                # Exibir a posição da mão na tela
                cv2.putText(
                    frame,
                    f"Posição: {row}, {col}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

            # Exibir a imagem com a grid e a posição
            cv2.imshow("Hand Tracking with Grid", frame)

            # Se a tecla 'q' for pressionada, sair do loop
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


# Criar e capturar com o HandTracker
hand_tracker = HandTracker()
hand_tracker.capture()
