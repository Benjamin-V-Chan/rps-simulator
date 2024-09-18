import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

def distance(x1, y1, x2, y2):
    x_distance = x1-x2
    y_distance = y1-y2
    return (x_distance ** 2 + y_distance ** 2) ** 0.5

def collision(piece_one, piece_two):
    if (piece_one.x < piece_two.x + piece_size and 
        piece_one.x + piece_size > piece_two.x and
        piece_one.y < piece_two.y + piece_size and 
        piece_one.y + piece_size > piece_two.y):
        return True
    return False

def determine_prey_type(piece_type):
    if piece_type == 'r':
        return 's'
    elif piece_type == 'p':
        return 'r'
    else:
        return 'p'

def determine_predator_type(piece_type):
    if piece_type == 'r':
        return 'p'
    elif piece_type == 'p':
        return 's'
    else:
        return 'r'
    
def get_prey_list(piece):
    prey_type = determine_prey_type(piece.type)
    target_prey_type_list = []
    for piece in all_pieces:
        if piece.type == prey_type:
            target_prey_type_list.append(piece)
    return target_prey_type_list

def find_nearest_prey(piece):
    prey_list = get_prey_list(piece)

    closest_prey = None
    closest_prey_distance = None

    for prey in prey_list:
        if collision(piece, prey):
            prey.reassign_type_to_predator()

        else:
            prey_distance = distance(piece.x, piece.y, prey.x, prey.y)
            if closest_prey:
                if prey_distance < closest_prey_distance:
                    closest_prey = prey
                    closest_prey_distance = prey_distance
            else:
                closest_prey = prey
                closest_prey_distance = prey_distance
    
    return closest_prey
    
def find_prey_direction(piece):
    nearest_prey = find_nearest_prey(piece)
    
    if not nearest_prey:
        return [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])] # IF NO PREY FOUND, GO RANDOM DIRECTION

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

def determine_piece_color(piece_type):
    if piece_type == 'r':
        return (0, 0, 255)
    elif piece_type == 'p':
        return (0, 255, 0)
    else:
        return (255, 0, 0)

class Piece:
    def __init__(self, x, y, piece_type):
        self.x = x
        self.y = y
        self.type = piece_type

    def move(self):
        direction_to_move = find_prey_direction(self)
        self.x += direction_to_move[0]
        self.y += direction_to_move[1]

    def draw(self):
        color = determine_piece_color(self.type)
        pygame.draw.rect(screen, color, (self.x, self.y, piece_size, piece_size))

    def reassign_type_to_predator(self):
        predator_type = determine_predator_type(self.type)
        self.type = predator_type

    def __repr__(self):
        return f'{self.type}'

    def __eq__(self, other):
        if isinstance(self, other):
            return self.type == other.type

fps = 30

piece_size = 15
all_pieces = []
pieces_per_team = 10
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
        clock.tick(fps)

main()