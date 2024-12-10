import pygame
import random

pygame.init()

# library of game constants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HEIGHT = 500
player_images = {
    0: pygame.image.load('goku.png'),
    10: pygame.image.load('sgoku.png'),
    20: pygame.image.load('3goku.png'),
    30: pygame.image.load('Ggoku.png'),
    40: pygame.image.load('Bgoku.png'),
    50: pygame.image.load('Ugoku.png')
}
player = pygame.transform.scale(player_images[0], (90, 70))
fps = 60
font = pygame.font.Font('freesansbold.ttf', 10)
timer = pygame.time.Clock()
score = 0
high_score = 0
game_over = False

# Load the background image
background_image = pygame.image.load('tower.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# game variables
player_x = 170
player_y = 400
platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3
facing_right = True  # New variable to track player direction

# create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Goku Jump')

# check for collisions with blocks
def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 20, player_y + 60, 35, 5]) and not j and y_change > 0:
            j = True
    return j

# update player y position every loop
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 9
    gravity = 0.4
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos

# handle movement of platforms
def update_platforms(my_list, y_pos, change):
    global score
    global high_score
    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
            score += 1
            # Update high_score if the current score is higher
            if score > high_score:
                high_score = score
    return my_list

# New function to update player image based on direction and score
def update_player_image():
    global player, facing_right, score
    image_key = (score // 10) * 10
    if image_key > 50:
        image_key = 50  # Use the last image for scores above 50
    current_image = player_images[image_key]

    # Calculate the aspect ratio of the original image
    original_width, original_height = current_image.get_size()
    aspect_ratio = original_width / original_height

    # Set the desired height and calculate the width based on the aspect ratio
    desired_height = 70
    desired_width = int(desired_height * aspect_ratio)

    # Scale the image while maintaining the aspect ratio
    scaled_image = pygame.transform.scale(current_image, (desired_width, desired_height))

    if x_change > 0 or (x_change == 0 and facing_right):
        facing_right = True
        player = scaled_image
    else:
        facing_right = False
        player = pygame.transform.flip(scaled_image, True, False)

running = True
while running:
    timer.tick(fps)
    screen.blit(background_image, (0, 0))  # Draw the background image
    screen.blit(player, (player_x, player_y))
    blocks = []
    score_text = font.render('Score:' + str(score), True, black)
    screen.blit(score_text, (320, 20))
    high_score_text = font.render('Highscore:' + str(high_score), True, black)
    screen.blit(high_score_text, (280, 0))

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, black, platforms[i], 0, 3)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0 
                player_x = 170
                player_y = 400
                platforms = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
            if event.key == pygame.K_a:
                x_change = -player_speed
            if event.key == pygame.K_d:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0

    if player_y < 440:
        player_y = update_player(player_y)
    else:
        game_over = True
        y_change = 0

    player_x += x_change
    jump = check_collisions(blocks, jump)
    platforms = update_platforms(platforms, player_y, y_change)

    if player_x < -20:
        player_x = -20
    elif player_x > 330:
        player_x = 330

    # Update player image based on movement direction and score
    update_player_image()

    pygame.display.flip()

pygame.quit()