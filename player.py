import pygame
from pygame import mixer

class Player:
    playerX: float
    playerY: float
    playerImg: pygame.image
    max_hp: int
    #bullets: list[coke]

    def __init__(self, xCord, yCord, picture, id):
        # player
        self.playerID = id
        self.playerImg = pygame.image.load(picture)#user's image
        self.playerX = xCord#user's X coordinate
        self.playerY = yCord#user's Y coordinate
        self.bullets = []#stores all the bullets
        self.healthImg = pygame.image.load("img\heart.png")
        self.max_hp = 7#max hp this user has
        self.playerUp = 0#indicate if player jumped
        self.playerJumpPos = yCord# Y position where player jumped
        self.reachedMaxJump = 0#reached max jump height
        self.playerOnGround = 0 #indicate whether player is on ground

    #change player's image
    def changeImage(self, img):
        self.playerImg = pygame.image.load(img)

    def display_health_bar(self, screen):

        #display health image
        for i in range(0, self.max_hp):
            player_font = pygame.font.Font('freesansbold.ttf',16)

            if (self.playerID == 1):
                player_text = player_font.render("p1", True, (255, 255, 255))
                screen.blit(player_text, (667, 0))
                screen.blit(self.healthImg, (688 + 16 * i, 0))  # player2 health

            else:
                player_text = player_font.render("p2", True, (255, 255, 255))
                screen.blit(player_text, (0, 0))
                screen.blit(self.healthImg, (21 + 16 * i, 0))  # player 1 health

    def playersJumpMove(self):
        if(self.playerUp == 1):
            if(self.reachedMaxJump == 0):
                self.playerY -= 4
            else:
                self.playerY += 4

            if(self.playerY <= self.playerJumpPos - 128):
                self.reachedMaxJump = 1

        if(self.playerOnGround == 1 and self.playerUp == 0):
            self.playerY += 4

    def playerScreenPosition(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))

    def check_on_hit(self, other_player):
        for bullet_ in other_player.get_bullets():
            x_val = bullet_.get_bullet_position() - self.playerX
            y_val = bullet_.get_bullet_y() - self.playerY
            if(abs(x_val) <= 2 and abs(y_val) <= 35):
                self.max_hp -= 1
                mixer.Sound("explosion.wav").play()
                other_player.get_bullets().remove(bullet_)
                break

    #return all the list of bullets this player has
    def get_bullets(self):
        return self.bullets

    #add bullets
    def add_bullets(self, bullet):
        self.bullets.append(bullet)

    #shoot bullets
    def shoot_bullet(self, screen):
        for bullet_ in self.bullets:
            bullet_.set_bullet_dir(screen)

    def clean_bullet(self):
        new_bullet = []
        for bullet_ in self.bullets:
            if 0 <= bullet_.get_bullet_x() <= 800:
                new_bullet.append(bullet_)
        self.bullets = new_bullet

    def playerInBound(self):
        #checking x boundary
        if self.playerX <= 0:
            self.playerX = 784
        elif self.playerX >= 784:
            self.playerX = 0

        #checking y boundary
        if self.playerY <= 0:
            self.playerY = 480
            self.playerUp = 0
            self.reachedMaxJump = 0
            self.playerOnGround = 1
        elif self.playerY >= 560:
            self.playerY = 1
            self.playerUp = 0
            self.reachedMaxJump = 0
            self.playerOnGround = 0
