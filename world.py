import pygame as pg
from constantes import *
from entity import Entity
import math

class World():
    def __init__(self) -> None:
        # définition des entités
        self.clock = pg.time.Clock()
        self.entities : list[Entity] = []
    
    def add_entity(self, ent : Entity):
        self.entities.append(ent)

    def update(self):
        t = self.clock.tick()
        for entity in self.entities:
            entity.update(t)
        
        self._check_collide()

    def display(self, screen):
        for entity in self.entities:
            entity.display(screen)
    
    def _collide(self, ent1, ent2):
        v1 = ent1.v
        m1 = ent1.masse

        v2 = ent2.v
        m2 = ent2.masse

        v1_prime = (2*m2*v2 + (m1 - m2)*v1)/(m2 + m1)
        v2_prime = (2*m1*v1 + (m2 - m1)*v2)/(m2 + m1)

        ent1.v = v1_prime
        ent2.v = v2_prime

    def _check_collide(self):
        i = 0
        while i < len(self.entities):
            ent1 = self.entities[i]
            j = i + 1
            while j < len(self.entities):
                ent2 = self.entities[j]
                j += 1
                dist = ent1.pos - ent2.pos
                if ent1.rayon + ent2.rayon > math.hypot(dist.x, dist.y):
                    self._collide(ent1, ent2)
            i+=1