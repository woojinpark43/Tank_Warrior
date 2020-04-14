import pygame
from player import Player

class GameOver:
    def __init__(self, winner):
        self.over_font = pygame.font.Font('freesansbold.ttf',64)
        self.explain_font = pygame.font.Font('freesansbold.ttf',40)
        self.winner = winner

    def show_winner(self, screen):
        if (self.winner == 1):
            over_text1 = self.over_font.render("GameOver",
                                         True, (255, 255, 255))
            over_text2 = self.over_font.render("p1 won",
                                               True, (255, 255, 255))
            over_text3 = self.explain_font.render("press y to play again",
                                               True, (255, 255, 255))
            screen.blit(over_text1, (200, 100))
            screen.blit(over_text2, (250, 164))
            screen.blit(over_text3, (200, 250))
        else:
            over_text1 = self.over_font.render("GameOver",
                                               True, (255, 255, 255))
            over_text2 = self.over_font.render("p2 won",
                                               True, (255, 255, 255))
            over_text3 = self.explain_font.render("press y to play again",
                                                  True, (255, 255, 255))
            screen.blit(over_text1, (200, 100))
            screen.blit(over_text2, (250, 164))
            screen.blit(over_text3, (200, 250))
