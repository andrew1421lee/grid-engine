import pygame

class point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class pix:

    def __init__(self, value):
        self.value = value

class grid:
    matrix = []

    def __init__(self, w, h, size):
        if not w % size == 0:
            print("Invalid Width or Height for given Size")
            quit()
        else:
            self.MAX_X = int(w / size)
            self.MAX_Y = int(h / size)
            for i in range(int(w / size)): 
                self.matrix.append([]) # goes horizontally
                for j in range(int(h / size)):
                    self.matrix[i].append(pix(None))

    def set_pix_at(self, value, pnt):
        if self.check_bounds(pnt):
            self.matrix[pnt.y][pnt.x].value = value
            return True
        else: return False

    def reset_pix_at(self, pnt):
        if self.check_bounds(pnt):
            self.matrix[pnt.y][pnt.x].value = None
            return True
        else: return False

    def check_bounds(self, pnt):
        if pnt.x >= self.MAX_X or pnt.y >= self.MAX_Y or pnt.y < 0 or pnt.x < 0:
            return False
        else: return True

    def check_pix_value(self, pnt):
        if self.check_bounds(pnt):
            return self.matrix[pnt.y][pnt.x].value
        else: return None


class engine:
    WIDTH = 400 # window width
    HEIGHT = 400 # window height
    GRIDSIZE = 10 # grid size
    FPS = 30 # frame rate
    MAX_X = int(WIDTH / GRIDSIZE) # max x index
    MAX_Y = int(HEIGHT / GRIDSIZE) # max y indes
    GRID = grid(WIDTH, HEIGHT, GRIDSIZE)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BG_COLOR = BLACK

    def __init__(self):
        global clock, screen # global clock (fps) and display

        pygame.init() # initialize pygame
        
    def start(self): # start the game engine
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH)) # show the screen
        self.clock = pygame.time.Clock() # set the clock

    def refresh_screen(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def draw_rect(self, color, pnt):
        if self.GRID.set_pix_at(color, pnt):
            pygame.draw.rect(self.screen, color, pygame.Rect(pnt.x * self.GRIDSIZE, pnt.y * self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE)) # draw the square
            return True
        else: return False

    def draw_text(self, color, size, text):
        font = pygame.font.SysFont("monospace", size)
        label = font.render(text, 1, color)
        self.screen.blit(label, (100, 100))

    def del_rect(self, pnt):
        if self.GRID.reset_pix_at(pnt):
            pygame.draw.rect(self.screen, self.BG_COLOR, pygame.Rect(pnt.x * self.GRIDSIZE, pnt.y * self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE)) # draw a black square over the square
            return True
        else: return False 

    #def draw_mul_rects(self, rects)

    #def del_mul_rects(self, rects)

    def print_matrix(self): # print out all contents of matrix (debug purpose)
        for xarrays in self.GRID.matrix:
            for xvals in xarrays:
                print(str(xvals.value) + "  ", end = "")
            print("")
