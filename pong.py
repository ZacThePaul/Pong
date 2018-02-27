import pygame as pg
import random

disw = 800
dish = 500
screen = pg.display.set_mode((disw, dish))

black = (0,0,0)
red = (255,0,0)

pg.init()

class GameRun(object):
    def __init__(self, disw, dish):
        self.disw = disw
        self.dish = dish
    def main(self):

        done = False

        computerScore = 0
        playerScore = 0

        start = False

        x = 700
        y = 200

        ballx = 400
        bally = 250
        ball_x_change = 0
        ball_y_change = 0

        paddle1x = 100
        paddle1y = 350

        paddle2x = 700
        paddle2y = 250

        y_change = 0

        volley = 0


        rr = 0

        infoGone = False

        while done == False:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        y_change -= 2
                    if event.key == pg.K_DOWN:
                        y_change += 2
                    if event.key == pg.K_SPACE:
                        if ballx == 400:
                            start = True
                            infoGone = True
                            rr = random.randint(1,2)

                if event.type == pg.KEYUP:
                    y_change = 0

            paddle2y += y_change
            ballx += ball_x_change
            bally += ball_y_change

            ball = pg.Rect(ballx,bally, 10, 10)
            paddle1 = pg.Rect(paddle1x, paddle1y, 10, 100)
            paddle2 = pg.Rect(paddle2x, paddle2y, 10, 100)

            if ball.colliderect(paddle1):
                ball_x_change = ball_x_change * -1
                volley += 1

            if volley < 5:
                if ball.colliderect(paddle2):
                    ball_x_change = ball_x_change * -1
                    ball_y_change += y_change
                    volley += 1
            elif volley >= 5:
                if ball.colliderect(paddle2):
                    ball_x_change = ball_x_change * - 1.5
                    volley += 1

            if bally > paddle1y:
                paddle1y += 2
            if bally < paddle1y:
                paddle1y -= 2

            if ballx > 800:
                computerScore = computerScore + 1
                ballx = 400
                bally = 250
                ball_x_change = 0
                ball_y_change = 0
                paddle2y = 250
                volley = 0
            if ballx < 0:
                playerScore = playerScore + 1
                ballx = 400
                bally = 250
                ball_x_change = 0
                ball_y_change = 0
                paddle2y = 250
                volley = 0
            if bally <= 0:
                ball_y_change = ball_y_change * -1

            if bally >= 500:
                ball_y_change = ball_y_change * -1

            if paddle2y <= 0:
                y_change = 0
            if paddle2y >= 400:
                y_change = 0

            if start == True:
                if rr == 1:
                    ball_x_change = 2
                    start = False
                if rr == 2:
                    ball_x_change = -2
                    start = False

            playerScoreFont = pg.font.SysFont('arial', 12)
            scoreLabel = playerScoreFont.render('player: %s' % playerScore, 1, red)

            computerScoreFont = pg.font.SysFont('arial', 12)
            CPUScoreLabel = computerScoreFont.render('computer: %s' % computerScore, 1, red)

            startFont = pg.font.SysFont('Courier New', 50)
            startLabel = startFont.render('To Begin Press Space', 1, red)

            volleyLable = playerScoreFont.render('Volley: %s' % volley, 1, red)

            screen.fill(black)

            pg.draw.rect(screen, red, (ballx, bally, 10, 10))
            pg.draw.rect(screen, red, (paddle1x, paddle1y, 10, 100))
            pg.draw.rect(screen, red, (paddle2x, paddle2y, 10, 100))
            screen.blit(scoreLabel, (500, 10))
            screen.blit(CPUScoreLabel, (200, 10))
            screen.blit(volleyLable, (350, 400))
            if infoGone == False:
                screen.blit(startLabel, (125, 200))

            pg.display.update()


if __name__=='__main__':
    GameRun(disw, dish).main()


