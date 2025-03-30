import pygame #для создания игры импортируем модуль pygame
import time   #для задержки после столкновения импортируем модуль time
import random #для случайного появления монет и врагов импортируем модуль random

pygame.init() #инициализирует все модули Pygame

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создаёт окно.
pygame.display.set_caption("Car Racing") #устанавливает заголовок окна.
clock = pygame.time.Clock() #объект для контроля FPS

# Загрузка изображений
image_background = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\AnimatedStreet.png")
image_player = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\Player.png")
image_enemy = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\Enemy.png")
image_coin = pygame.image.load(r"C:\Users\Lenovo\Desktop\PP2_labs\pngimg.com - coin_PNG36871.png")
image_coin = pygame.transform.scale(image_coin, (30, 30)) #уменьшаем монету до 30×30 пикселей.



# Музыка и звуки
pygame.mixer.music.load(r"C:\Users\Lenovo\Desktop\PP2_labs\Lectures_G2_Week10_racer_resources_background.wav") #загружаем фоновую музыку.
pygame.mixer.music.play(-1) #проигрываем бесконечно (-1).
sound_crash = pygame.mixer.Sound(r"C:\Users\Lenovo\Desktop\PP2_labs\Lectures_G2_Week10_racer_resources_crash.wav")#загружаем звук аварии.

# Шрифты
font = pygame.font.SysFont("Verdana", 60) #создаёт шрифт Verdana, 60px.
small_font = pygame.font.SysFont("Verdana", 20)
image_game_over = font.render("Game Over", True, "black") #рисует текст "Game Over".



# Параметры фона
background_y = 0 #стартовая координата фона.
scroll_speed = 5 #скорость прокрутки.
score = 0 #начальный счёт (количество собранных монет).




class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()#вызывает конструктор pygame.sprite.Sprite, чтобы объект стал спрайтом.
        self.image = image_player #вызывает конструктор pygame.sprite.Sprite, чтобы объект стал спрайтом.
        self.rect = self.image.get_rect() #оздаёт прямоугольник (bounding box) вокруг изображения. Этот прямоугольник помогает управлять позицией объекта.
        self.rect.x = WIDTH // 2 - self.rect.w // 2 #Размещает игрока по центру экрана по оси X. WIDTH // 2 — центр экрана. - self.rect.w // 2 — сдвигает левый край машины к центру.
        self.rect.y = HEIGHT - self.rect.h #Начальная позиция по Y. Мы отнимаем высоту игрока, чтобы он стоял на нижнем краю экрана. Если не отнимать высоту, то игрок начнётся за границей экрана.
        self.speed = 5 #скорость игрока.

    def move(self): #move() — управление машиной
        keys = pygame.key.get_pressed()#Получает список всех нажатых клавиш. Если клавиша нажата, её значение будет True, иначе — False.
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0) #move_ip(dx, dy) (перемещение на dx, dy пикселей).
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)

        # Ограничения движения
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = self.rect.h   # Ограничение, чтобы машина не поднималась слишком высоко


class Coin(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, WIDTH-30)  # Случайная позиция по ширине
        self.rect.y = random.randint(0, HEIGHT // 3)  # Ограничиваем по высоте (верхняя треть экрана)
        self.speed = scroll_speed  # Движение вниз
        
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.kill() #Если вышла за экран → kill() (удаляем объект).


   

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)# Появляется в случайном месте 
        self.rect.y = 0 #сверху
        self.speed = random.randint(5, 10) #Двигается вниз со случайной скоростью.

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.kill()


# Создание объектов
player = Player() #Создаёт объект игрока (Player).
all_sprites = pygame.sprite.Group() #это специальная структура, которая позволяет управлять сразу несколькими спрайтами.В эту группу добавляются все объекты, чтобы можно было их удобно обновлять и рисовать.
enemy_sprites = pygame.sprite.Group()#Создаёт группу врагов (машин-препятствий). В эту группу добавляются только машины-препятствия (Enemy), чтобы легко проверять столкновения игрока с врагами.
coin_sprites = pygame.sprite.Group() #Создаёт группу монет. В эту группу добавляются только монеты (Coin), чтобы можно было проверять их сбор игроком.

