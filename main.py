from pygame import *
from random import randint

FPS = 60
GAME_FINISHED, GAME_RUN = False, True
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
CLOCK = time.Clock()


WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Maze (Labyrinth (Лабиринт))")


mixer.init()

mixer.music.load("music.mp3")
mixer.music.play()


font.init()

font1 = font.SysFont("Arial", 72, True)

win_text = font1.render("Ты победил!", True, (255, 255, 255))
lose_text = font1.render("Ты проиграл!", True, (255, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, img, position, size, speed):
        super().__init__()
        
        self.image = transform.smoothscale(
            image.load(img),
            size
        )
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        
        self.speed = speed
        self.width, self.height = size
        
    def reset(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WINDOW_HEIGHT - self.height:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < WINDOW_WIDTH - self.width:
            self.rect.x += self.speed
    
class Enemy(GameSprite):
    def __init__(self, img, position, size, speed):
        super().__init__(img, position, size, speed)
        
        self.direction_x, self.direction_y = "RIGHT", "TOP"
        self.start_x, self.end_x = None, None
        self.start_y, self.end_y = None, None
    
    def set_track_x(self, start_x, end_x):
        self.start_x, self.end_x = start_x, end_x
    
    def set_track_y(self, start_y, end_y):
        self.start_y, self.end_y = start_y, end_y
    
    def update(self):

        if self.start_x != None and self.end_x != None:
            if self.direction_x == "RIGHT":
                if self.rect.x < self.end_x:  
                    self.rect.x += self.speed
                else: 
                    self.direction_x = "LEFT"
            else: 
                if self.rect.x > self.start_x:
                    self.rect.x -= self.speed
                else: 
                    self.direction_x = "RIGHT"

        if self.start_y != None and self.end_y != None:
            if self.direction_y == "TOP":
                if self.rect.y < self.end_y:  
                    self.rect.y += self.speed
                else:
                    self.direction_y = "BOTTOM"
            else: 
                if self.rect.y > self.start_y: 
                    self.rect.y -= self.speed
                else:
                    self.direction_y = "TOP"
    
class Wall(sprite.Sprite):
    def __init__(self, position, size, color):
        super().__init__()
        
        self.image = Surface(size)
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        
        self.width, self.height = size
        
    def draw(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))

bg = GameSprite(img="bg.jpg",
                position=(0, 0),
                size=(WINDOW_WIDTH, WINDOW_HEIGHT),
                speed=0)

player = Player(img="player.png",
                position=(5, 400),
                size=(24, 48),
                speed=5)

enemy1 = Enemy(img="enemy.png",
               position=(400, 200),
               size=(24, 48),
               speed=5)

enemy1.set_track_x(100, 500)

enemy_group = sprite.Group()
enemy_group.add([enemy1])

wall1 = Wall(position=(100, 0),
             size=(10, 180),
             color=(100, 100, 100))

wall2 = Wall(position=(100, 250),
             size=(10, 200),
             color=(100, 100, 100))

wall3 = Wall(position=(100, 410),
             size=(200, 10),
             color=(100, 100, 100))

wall4 = Wall(position=(100, 170),
             size=(500, 10),
             color=(100, 100, 100))

wall5 = Wall(position=(100, 250),
             size=(100, 10),
             color=(100, 100, 100))

wall6 = Wall(position=(200, 250),
             size=(10, 100),
             color=(100, 100, 100))

wall7 = Wall(position=(200, 350),
             size=(100, 10),
             color=(100, 100, 100))

wall8 = Wall(position=(270, 250),
             size=(10, 50),
             color=(100, 100, 100))

wall9 = Wall(position=(270, 250),
             size=(330, 10),
             color=(100, 100, 100))

wall10 = Wall(position=(300, 350),
             size=(10, 200),
             color=(100, 100, 100))

wall11 = Wall(position=(360, 350),
             size=(100, 10),
             color=(100, 100, 100))

wall12 = Wall(position=(360, 350),
             size=(10, 200),
             color=(100, 100, 100))

wall13 = Wall(position=(370, 350),
             size=(300, 10),
             color=(100, 100, 100))

wall14 = Wall(position=(270, 290),
             size=(400, 10),
             color=(100, 100, 100))



win = Wall(position=(630, 0),
             size=(20, 480),
             color=(0, 100, 0))

walls_group = sprite.Group()
walls_group.add([wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14])
win_group = sprite.Group()
win_group.add([win])
while GAME_RUN:
    
    for ev in event.get():
        if ev.type == QUIT:
            GAME_RUN = False

    bg.reset()
    player.reset()
    enemy_group.draw(WINDOW)
    walls_group.draw(WINDOW)
    win_group.draw(WINDOW)
    
    r = randint(200, 255)
    g = randint(200, 255)
    b = randint(200, 255)
    
    win_text = font1.render("Ты победил!", True, (0, g, 0))
    lose_text = font1.render("Ты проиграл!", True, (r, 0, 0))
    fps_text = font1.render(str(int(CLOCK.get_fps())), True, (255, 255, 255))
    coordinate_player = font1.render(str(player.rect.x) + " " + str(player.rect.y), True, (255, 255, 255))
    coordinate_enemy = font1.render(str(enemy1.rect.x) + " " + str(enemy1.rect.y), True, (255, 255, 255))
    
    keys = key.get_pressed()

    if keys[K_2]:
        WINDOW.blit(coordinate_enemy, (0, 0))
    if keys[K_1]:
        WINDOW.blit(coordinate_player, (0, 0))
    if keys[K_0]:
        WINDOW.blit(fps_text, (0, 0))

    if sprite.spritecollide(player, enemy_group, False):
        WINDOW.blit(lose_text, (WINDOW_WIDTH / 2 - lose_text.get_width() / 2, 
                                WINDOW_HEIGHT / 2 - lose_text.get_height() / 2))
        GAME_FINISHED = True
        
    if sprite.spritecollide(player, walls_group, False):
        WINDOW.blit(lose_text, (WINDOW_WIDTH / 2 - lose_text.get_width() / 2, 
                                WINDOW_HEIGHT / 2 - lose_text.get_height() / 2))
        GAME_FINISHED = True
    
    if sprite.spritecollide(player, win_group, False):
        WINDOW.blit(win_text, (WINDOW_WIDTH / 2 - win_text.get_width() / 2, 
                                WINDOW_HEIGHT / 2 - win_text.get_height() / 2))
        GAME_FINISHED = True

    if not GAME_FINISHED:
        player.update()
        enemy_group.update()
    
    display.update()
    CLOCK.tick(FPS)



