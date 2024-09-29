import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Screen")

rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(200, 200, 50, 50)

move_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE: 
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect1.y -= move_speed
    if keys[pygame.K_DOWN]:
        rect1.y += move_speed
    if keys[pygame.K_LEFT]:
        rect1.x -= move_speed
    if keys[pygame.K_RIGHT]:
        rect1.x += move_speed

    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (255, 0, 0), rect1)  
    pygame.draw.rect(screen, (0, 255, 0), rect2)  

    pygame.display.flip()

pygame.quit()