all_sprites.add(player)#добавляет игрока в общую группу спрайтов. Теперь игрок автоматически обновляется и рисуется вместе с остальными объектами.

# Запускаем игру
running = True
frame_count = 0  # Счетчик кадров для появления объектов

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()

    # Прокрутка фона
    background_y += scroll_speed # Фон смещается вниз (background_y увеличивается).
    if background_y >= HEIGHT: # Когда фон доходит до конца (background_y >= HEIGHT), он сбрасывается (background_y = 0), создавая бесконечный эффект прокрутки.
        background_y = 0

    screen.blit(image_background, (0, background_y - HEIGHT)) #Рисует фон немного выше экрана, так что он появится плавно, когда background_y увеличится.background_y - HEIGHT означает, что второй фон размещается ровно над первым.Например, если HEIGHT = 600, то когда background_y = 100, фон рисуется на (0, -500), постепенно появляясь сверху.
    screen.blit(image_background, (0, background_y)) # Рисует фон в обычном положении, то есть в background_y. Этот фон плавно смещается вниз, создавая иллюзию движения дороги.

    #Так как фон рисуется дважды, один плавно заменяет другой, создавая эффект непрерывного движения.



    # Генерация новых монет и машин
    frame_count += 1 #Счётчик frame_count увеличивается на 1 каждый кадр.
    if frame_count % 50 == 0:  # Каждые 50 кадров создаем монету
        new_coin = Coin(player)
        coin_sprites.add(new_coin)#coin_sprites — это группа, хранящая все монеты в игре,add(new_coin) добавляет созданную монету в эту группу.
        all_sprites.add(new_coin)#all_sprites — это общая группа всех объектов (игрока, монет, врагов и т. д.).Добавление монеты в all_sprites нужно, чтобы она автоматически обновлялась и рисовалась в игровом цикле

    if frame_count % 100 == 0:  # Каждые 100 кадров создаем машину-препятствие
        new_enemy = Enemy() #создаёт новый объект врага (машины-препятствия) с помощью класса Enemy.
        enemy_sprites.add(new_enemy)
        all_sprites.add(new_enemy)

    # Движение объектов
    for entity in all_sprites: #Перебирает все спрайты в all_sprites.
        entity.move() #Вызывает move() у каждого объекта (игрока, монет, врагов).
        screen.blit(entity.image, entity.rect) #Рисует (blit) все игровые объекты на экране.



    # Проверка столкновения с монетами
    collected_coins = pygame.sprite.spritecollide(player, coin_sprites, True)#spritecollide() проверяет, какие монеты касаются игрока.Если монета собрана, она исчезает (True – удалить объект).
    score += len(collected_coins)#К счёту добавляется количество собранных монет (len(collected_coins)).

    # Проверка столкновения с врагами
    if pygame.sprite.spritecollideany(player, enemy_sprites): #spritecollideany() проверяет, столкнулся ли игрок с врагом.
        sound_crash.play()#оспроизводится звук аварии
        time.sleep(1)#Игра останавливается на 1 секунду

        running = False
        screen.fill("red")#Экран заполняется красным
        screen.blit(image_game_over, (30, 250))#Выводится надпись "Game Over".
        pygame.display.flip()
        time.sleep(3)#После 3 секунд ожидания (time.sleep(3)) игра завершается.

    # Отображение счета
    score_text = small_font.render(f"Coins: {score}", True, "black")
    screen.blit(score_text, (WIDTH - 100, 10)) #Отображает его в правом верхнем углу

    pygame.display.flip()#обновляет экран
    clock.tick(60)  # ограничивает FPS до 60, чтобы игра шла плавно.это количество кадров, которое игра отображает за одну секунду. Чем выше FPS, тем плавнее выглядит анимация.
