import pygame
from player import Player
from bullet import missile
from obstacle import Obstacle
from map import Map
from game_over import GameOver
from pygame import mixer

#initialize pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('Ultime_Volcano.png')

#Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#create screen
main_screen = pygame.display.set_caption("Tank Warrior")

# Title and Icon
pygame.display.set_caption("Tank Warrior")

#bullets
bullet_dir_1 = False #right = True, left = False
bullet_dir_2 = True

#player
player1 = Player(680, 100, 'img/tank1-left.png', 1)
player2 = Player(70, 100, 'img/tank2-right.png', 2)

#obstacles
obstacle1 = Obstacle(0,0,758,540)#horizontal obstacle 1
obstacle2 = Obstacle(560,180,560, 346)#horizontal obstacle 2
obstacle3 = Obstacle(260,260,514, 154)#horizontal obstacle 3

#map
gameMap = Map()#map for the game

#movements
player1XChange = 0
player2XChange = 0

#winner
winner = 0

#Run while user exits
game_running = True
while game_running:

    # RGB - Red, Green, Blue
    screen.fill((0, 128, 128))
    #background Image
    screen.blit(background, (0, 0))

    #Check loop through every event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Check if the user press exit
            game_running = False #End game

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:

            #player1 control
            if event.key == pygame.K_LEFT:
                # print("Left arrow is pressed:")
                player1XChange -= 4
                player1.changeImage("img/tank1-left.png")
                bullet_dir_1 = False
            if event.key == pygame.K_RIGHT:
                # print("Right arrow is pressed:")
                player1XChange += 4
                player1.changeImage("img/tank1-right.png")
                bullet_dir_1 = True
            if event.key == pygame.K_UP:
                # print("Up arrow is pressed:")
                if(player1.playerUp == 0 and player1.playerOnGround == 0):
                    player1.playerJumpPos = player1.playerY
                    player1.playerUp = 1
            if event.key == pygame.K_DOWN:
                # print("Down arrow is pressed:")
                if(player1.playerUp == 0):
                    player1.playerY += 4

            #player 2 control
            if event.key == ord('a'):
                # print("Left2 arrow is pressed:")
                player2XChange -= 4
                player2.changeImage("img/tank2-left.png")
                bullet_dir_2 = False
            if event.key == ord('d'):
                # print("Right2 arrow is pressed:")
                player2XChange += 4
                player2.changeImage("img/tank2-right.png")
                bullet_dir_2 = True
            if event.key == ord('w'):
                # print("Up arrow is pressed:")
                if (player2.playerUp == 0 and player2.playerOnGround == 0):
                    player2.playerJumpPos = player2.playerY
                    player2.playerUp = 1
            if event.key == ord('s'):
                # print("Right2 arrow is pressed:")
                if(player2.playerUp == 0):
                    player2.playerY += 4

            #play again
            if event.key == ord('y'):
                # play again XD
                if(winner != 0):
                    player1 = Player(680, 100, 'img/tank1-left.png', 1)
                    player2 = Player(70, 100, 'img/tank2-right.png', 2)
                    winner = 0

            #shoot bullets player 1
            if event.key == ord('/'):
                print("player1 shoot bullet")
                mixer.Sound("laser.wav").play()
                if(bullet_dir_1):
                    bullet = missile(player1.playerX, player1.playerY,
                                     bullet_dir_1, "img/missile-right.png")
                else:
                    bullet = missile(player1.playerX, player1.playerY,
                                     bullet_dir_1, "img/missile-left.png")
                player1.add_bullets(bullet)

            #player 2 shoots bullet
            if event.key == ord('r'):
                print("player2 shoot bullet")
                mixer.Sound("laser.wav").play()
                if (bullet_dir_2):
                    bullet = missile(player2.playerX, player2.playerY,
                                     bullet_dir_2, "img/missile-right.png")

                else:
                    bullet = missile(player2.playerX, player2.playerY,
                                     bullet_dir_2, "img/missile-left.png")
                player2.add_bullets(bullet)

        if event.type == pygame.KEYUP:
            #player 1's keyups
            if event.key == pygame.K_LEFT \
                    or event.key == pygame.K_RIGHT:
                player1XChange = 0

            #player 2's keyups
            if event.key == ord('a') or event.key == ord('d'):
                player2XChange = 0

    #change player's x movement
    player1.playerX += player1XChange
    player2.playerX += player2XChange

    # change player's y movement
    player1.playersJumpMove()
    player2.playersJumpMove()

    # check if the player is on the map
    gameMap.playerOnGround(player1)
    gameMap.playerOnGround(player2)

    #make sure players are in Bound
    player1.playerInBound()
    player2.playerInBound()

    #Add player in screen
    player1.playerScreenPosition(screen)
    player2.playerScreenPosition(screen)

    #shoot bullet
    player1.shoot_bullet(screen)
    player2.shoot_bullet(screen)

    #clear all the bullets that are outside the bounds
    player1.clean_bullet()
    player2.clean_bullet()

    #check if the player got hit by a bullet
    player1.check_on_hit(player2)
    player2.check_on_hit(player1)

    #display health information
    player1.display_health_bar(screen)
    player2.display_health_bar(screen)

    #move obstacle
    obstacle1.obstacleMove()
    obstacle2.obstacleMove()
    obstacle3.obstacleMove()

    #check obstacle bounds
    obstacle1.obstacleInBound()
    obstacle2.obstacleInBound()
    obstacle3.obstacleInBound()

    #check if player got hit by an obstacle
    obstacle1.obstacleOnHit(player1)
    obstacle1.obstacleOnHit(player2)
    obstacle2.obstacleOnHit(player1)
    obstacle2.obstacleOnHit(player2)
    obstacle3.obstacleOnHit(player1)
    obstacle3.obstacleOnHit(player2)

    #display obstacles
    obstacle1.obstacleScreenPosition(screen)
    obstacle2.obstacleScreenPosition(screen)
    obstacle3.obstacleScreenPosition(screen)

    #display map
    gameMap.setGround(screen)

    if ((player1.max_hp <= 0 or player2.max_hp <= 0)
        and winner == 0):
        if (player1.max_hp < player2.max_hp):
            winner = 2
        else:
            winner = 1

    if (winner != 0):
        game = GameOver(winner)
        game.show_winner(screen)

    #Update the display
    pygame.display.update()
