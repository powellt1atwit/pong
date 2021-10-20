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
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1200, 600))

    #add a solid background as r,g,b:
    screen.fill((128,128,128))
    pygame.display.update()


    #create walls on the screen
    fgColour = pygame.Color("white")
    pygame.draw.rect(screen, fgColour, pygame.Rect(0, 0, width, border))
    pygame.draw.rect(screen, fgColour, pygame.Rect(0, 0, border, height))
    pygame.draw.rect(screen, fgColour, pygame.Rect(0, height-border, width, border))
    pygame.display.flip()

     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
