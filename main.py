import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('mancala')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
holes = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
turn = "first player"
game_end = False

def draw_board():
    global holes

    pygame.draw.rect(gameDisplay, black, pygame.Rect(40, 165, 720, 260), 1) # board

    # first row
    hole_1_pos = (188, 358)
    hole_2_pos = (273, 358)
    hole_3_pos = (358, 358)
    hole_4_pos = (443, 358)
    hole_5_pos = (525, 358)
    hole_6_pos = (607, 358)

    pygame.draw.circle(gameDisplay, black, hole_1_pos, 38, 1)
    message_display(str(holes[1]), hole_1_pos)

    pygame.draw.circle(gameDisplay, black, hole_2_pos, 38, 1)
    message_display(str(holes[2]), hole_2_pos)

    pygame.draw.circle(gameDisplay, black, hole_3_pos, 38, 1)
    message_display(str(holes[3]), hole_3_pos)

    pygame.draw.circle(gameDisplay, black, hole_4_pos, 38, 1)
    message_display(str(holes[4]), hole_4_pos)

    pygame.draw.circle(gameDisplay, black, hole_5_pos, 38, 1)
    message_display(str(holes[5]), hole_5_pos)

    pygame.draw.circle(gameDisplay, black, hole_6_pos, 38, 1)
    message_display(str(holes[6]), hole_6_pos)

    # second row
    hole_13_pos =(188,240)
    hole_12_pos =(273,240)
    hole_11_pos =(358,240)
    hole_10_pos =(443,240)
    hole_9_pos = (525,240)
    hole_8_pos = (607,240)

    pygame.draw.circle(gameDisplay, black, hole_13_pos, 38, 1)
    message_display(str(holes[13]), hole_13_pos)

    pygame.draw.circle(gameDisplay, black, hole_12_pos, 38, 1)
    message_display(str(holes[12]), hole_12_pos)

    pygame.draw.circle(gameDisplay, black, hole_11_pos, 38, 1)
    message_display(str(holes[11]), hole_11_pos)

    pygame.draw.circle(gameDisplay, black, hole_10_pos, 38, 1)
    message_display(str(holes[10]), hole_10_pos)

    pygame.draw.circle(gameDisplay, black, hole_9_pos, 38, 1)
    message_display(str(holes[9]), hole_9_pos)

    pygame.draw.circle(gameDisplay, black, hole_8_pos, 38, 1)
    message_display(str(holes[8]), hole_8_pos)

    # left side pool
    second_player_pool = (90 ,295)
    pygame.draw.ellipse(gameDisplay, black, pygame.Rect(60,190, 70, 220), 1)
    message_display(str(holes[0]), second_player_pool)

    # right side pool
    first_player_pool = (695 ,295)
    pygame.draw.ellipse(gameDisplay, black, pygame.Rect(665,190, 70, 220), 1)
    message_display(str(holes[7]), first_player_pool)

    does_first_plyers_has_sedds = False
    does_second_plyers_has_sedds = False
    for i in range(14):
        if holes[i] > 0:
            if 1 <= i <= 6:
                does_first_plyers_has_sedds = True
            if 8 <= i <= 13:
                does_second_plyers_has_sedds = True

    if not does_first_plyers_has_sedds or not does_second_plyers_has_sedds:
        end_game()

def end_game():
    global game_end
    if holes[7]> holes[0]:
        message_display("first player won", (display_width/6, display_width/6))
    else:
        message_display("second player won", (display_width/6, display_width/6))
    game_end = True




def play_turn(key):
    global turn, game_end
    print("important key pressed: {0}".format(key))

    start_hole = key
    enemy_pool = 0
    my_pool = 7
    my_holes = [1,6]
    if turn == "second player":
        start_hole = start_hole + (7-start_hole)*2 # fit the pos for the second player
        enemy_pool = 7
        my_pool = 0
        my_holes = [8, 13]

    number_of_seeds = holes[start_hole]
    holes[start_hole] = 0
    curr_hole = (start_hole + 1) % 14
    if number_of_seeds == 0 or game_end:
        return

    while number_of_seeds != 0:
        if curr_hole == enemy_pool:
            curr_hole += 1
        holes[curr_hole] += 1
        number_of_seeds -= 1
        curr_hole = (curr_hole + 1) % 14

    last_seed_hole = ((14 + curr_hole -1 ) % 14)
    if my_holes[0] <= last_seed_hole <= my_holes[1] and holes[last_seed_hole] == 1:
        opposite_hole = last_seed_hole + (7-last_seed_hole)*2
        holes[my_pool] += holes[opposite_hole]
        holes[opposite_hole] = 0

    if last_seed_hole != my_pool:
        next_turn()



def next_turn():
    global turn

    if turn == "first player":
        turn = "second player"
    else:
        turn= "first player"


def get_key(key):
    if key == pygame.K_1:
        return 1
    if key == pygame.K_2:
        return 2
    if key == pygame.K_3:
        return 3
    if key == pygame.K_4:
        return 4
    if key == pygame.K_5:
        return 5
    if key == pygame.K_6:
        return 6
    else:
        return -1

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, pos):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = pos
    gameDisplay.blit(TextSurf, TextRect)

def game_loop():
    is_exit = False
    while not is_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_exit = True
            if event.type == pygame.KEYDOWN:
                key = get_key(event.key)
                if 1 <= key <= 6:
                    play_turn(key)
            print(event)
            print(turn)

        gameDisplay.fill(white)
        draw_board()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()