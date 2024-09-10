import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))

def distance(x1, y1, x2, y2):
    pass

def determine_target_prey_type(piece_type):
    if piece_type == 'r':
        return 's'
    elif piece_type == 'p':
        return 'r'
    else:
        return 'p'

def get_target_prey_type_list(target_prey_type):
    pass

def find_nearest_prey(piece):
    prey_type = determine_target_prey_type(piece.type)
    prey_list = get_target_prey_type_list(prey_type)

    pass

def find_prey_direction(piece):
    nearest_prey = find_nearest_prey(piece)
    
    if not nearest_prey:
        return [random.randint([-1, 0, 1]), random.choice([-1, 0, 1])] # IF NO PREY FOUND, GO RANDOM DIRECTION

    direction_to_move = [0, 0] # If none conditons are met, defaults is stay on current x and/or y

    if nearest_prey.y < piece.y: # Above
        direction_to_move[1] = -1
    elif nearest_prey.y > piece.y: # Below
        direction_to_move[1] = 1

    if nearest_prey.x < piece.x: # Left
        direction_to_move[0] = -1
    elif nearest_prey.x > piece.x: # Right
        direction_to_move[0] = 1

    return direction_to_move

class Piece:
    def __init__(self, x, y, piece_type):
        self.x = x
        self.y = y
        self.type = piece_type

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, piece_size, piece_size))

    def move(self):
        direction_to_move = find_prey_direction(self)
        self.x += direction_to_move[0]
        self.y += direction_to_move[1]

    def __repr__(self):
        return f'{self.type}'

    def __eq__(self, other):
        if isinstance(self, other):
            return self.type == other.type

piece_size = 15
all_pieces = []
pieces_per_team = 16
piece_types = ['r', 'p', 's']

for piece_type in piece_types:
    for i in range(pieces_per_team):
        all_pieces.append(Piece(random.randint(0, 800), random.randint(0, 800), piece_type))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((255, 255, 255))

        for piece in all_pieces:
            piece.move()
            piece.draw()

        pygame.display.update()

main()