import pygame

class ball:
    
    #class variables
    radius = 10

    def __init__(self, x, y, vx, vy, screen, fgColour, bgColour, border, height):
        
        #instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgColour = fgColour
        self.bgColour = bgColour
        self.border = border
        self.height = height


    def show(self, colour):
        
        pygame.draw.circle(self.screen, colour, (self.x, self.y), self.radius)
    
    def update(self):

        newx = self.x + self.vx
        newy = self.y + self.vy

        if  newx < (self.border + self.radius) :
            self.vx = -self.vx
        elif newy < (self.border + self.radius) or newy > (self.height - self.border - self.radius):
            self.vy = -self.vy
        else:
            self.show(self.bgColour)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(self.fgColour)