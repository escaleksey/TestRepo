from pygame import *
from const import *
from sprite.player import Player
from sprite.ball import Ball

window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

player = Player(PLAYER_IMAGE, (30, 100), (0, 10), 4)
player2 = Player(PLAYER_IMAGE, (30, 100), (WIDTH-30, 10), 4)
ball = Ball(BALL_IMAGE, (50, 50), (WIDTH//2, HEIGHT//2), 5)
ball.set_random_dir()

player_group = sprite.Group()
player_group.add_internal(player)
player_group.add_internal(player2)

game = True
process = True

points_1 = 0
points_2 = 0

font.init()
score_font = font.Font(None,30)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if process:
        score_first =  score_font.render(f"Очков: {points_1}", True, (0, 0, 0))
        score_second = score_font.render(f"Очков: {points_2}", True, (0, 0, 0))
        
        ball.move(1) # !
        
        keys = key.get_pressed()

        if keys[K_w]:
            player.move(UP)
        if keys[K_s]:
            player.move(DOWN)

        if keys[K_UP]:
            player2.move(UP)
        if keys[K_DOWN]:
            player2.move(DOWN)

        if sprite.spritecollide(ball, player_group, False):
            ball.change_dir_x()

        check, player_number = ball.check_goal()
        if check:
            if player_number == 1:
                points_2 += 1
            else:
                points_1 += 1


    window.fill(BG_COLOR)
    window.blit(score_first, (10, 10))
    window.blit(score_second, (WIDTH - 100, 10))
    player.render(window)
    player2.render(window)
    ball.render(window)

    display.update()
    clock.tick(FPS)
