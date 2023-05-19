import pygame as pg
from colors import *
from entity import Entity
import math
from constantes import *

class Ball(Entity):
    COEFF_FROTTEMENT = 0.05

    def __init__(self, pos : pg.Vector2, v : pg.Vector2 = pg.Vector2(0,0), masse = 1) -> None:
        self.pos = pos
        self.v = v # px / sec
        self.masse = masse # kg
        self.rayon = METTER * pow(3*masse/(4*RHO*math.pi), 1/3) # px
    
    def display(self, screen : pg.Surface):
        pg.draw.circle(screen, BLUE, self.pos, self.rayon)
    
    def update(self, ticks):
        dx = 0
        dy = 0

        dt = ticks / 1000
        dx += self.v.x * dt
        dy += self.v.y * dt 

        # collision avec les murs
        if (self.pos.x + dx + self.rayon) > WINDOW_SIZE[0] or (self.pos.x + dx - self.rayon) < 0:
            self.v.x = -self.v.x
            dx = 0
        
        if (self.pos.y + dy + self.rayon) > WINDOW_SIZE[1] or (self.pos.y + dy - self.rayon) < 0:
            self.v.y = -self.v.y
            dy = 0

        # maj vitesse en fonction des frottements
        self.v.x *= max(1 - self.COEFF_FROTTEMENT * dt, 0)
        self.v.y *= max(1 - self.COEFF_FROTTEMENT * dt, 0)

        # on change la vitesse avec la gravité.
        self.v.y += G * METTER * dt
        
        self.pos.x += dx
        self.pos.y += dy
    
    def can_collide(self):
        return True
