import pygame
from player import Player

class Map:
    groundImg: pygame.image

    def __init__(self):
        # ground
        self.groundLoc = {}
        self.groundImg = pygame.image.load("img\ground.png")#ground img

    def setGround(self, screen):
        #creating a map
        for i in range(0, 13):
            screen.blit(self.groundImg, (0 + 64 * i, 560))
            if "560" not in self.groundLoc.keys():
                self.groundLoc["560"] = [0 + 64 * i]
            else:
                self.groundLoc["560"].append(0 + 64 * i)

        #left level 1 ground
        screen.blit(self.groundImg, (100, 464))
        self.groundLoc["464"] = [100]
        screen.blit(self.groundImg, (164, 464))
        self.groundLoc["464"].append(164)

        #right level 1 ground
        screen.blit(self.groundImg, (570, 464))
        self.groundLoc["464"].append(570)
        screen.blit(self.groundImg, (634, 464))
        self.groundLoc["464"].append(634)

        #level 2 ground
        for i in range(0, 7):
            screen.blit(self.groundImg, (180 + 64 * i, 368))
            if "368" not in self.groundLoc.keys():
                self.groundLoc["368"] = [180 + 64 * i]
            else:
                self.groundLoc["368"].append(180 + 64 * i)

        #right level 3 ground
        screen.blit(self.groundImg, (670, 272))
        self.groundLoc["272"] = [670]
        #left level 3 ground
        screen.blit(self.groundImg, (100, 272))
        self.groundLoc["272"].append(100)

        #level 4 ground
        for i in range(0, 5):
            screen.blit(self.groundImg, (260 + 64 * i, 176))
            if "176" not in self.groundLoc.keys():
                self.groundLoc["176"] = [260 + 64 * i]
            else:
                self.groundLoc["176"].append(260 + 64 * i)

        #right level 5 ground
        for i in range(0, 2):
            screen.blit(self.groundImg, (630 + 64 * i, 80))
            if "80" not in self.groundLoc.keys():
                self.groundLoc["80"] = [630 + 64 * i]
            else:
                self.groundLoc["80"].append(630 + 64 * i)
        #left level 5 ground
        for i in range(0, 2):
            screen.blit(self.groundImg, (50 + 64 * i, 80))
            if "80" not in self.groundLoc.keys():
                self.groundLoc["80"] = [50 + 64 * i]
            else:
                self.groundLoc["80"].append(50 + 64 * i)

    def playerOnGround(self, player):

        found = 0
        for key in self.groundLoc.keys():
            y = int(key);
            if (y - 33.5 <= player.playerY <= y - 30):
                for x in self.groundLoc[key]:
                    if x - 37 <= player.playerX <= x + 37:
                        player.playerUp = 0
                        player.reachedMaxJump = 0
                        player.playerOnGround = 0
                        found = 1
                        break
                if (found == 1):
                    break
            else:
                player.playerOnGround = 1
