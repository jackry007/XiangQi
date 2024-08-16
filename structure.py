import pygame #type: ignore
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1100
BOARD_ROWS = 10
BOARD_COLS = 9

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chinese Chess (Xiangqi)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (160, 82, 45)

# Load piece images


def load_images(CELL_SIZE):
    pieces = {}
    piece_names = ['black_cannon', 'black_elephant', 'black_guard', 'black_horse', 'black_king', 'black_pawn', 'black_rook',
                   'red_cannon', 'red_elephant', 'red_guard', 'red_horse', 'red_king', 'red_pawn', 'red_rook']
    for name in piece_names:
        image = pygame.image.load(f"images/{name}.png")
        pieces[name] = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
    return pieces

# Draw the board


def draw_board(CELL_SIZE):
    # Board background
    screen.fill(BROWN)

    # Draw grid lines
    for row in range(BOARD_ROWS):
        if row != 4:  # Skip the row that represents the river
            pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, CELL_SIZE // 2 + row * CELL_SIZE),
                             (SCREEN_WIDTH - CELL_SIZE // 2, CELL_SIZE // 2 + row * CELL_SIZE), 2)
    for col in range(BOARD_COLS):
        # Skip the column lines between rows 4 and 5
        pygame.draw.line(screen, BLACK, (CELL_SIZE // 2 + col * CELL_SIZE, CELL_SIZE // 2),
                         (CELL_SIZE // 2 + col * CELL_SIZE, 4 * CELL_SIZE + CELL_SIZE // 2), 2)
        pygame.draw.line(screen, BLACK, (CELL_SIZE // 2 + col * CELL_SIZE, 5 * CELL_SIZE + CELL_SIZE // 2),
                         (CELL_SIZE // 2 + col * CELL_SIZE, SCREEN_HEIGHT - CELL_SIZE // 2), 2)

    # Draw river with a gap in the middle
    pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, 4 * CELL_SIZE + CELL_SIZE // 2),
                     (SCREEN_WIDTH // 2  // 2, 4 * CELL_SIZE + CELL_SIZE // 2), 2)
    pygame.draw.line(screen, BLACK, (SCREEN_WIDTH // 2  // 2, 4 * CELL_SIZE + CELL_SIZE // 2),
                     (SCREEN_WIDTH - CELL_SIZE // 2, 4 * CELL_SIZE + CELL_SIZE // 2), 2)

    # Draw palace
    pygame.draw.line(screen, BLACK, (3 * CELL_SIZE + CELL_SIZE // 2, CELL_SIZE // 2),
                     (5 * CELL_SIZE + CELL_SIZE // 2, 2 * CELL_SIZE + CELL_SIZE // 2), 2)
    pygame.draw.line(screen, BLACK, (3 * CELL_SIZE + CELL_SIZE // 2, 2 * CELL_SIZE + CELL_SIZE // 2),
                     (5 * CELL_SIZE + CELL_SIZE // 2, CELL_SIZE // 2), 2)

    pygame.draw.line(screen, BLACK, (3 * CELL_SIZE + CELL_SIZE // 2, 7 * CELL_SIZE + CELL_SIZE // 2),
                     (5 * CELL_SIZE + CELL_SIZE // 2, 9 * CELL_SIZE + CELL_SIZE // 2), 2)
    pygame.draw.line(screen, BLACK, (3 * CELL_SIZE + CELL_SIZE // 2, 9 * CELL_SIZE + CELL_SIZE // 2),
                     (5 * CELL_SIZE + CELL_SIZE // 2, 7 * CELL_SIZE + CELL_SIZE // 2), 2)

# Draw the pieces on the board


def draw_pieces(board, piece_images, CELL_SIZE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            piece = board[row][col]
            if piece != '--':
                screen.blit(piece_images[piece],
                            (col * CELL_SIZE, row * CELL_SIZE))

# Main game loop


def main():
    # Calculate CELL_SIZE based on screen size
    CELL_SIZE = min(SCREEN_WIDTH // BOARD_COLS, SCREEN_HEIGHT // BOARD_ROWS)
    piece_images = load_images(CELL_SIZE)

    board = [
        ['black_rook', 'black_horse', 'black_elephant', 'black_guard', 'black_king',
            'black_guard', 'black_elephant', 'black_horse', 'black_rook'],
        ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', 'black_cannon', '--', '--', '--', '--', '--', 'black_cannon', '--'],
        ['black_pawn', '--', 'black_pawn', '--', 'black_pawn',
            '--', 'black_pawn', '--', 'black_pawn'],
        ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
        ['red_pawn', '--', 'red_pawn', '--', 'red_pawn',
            '--', 'red_pawn', '--', 'red_pawn'],
        ['--', 'red_cannon', '--', '--', '--', '--', '--', 'red_cannon', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
        ['red_rook', 'red_horse', 'red_elephant', 'red_guard', 'red_king',
            'red_guard', 'red_elephant', 'red_horse', 'red_rook']
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the board
        draw_board(CELL_SIZE)

        # Draw the pieces
        draw_pieces(board, piece_images, CELL_SIZE)

        pygame.display.flip()


if __name__ == "__main__":
    main()
