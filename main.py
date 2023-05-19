import pygame as pg
from constantes import *
from colors import *
from world import World
from ball import Ball

def start():
    pg.init()
    screen=pg.display.set_mode(WINDOW_SIZE)
    running = True

    # world init
    world = World()
    world.add_entity(Ball(pg.Vector2(50, 50),  # position dans la fenêtre
                          pg.Vector2(50, 200), # vitesse initialle (en pixel/seconde)
                          15
                        ))
    world.add_entity(Ball(pg.Vector2(200, 100),
                          pg.Vector2(-500, -100),
                          10
                        ))
    world.add_entity(Ball(pg.Vector2(300, 50),
                          pg.Vector2(-300, 50),
                          10
                        ))
    world.add_entity(Ball(pg.Vector2(400, 200),
                          pg.Vector2(0, 200),
                          50
                        ))

    while running:
        # if user clicked X to close window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # code here !
        world.update()

        # update display
        screen.fill(WHITE)
        world.display(screen)

        pg.display.update()
    
    pg.quit()


if __name__ == "__main__":
    start()