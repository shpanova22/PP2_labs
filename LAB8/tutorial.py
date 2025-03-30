import pygame
import time
import random


pygame.init()

WIDTH=400
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")
clock=pygame.time.Clock()

image_background=pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\AnimatedStreet.png")
image_player = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\Player.png")
image_enemy = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\Enemy.png")

pygame.mixer.music.load(r"C:\Users\Lenovo\Desktop\PP2_labs\Lectures_G2_Week10_racer_resources_background.wav")
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound(r"C:\Users\Lenovo\Desktop\PP2_labs\Lectures_G2_Week10_racer_resources_crash.wav")


font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over", True, "black")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5
        # or
        # self.rect.midbottom = (WIDTH // 2, HEIGHT)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10
        # or
        # self.rect.midbottom = (WIDTH // 2, HEIGHT)

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)


running=True

while running:
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    player.move()

    screen.blit(image_background, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)

        running = False
        screen.fill("red")
        screen.blit(image_game_over, (30,250))
        pygame.display.flip()

        time.sleep(3)
        
    
    pygame.display.flip() # updates the screen
    clock.tick(60) # sets the FPS
    
        

    


