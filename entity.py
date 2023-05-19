import pygame as pg

class Entity():
    def __init__(self) -> None:
        pass

    def display(self, screen : pg.Surface ) -> None:
        pass

    def update(self, ticks):
        pass

    def can_collide(self):
        return False