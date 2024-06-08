import pygame

class Ball:
    def __init__(self) -> None:
        self.on_ground = False
        self.velocity_x: float = 0
        self.velocity_y: float = 0
        self.gravity: int = 0 
        self.position = 50
    
    def move_ball_x(self):
        if self.velocity_x > 10:
            self.velocity_x = 10
        else:
            pass
        
    def get_velocity_x(self):
        return self.velocity_x
    
    def update_position(self):
        self.gravity_multiplier()
        self.position += self.velocity_y + self.gravity
        
    def gravity_multiplier(self):        
        if not self.on_ground:
            self.gravity += 0.2
        else:
            self.velocity_y = self.gravity * -0.35
            self.gravity = 0

    def update_on_ground(self,ground_height):
        if ground_height < self.position+self.gravity+21:
            self.on_ground = True
        else:
            self.on_ground = False
    
    def get_on_ground(self):
        return self.on_ground
        
    def draw_ball(self,screen):
        self.update_position()
        pygame.draw.circle(screen, (255,255,255) ,(100,self.position), 20)