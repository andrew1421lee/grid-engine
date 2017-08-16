import pygame

class engine:
    WIDTH = 400 # window width
    HEIGHT = 400 # window height
    GRIDSIZE = 40 # grid size
    FPS = 15 # frame rate
    MAX_X = int(WIDTH / GRIDSIZE) # max x index
    MAX_Y = int(HEIGHT / GRIDSIZE) # max y indes
    GRIDMATRIX = [] # stores grid values

    BG_COLOR = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self):
        global clock, screen # global clock (fps) and display
        for i in range(int(self.WIDTH / self.GRIDSIZE)): # initialize gridmatrix with 0
            self.GRIDMATRIX.append([]) # x value arrays
            for j in range(int(self.HEIGHT / self.GRIDSIZE)): # init x value arrays
                self.GRIDMATRIX[i].append(0)
        pygame.init() # initialize pygame
        
    def start(self): # start the game engine
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH)) # show the screen
        self.clock = pygame.time.Clock() # set the clock
#        i = 0
#        done = False 
#        while not done: # loop until exit
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    done = True
#            self.draw_rect(self.WHITE, i, i)
#            if i % 2 == 0:
#                self.del_rect(i - 2, i -2)
#            i = i + 1
#            pygame.display.flip() # update the screen
#            self.clock.tick(self.FPS) # wait for fps clock

    def get_key_press(self): # returns a key press event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return event.key

    def check_for_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def refresh_screen(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def draw_rect(self, color, x, y):
        if x >= self.MAX_X or y >= self.MAX_Y: # not allowed to go out of bounds
            return False
        else: 
            pygame.draw.rect(self.screen, color, pygame.Rect(x * self.GRIDSIZE, y * self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE)) # draw the square
            self.GRIDMATRIX[y][x] = 1 # record its location
            return True

    def del_rect(self, x, y):
        if x >= self.MAX_X or y >= self.MAX_Y:
            return False
        if not self.GRIDMATRIX[y][x] == 0:
            pygame.draw.rect(self.screen, self.BG_COLOR, pygame.Rect(x * self.GRIDSIZE, y * self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE)) # draw a black square over the square
            self.GRIDMATRIX[y][x] = 0 # record deletion
            return True
        else:
            return False 

    def print_matrix(self): # print out all contents of matrix (debug purpose)
        for xarrays in self.GRIDMATRIX:
            for xvals in xarrays:
                print(str(xvals) + "  ", end = "")
            print("")
