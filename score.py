import pygame

pygame.font.init()

class Score_board:
    def __init__(self) -> None:
        self.current_score: int = 0
        self.score_font = pygame.font.SysFont('Actor', 60)
        
    def set_score(self,score):
        self.current_score = score
        
    def get_score(self):    
        return self.current_score
        
    def draw_score(self,screen):
        self.score_render = self.score_font.render(f'{self.current_score}', True, (255, 255, 255))
        self.score_rect = self.score_render.get_rect(center=(350,40))
        screen.blit(self.score_render,self.score_rect)