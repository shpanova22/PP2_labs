import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

running = True
is_red = True

x = 30
y = 30
image = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\ball.png")

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: 
        x += 5
    if keys[pygame.K_LEFT]: 
        x -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if keys[pygame.K_UP]:
        y -= 5
    
    
    
    if is_red:
        screen.fill(red)  
    else:
        screen.fill(blue)  

    screen.blit(image, (x, y))

    pygame.display.flip()
    clock.tick(60)