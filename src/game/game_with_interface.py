import pygame
import sys

# Configurações do jogo
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Inicializa o Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Damas")

# Estrutura do tabuleiro
board = [[None for _ in range(COLS)] for _ in range(ROWS)]
for row in range(ROWS):
    for col in range(COLS):
        if (row + col) % 2 == 1:
            if row < 3:
                board[row][col] = "R"
            elif row > 4:
                board[row][col] = "G"


# Função para desenhar o tabuleiro
def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )


# Função para desenhar as peças
def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "R":
                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        col * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2,
                    ),
                    SQUARE_SIZE // 2 - 5,
                )
            elif board[row][col] == "G":
                pygame.draw.circle(
                    screen,
                    GRAY,
                    (
                        col * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2,
                    ),
                    SQUARE_SIZE // 2 - 5,
                )


# Função para converter posição de pixel para coordenadas de tabuleiro
def get_board_pos(pos):
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE


# Loop principal
def init_game():
    running = True
    selected_piece = None
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_board_pos(pygame.mouse.get_pos())
                print(selected_piece)
                if selected_piece:
                    board[selected_piece[0]][selected_piece[1]] = None
                    board[row][col] = "R"
                    selected_piece = None
                elif board[row][col] == "R":
                    print("Teste")
                    selected_piece = (row, col)
        draw_board()
        draw_pieces()
        pygame.display.flip()
    pygame.quit()
    sys.exit()
