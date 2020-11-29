import pygame
import random
import math
from pygame import mixer
import sys

# Initialize pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('background.jpg')
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('battleship.png')
pygame.display.set_icon(icon)


# Player class
class Player:
    def __init__(self, playerimg, playerX, playerY, playerX_change, playerY_change):
        self.playerimg = playerimg
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = playerX_change
        self.playerY_change = playerY_change

    def player(self, x, y):
        screen.blit(self.playerimg, (x, y))

    def isCollision(self, objectX, objectY):
        distance = math.sqrt(math.pow(objectX - self.playerX, 2) + math.pow(objectY - self.playerY, 2))
        if distance < 27:
            return True
        else:
            return False



# Enemy class
class Enemy:
    def __init__(self, enemyimg, enemyX, enemyY, enemyX_change, enemyY_change, enemy_power):
        self.enemyimg = enemyimg
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change
        self.enemyY_change = enemyY_change
        self.enemy_power = enemy_power
    def enemy(self, x, y):
        screen.blit(self.enemyimg, (x, y))
    def isCollision(self, bulletX, bulletY):
        distance = math.sqrt(math.pow(bulletX - self.enemyX, 2) + math.pow(bulletY - self.enemyY, 2))
        if distance < 27:
            return True
        else:
            return False



# Bullet class
# ready : not firing state
# fire : fired state
class Bullet:
    def __init__(self, bulletimg, bulletX, bulletY, bulletX_change, bulletY_change, bullet_state, bullet_damage):
        self.bulletimg = bulletimg
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bulletX_change = bulletX_change
        self.bulletY_change = bulletY_change
        self.bullet_state = bullet_state
        self.bullet_damage = bullet_damage

    def fire_bullet(self, x, y):
        self.bullet_state = "fire"
        screen.blit(self.bulletimg, (x + 16, y + 10))


def draw_text(text, color, x, y, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_input = font.render(text, True, color)
    screen.blit(text_input, (x, y))


def text_to_button(button_text, color, X, Y, width, height, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_input = font.render(button_text, True, color)
    textX = X + (width / 2) - 40
    textY = Y + (height / 2) - 8
    screen.blit(text_input, (textX, textY))


def main_menu():
    click = False
    while True:
        screen.fill((0, 0, 0))
        draw_text('Game Menu', (255, 255, 255), 290, 5, 40)
        mx, my = pygame.mouse.get_pos()
        new_game_button = pygame.Rect(300, 100, 200, 50)
        exit_game_button = pygame.Rect(300, 200, 200, 50)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
        if new_game_button.collidepoint((mx, my)):
            if click:
                main_game()
        if exit_game_button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (0, 0, 255), new_game_button)
        pygame.draw.rect(screen, (0, 0, 255), exit_game_button)
        text_to_button("New Game", (255, 255, 255), 300, 100, 200, 50, 20)
        text_to_button("Exit Game", (255, 255, 255), 300, 200, 200, 50, 20)
        click = False
        pygame.display.update()


def game_over_menu():
    click = False
    while True:
        screen.fill((0, 0, 0))
        draw_text('Game Over', (255, 255, 255), 290, 5, 40)
        mx, my = pygame.mouse.get_pos()
        new_game_button = pygame.Rect(300, 100, 200, 50)
        exit_game_button = pygame.Rect(300, 200, 200, 50)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    click = True
        if new_game_button.collidepoint((mx, my)):
            if click:
                main_game()
        if exit_game_button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255, 0, 0), new_game_button)
        pygame.draw.rect(screen, (255, 0, 0), exit_game_button)
        text_to_button("New Game", (255, 255, 255), 300, 100, 200, 50, 20)
        text_to_button("Exit Game", (255, 255, 255), 300, 200, 200, 50, 20)
        click = False
        pygame.display.update()


