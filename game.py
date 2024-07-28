import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGTH = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("---------------------------------------------------------------------------Dodge the ghosts---------------------------------------------------------------------------")

BG = pygame.image.load("house.jpg")

PLAYER_WIDTH = 50
PLAYER_HEIGTH = 50
PLAYER_VEL = 5
GHOST_WIDTH = 10
GHOST_HEIGHT = 20
GHOST_VEL = 3
FONT = pygame.font.SysFont("simple", 50)

def draw(player, elapsed_time, ghost):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Score: {round(elapsed_time)}", 1, "white")
    WIN.blit(time_text, (10, 10))
   
    pygame.draw.rect(WIN, "green" , player)    
 
    for ghost in ghost:
        pygame.draw.rect(WIN,"white", ghost)

    pygame.display.update()
   
def main():  
    run = True                   
    
    player = pygame.Rect(200, HEIGTH - PLAYER_HEIGTH,
                         PLAYER_WIDTH, PLAYER_HEIGTH)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    ghost_add_increment = 2000
    ghost_count = 0

    ghosts = []
    hit = False

    while run:      
        ghost_count += clock.tick(70)
        elapsed_time = time.time() - start_time

        if ghost_count > ghost_add_increment:
            for _ in range(5):
                ghost_x = random.randint(0, WIDTH - GHOST_WIDTH)
                ghost = pygame.Rect(ghost_x, -GHOST_HEIGHT, GHOST_WIDTH, GHOST_HEIGHT)
                ghosts.append(ghost)

            ghost_add_increment = max(200, ghost_add_increment - 50)
            ghost_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break    

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
           player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
           player.x += PLAYER_VEL

        for ghost in ghosts[:]:
            ghost.y += GHOST_VEL
            if ghost.y > HEIGTH:
                ghosts.remove(ghost)
            elif ghost.y >= player .y and ghost.colliderect(player):
                ghost.remove(ghost)
                hit = True
                break

        draw(player, elapsed_time, ghosts)

    pygame.quit()

if __name__ == "__main__":
    main()