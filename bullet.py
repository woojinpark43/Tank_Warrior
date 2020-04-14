import pygame

class Bullet:
    bulletX: float
    bulletY: float

    def __init__(self, xCord, yCord):
        self.bulletX = xCord
        self.bulletY = yCord

class missile(Bullet):
    bullet_Img: pygame.image
    bullet_speed: int
    bullet_dir: bool
    bullet_position:int

    def __init__(self, xCord, yCord, dir, img):
        super().__init__(xCord, yCord)
        self.bullet_speed = 0
        self.bullet_Img = pygame.image.load(img)
        self.bullet_dir = dir

    def get_bullet_x(self):
        return self.bulletX

    def get_bullet_y(self):
        return self.bulletY

    def get_bullet_position(self):
        return self.bullet_position

    def move_bullet(self, screen):
        if (self.bullet_dir):
            screen.blit(self.bullet_Img, (self.bulletX + 16 + self.bullet_speed, self.bulletY + 10))
            self.bullet_position = self.bulletX + 16 + self.bullet_speed #bullet position after the shoot
        else:
            screen.blit(self.bullet_Img, (self.bulletX + 16 - self.bullet_speed, self.bulletY + 10))
            self.bullet_position = self.bulletX + 16 - self.bullet_speed  # bullet position after the shoot
        self.bullet_speed += 5

    #set the direction and fire the bullet
    def set_bullet_dir(self, screen):
        self.move_bullet(screen)