def show_score(score_value, x, y):
    font = pygame.font.Font('freesansbold.ttf', 20)
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Game Loop
def main_game():
    player1 = Player(pygame.image.load('spaceship.png'), 370, 480, 0, 0)
    enemies = []
    num_of_enemies = 3
    for i in range(num_of_enemies):
        enemies.append(Enemy(pygame.image.load('ufo.png'), random.randint(0, 736), 0, 0, 0.3, 5))
    for i in range(num_of_enemies):
        enemies.append(Enemy(pygame.image.load('asteroid.png'), random.randint(0, 736), 0, 0, 0.1, 10))
    for i in range(num_of_enemies):
        enemies.append(Enemy(pygame.image.load('ufo2.png'), random.randint(0, 736), random.randint(50, 150), 0, 0.2, 15))
    bullet_level_1 = Bullet(pygame.image.load('bullet.png'), 0, 480, 0, 3, "ready", 1)
    bullet_level_2 = Bullet(pygame.image.load('bulletlevel2.png'), 0, 480, 0, 3, "ready", 5)
    # score
    score_value = 0
    # background sound
    mixer.music.load("background.wav")
    mixer.music.play(-1)
    while True:
        screen.fill((0, 0, 0))
        # background image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if keystroke is pressed check whether it's right or left || KeyDown means pressing that button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.playerX_change = -0.6
                if event.key == pygame.K_RIGHT:
                    player1.playerX_change = 0.6
                if event.key == pygame.K_UP:
                    player1.playerY_change = -0.6
                if event.key == pygame.K_DOWN:
                    player1.playerY_change = 0.6
                if event.key == pygame.K_SPACE:
                    if bullet_level_2.bullet_state == "ready":
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()
                        bullet_level_2.bulletX = player1.playerX
                        bullet_level_2.bulletY = player1.playerY
                        bullet_level_2.fire_bullet(bullet_level_2.bulletX, bullet_level_2.bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player1.playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player1.playerY_change = 0

        # update the X position of the player
        player1.playerX += player1.playerX_change
        if player1.playerX <= 0:
            player1.playerX = 0
        elif player1.playerX >= 736:
            player1.playerX = 736
        # update the Y position of the Player
        player1.playerY += player1.playerY_change
        if player1.playerY <= 0:
            player1.playerY = 0
        elif player1.playerY >= 536:
            player1.playerY = 536

        # update the Y position of the enemy
        for enemy in enemies:
            # Game over
            collision_with_player = enemy.isCollision(player1.playerX, player1.playerY)
            if collision_with_player:
                mixer.music.pause()
                game_over_menu()
            enemy.enemyY += enemy.enemyY_change
            if enemy.enemyY <= 0:
                enemy.enemyY = -500
                enemy.enemyY += enemy.enemyY_change
            elif enemy.enemyY >= 736:
                enemy.enemyY = -500

            # collision with bullet
            collision = enemy.isCollision(bullet_level_2.bulletX, bullet_level_2.bulletY)
            if collision:
                explosion_sound = mixer.Sound("explosion.wav")
                explosion_sound.play()
                bullet_level_2.bulletY = player1.playerY
                bullet_level_2.bullet_state = "ready"
                score_value += bullet_level_2.bullet_damage
                enemy.enemy_power -= bullet_level_2.bullet_damage
                if enemy.enemy_power == 0:
                    # when enemy dies, trigger something
                    enemy.enemyY = -500
                    enemy.enemyX = -1000

            enemy.enemy(enemy.enemyX, enemy.enemyY)

        # Bullet Movement
        if bullet_level_2.bulletY <= 0:
            bullet_level_2.bulletY = 0
            bullet_level_2.bullet_state = "ready"
        if bullet_level_2.bullet_state == "fire":
            bullet_level_2.fire_bullet(bullet_level_2.bulletX, bullet_level_2.bulletY)
            bullet_level_2.bulletY -= bullet_level_2.bulletY_change
        player1.player(player1.playerX, player1.playerY)
        show_score(score_value, 10, 10)
        pygame.display.update()


main_menu()
