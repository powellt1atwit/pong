#import Paddle and Ball classes
from paddle import paddle
from ball import ball

#import random
import random

# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("minimal program")

    width = 1200
    height = 600
    border = 20
    velocity = 5
    FPS = 60
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1200, 600))

    #add a solid background as r,g,b:
    screen.fill((0,0,0))
    pygame.display.update()


    #create walls on the screen
    fgColour = pygame.Color("white")
    bgColour = pygame.Color("black")
    pygame.draw.rect(screen, fgColour, pygame.Rect(0, 0, width, border))
    pygame.draw.rect(screen, fgColour, pygame.Rect(0, 0, border, height))
    pygame.draw.rect(screen, fgColour, pygame.Rect(0, height-border, width, border))
    pygame.display.flip()

    #Ball init
    x0 = width - ball.radius
    y0 = height // 2
    vx0 = -(velocity)
    vy0 = random.uniform(-velocity, velocity)

    b0 = ball(x0, y0, vx0, vy0, screen, fgColour, bgColour, border, height)
    b0.show(fgColour)


    pygame.display.update()

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
     
    # main loop
    while running:
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()
        clock.tick(FPS)
        
        #ball
        b0.update()    
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()