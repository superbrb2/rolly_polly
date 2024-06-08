import pygame


class Ground:
    def __init__(self) -> None:
        self.height = 600
        
    def draw_ground(self,screen):
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(0,self.height,700,100))
    
    def get_height(self):
        return self.height

class Score_line:
    def __init__(self, height, score) -> None:
        self.height: int = height
        self.score_gained: int = score
        
    def get_score_gained(self):
        return self.score_gained
    
    def get_height(self):
        return self.height
    
    def set_height(self,new_height):
        self.height = new_height
        
    