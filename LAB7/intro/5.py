import pygame
import math

pygame.init()

# Создаём окно
screen = pygame.display.set_mode((500, 500))

# Загружаем изображение
image = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\ball.png")
image = pygame.transform.scale(image, (50, 50))  # Масштабируем, если нужно

# Получаем прямоугольник изображения
rect = image.get_rect(center=(250, 250))  # Размещаем в центре экрана

angle = 0  # Начальный угол поворота

running = True
while running:
    screen.fill((30, 30, 30))  # Фон

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Вращаем изображение
    rotated_image = pygame.transform.rotate(image, angle)
    
    # Новый прямоугольник, чтобы центр оставался на месте
    new_rect = rotated_image.get_rect(center=rect.center)

    # Рисуем повернутое изображение
    screen.blit(rotated_image, new_rect.topleft)

    # Увеличиваем угол
    angle += 1

    pygame.display.flip()
    pygame.time.delay(20)  # Задержка для плавного вращения

pygame.quit()


