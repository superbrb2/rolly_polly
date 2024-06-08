import pygame
import score
import ball
import level

WIDTH = HEIGHT = 700

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
screen.fill('#5BC3EB')
pygame.display.set_caption('Rolly Polly')

score_board = score.Score_board()
the_ball = ball.Ball()
the_ground = level.Ground()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
        screen.fill('#5BC3EB')
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                if the_ball.get_on_ground():
                    the_ball.move_ball_x()
                else:
                    the_ball.gravity_multiplier()
                score_board.set_score(score_board.get_score()+10)
        score_board.draw_score(screen)
    
    
    screen.fill('#5BC3EB')
    the_ball.update_on_ground(the_ground.get_height())
    the_ball.draw_ball(screen)
    the_ground.draw_ground(screen)
    score_board.draw_score(screen)


        
        
        
      
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()
    
    