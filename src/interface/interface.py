import cv2
import mediapipe as mp



class HandTracker:
    def __init__(self, game):
        self.game = game
        # Inicializar MediaPipe Hand Detection
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.2, min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

        # Definir o tamanho da grid 8x8
        self.grid_size = 8
        self.screen_width = 800  # Largura da tela quadrada
        self.screen_height = 800  # Altura da tela quadrada
        self.hand_closed = False

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

                # Encontrar a posição do centro da mão (média de algumas landmarks)
                x = sum(landmarks[i].x for i in range(0, 21)) / 21
                y = sum(landmarks[i].y for i in range(0, 21)) / 21
                palm_position = (x, y)

                # Detectar se a mão está fechada
                if self.is_hand_closed(landmarks):
                    if not self.hand_closed:
                        self.mao_fechou(palm_position)
                        self.hand_closed = True
                else:
                    if self.hand_closed:
                        self.mao_abriu(palm_position)
                        self.hand_closed = False

                return palm_position

        return None

    def is_hand_closed(self, landmarks):
        """
        Determina se a mão está fechada com base na posição dos dedos.
        """
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]

        palm_base = landmarks[0]

        closed_threshold = 0.1

        return (
            abs(thumb_tip.y - palm_base.y) < closed_threshold and
            abs(index_tip.y - palm_base.y) < closed_threshold and
            abs(middle_tip.y - palm_base.y) < closed_threshold and
            abs(ring_tip.y - palm_base.y) < closed_threshold and
            abs(pinky_tip.y - palm_base.y) < closed_threshold
        )

    def calculate_grid_position(self, palm_position):
        """
        Calcula a posição da mão na grid 8x8, baseada na posição relativa do centro da mão.
        """
        x, y = palm_position

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

    def mao_fechou(self, palm_position):
        row, col = self.calculate_grid_position(palm_position)
        with open("log.txt", "a") as f:
            f.write(f"Mão fechou em: {row}, {col}\n")
        self.game.hand_closed(row, col)

    def mao_abriu(self, palm_position):
        row, col = self.calculate_grid_position(palm_position)
        with open("log.txt", "a") as f:
            f.write(f"Mão abriu em: {row}, {col}\n")
        self.game.hand_opened(row, col)

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