import pygame
from pygame.locals import *
import random

pygame.init()

# Windoww
game_width = 500
game_height = 500
screen_size = (game_width, game_height)
game_window = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Space Shooter')

# Colors
red = (200, 0, 0)
white = (255, 255, 255)

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.lives = 3
        self.score = 0

        image = pygame.image.load('images/spaceship.png')
        image_scale = 40 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        scaled_size = (new_width, new_height)
        self.image = pygame.transform.scale(image, scaled_size)

        self.rect = self.image.get_rect()

        self.invincibility_frames = 0
        damage_image = pygame.image.load('images/damage.png')
        image_scale = 80 / damage_image.get_rect().width
        new_width = damage_image.get_rect().width * image_scale
        new_height = damage_image.get_rect().height * image_scale
        scaled_size = (new_width, new_height)
        self.damage_image = pygame.transform.scale(damage_image, scaled_size)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        if self.invincibility_frames > 0:
            self.invincibility_frames -= 1

    def draw_damage(self):
        if self.invincibility_frames > 0:
            damage_x = self.x - self.image.get_width() / 3
            damage_y = self.y - self.image.get_height() / 2
            game_window.blit(self.damage_image, (damage_x, damage_y))


class Meteor(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        color = random.choice(['meteorBrown', 'meteorGrey'])
        size = random.choice(['big', 'med', 'small', 'tiny'])
        num = random.randint(1, 2)
        self.image = pygame.image.load(f'images/Meteors/{color}_{size}{num}.png')


        if size == 'big':
            self.hits = 4
            self.points = 4
        elif size == 'med':
            self.hits = 3
            self.points = 3
        elif size == 'small':
            self.hits = 2
            self.points = 2
        elif size == 'tiny':
            self.hits = 1
            self.points = 1

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):

        self.rect.y += 1

        if self.rect.y % 20 == 0:
            self.image = pygame.transform.rotate(self.image, 90)

        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()

            if player.invincibility_frames == 0:
                player.lives -= 1

                player.invincibility_frames = 50

        if pygame.sprite.spritecollide(self, missile_group, True):
            self.hits -= 1

            if self.hits == 0:
                player.score += self.points

        if self.rect.top > game_height or self.hits == 0:
            self.kill()


class Missile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(x - 2, y, 4, 8)

    def draw(self):
        for w in range(self.rect.width):
            for h in range(self.rect.height):
                game_window.set_at((self.rect.x + w, self.rect.y - h), white)

    def update(self):

        self.rect.y -= 5

        if self.rect.bottom > 0:
            self.draw()
        else:
            self.kill()

player_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()
missile_group = pygame.sprite.Group()

bg = pygame.image.load('images/background.png')

player_x = 250
player_y = 450
player = Player(player_x, player_y)
player_group.add(player)

missile_cooldown = 200
last_missile = pygame.time.get_ticks() - missile_cooldown

def write_text(str, color, x, y):
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(str, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    game_window.blit(text, text_rect)

def create_meteor():

    meteor_x = random.randint(50, game_width - 50)

    meteor_y = 0

    meteor = Meteor(meteor_x, meteor_y)
    meteor_group.add(meteor)

create_meteor()

clock = pygame.time.Clock()
fps = 120
running = True
loop_ctr = 0
while running:

    loop_ctr += 1

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[K_LEFT] and player.rect.left > 0:
        player.x -= 2
    elif keys[K_RIGHT] and player.rect.right < game_width:
        player.x += 2

    if keys[K_SPACE]:

        current_time = pygame.time.get_ticks()
        if current_time - last_missile > missile_cooldown:

            missile = Missile(player.rect.centerx, player.rect.y)
            missile_group.add(missile)

            last_missile = current_time

    for bg_x in range(0, game_width, bg.get_width()):
        for bg_y in range(0, game_height, bg.get_height()):
            game_window.blit(bg, (bg_x ,bg_y))

    player_group.update()
    player_group.draw(game_window)

    player.draw_damage()

    missile_group.update()

    if loop_ctr == 100:

        create_meteor()

        loop_ctr = 0

    meteor_group.update()
    meteor_group.draw(game_window)

    write_text(f'Lives: {player.lives}', white, game_width / 8, 20)
    write_text(f'Score: {player.score}', white, game_width * 7 / 8, 20)

    pygame.display.update()

    gameover = player.lives == 0
    while gameover:

        clock.tick(fps)

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()

        gameover_str = f'Game over. Do you want to play again? (Y or N)'
        write_text(gameover_str, red, game_width / 2, game_height / 2)

        keys = pygame.key.get_pressed()
        if keys[K_y]:

            player_group.empty()
            meteor_group.empty()
            missile_group.empty()

            create_meteor()

            player = Player(player_x, player_y)
            player_group.add(player)

            gameover = False

        elif keys[K_n]:
            running = False
            break

        pygame.display.update()

pygame.quit()

