import cv2
import mediapipe as mp
import os
from game.game import Game


class HandTracker:
    def __init__(self, game):
        self.game = game
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=0.2, min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_drawing = mp.solutions.drawing_utils

        # Definir o tamanho da grid 8x8
        self.grid_size = 8
        self.screen_width = 800  # Largura da tela quadrada
        self.screen_height = 800  # Altura da tela quadrada
        self.hand_closed = False

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
        cap = cv2.VideoCapture(0)  # 0 para captura com webcam padrão

        # Limpando terminal e iniciando tabuleiro
        os.system("clear")
        self.game.board.print()
        print(f"Vez do jogados de {self.game.current_piece}")

        # Loop de leitura da webcam
        while True:
            ret, frame = cap.read()  # Leitura do frame
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Conversão para RGB
            results = self.hands.process(imgRGB)  # Encontra a mão na imagem

            # Se conseguiu mapear a mao
            if results.multi_hand_landmarks:
                # Para cada ponto da mao
                for hand_landmarks in results.multi_hand_landmarks:
                    # Mostra as linhas da mão na tela
                    self.mp_draw.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )

                    for id, lm in enumerate(hand_landmarks.landmark):
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)

                        if id == 9:  # MIDDLE_FINGGER_MCP
                            pos_X = (cx // 75) + 1
                            pos_Y = 8 - ((cy // 75) + 1)
                            mcp_y = cy
                            cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

                            cv2.putText(
                                frame,
                                f"Posi: {Game.get_position((pos_X, pos_Y))}",
                                (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (0, 255, 0),
                                2,
                            )
                        if id == 12:  # MIDDLE_FINGGER_TIP
                            pos_X = (cx // 75) + 1
                            pos_Y = 8 - ((cy // 75) + 1)
                            tip_y = cy
                            cv2.circle(frame, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

                            if tip_y > mcp_y and not self.hand_closed:
                                # Mão fechou
                                self.game.hand_closed(pos_Y, pos_X)
                                self.hand_closed = True
                            elif tip_y < mcp_y and self.hand_closed:
                                # Mão abriu
                                os.system("clear")
                                self.game.hand_opened(pos_Y, pos_X)
                                self.hand_closed = False
                                print(
                                    f"Vez do jogador de peças {self.game.current_piece}"
                                )
                                self.game.board.print()

            if not ret:
                break

            # # Redimensionar para manter a proporção quadrada
            frame = cv2.resize(frame, (self.screen_width, self.screen_height))

            # # Desenhar a grid 8x8
            self.draw_grid(frame)

            # # Exibir a imagem com a grid e a posição
            cv2.imshow("Hand Tracking with Grid", frame)

            # # Se a tecla 'q' for pressionada, sair do loop
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
