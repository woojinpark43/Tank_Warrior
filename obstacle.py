import pygame
from pygame import mixer

class Obstacle:
    obstacleX: float
    obstacleY: float
    obstacleImg: pygame.image

    def __init__(self, xCord, xCord1, xCord2, yCord):
        # Obstacle
        self.obstacleImg = pygame.image.load("img\saw.png")#user's image
        self.obstacleX = xCord#obstacle X coordinate
        self.obstacleX1 = xCord1#obstacle X coordinate boundary 1
        self.obstacleX2 = xCord2#obstacle X coordinate boundary 2
        self.obstacleY = yCord#obstacle Y coordinate
        self.moveX = 3#direction of the obstacle

    def obstacleScreenPosition(self, screen):
        #display obstacle in screen
        screen.blit(self.obstacleImg, (self.obstacleX, self.obstacleY))

    def obstacleMove(self):
        self.obstacleX += self.moveX

    def obstacleOnHit(self, player):
        if self.obstacleX - 15 <= player.playerX\
            <= self.obstacleX + 15 \
            and self.obstacleY - 32 <= player.playerY\
            <= self.obstacleY + 5:
            player.max_hp -= 1
            mixer.Sound("explosion.wav").play()

    def obstacleInBound(self):
        #checking x boundary
        if self.obstacleX <= self.obstacleX1:
            self.moveX = 3
        elif self.obstacleX >= self.obstacleX2:
            self.moveX = -3
