from grid import *

def main():
    global instance, gameover, done 
    instance = engine()
    instance.start()

    done = False
    gameover = False
    clock = 0
    slowdown = 4
    snek = snake(point(0, 0))
    while not done:
        key_press = None
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                done = True
            elif events.type == pygame.KEYDOWN:
                key_press = events.key
    
        if clock % slowdown == 0:
            instance.del_rect(snek.tail)
            if snek.head.x < 0 or snek.head.y < 0 or snek.head.x >= instance.MAX_X or snek.head.y >= instance.MAX_Y:
                game_over()
                gameover = True
                instance.refresh_screen()
            else: instance.draw_rect(instance.WHITE, snek.head)

        if key_press == pygame.K_UP: snek.facing = 0
        elif key_press == pygame.K_DOWN: snek.facing = 2
        elif key_press == pygame.K_LEFT: snek.facing = 3
        elif key_press == pygame.K_RIGHT: snek.facing = 1
    
        if clock % slowdown == 0 and not gameover:
            if snek.facing == 0: snek.add_segment(point(snek.head.x, snek.head.y - 1))# north
            elif snek.facing == 1: snek.add_segment(point(snek.head.x + 1, snek.head.y)) # east
            elif snek.facing == 2: snek.add_segment(point(snek.head.x, snek.head.y + 1)) # south
            elif snek.facing == 3: snek.add_segment(point(snek.head.x - 1, snek.head.y))
    
        #print(str(snek.tail.x) + ", " + str(snek.tail.y))
        if not gameover:
            instance.refresh_screen()

        clock = clock + 1
    
        if clock > 10000000:
            clock = 0

    instance.print_matrix()

def game_over():
    instance.draw_text(instance.WHITE, 30, "GAME OVER MAN")
    gameover = True

class snake:
    head = None
    body = []
    tail = None
    facing = 2 # 0 = north, 1 = east, 2 = south, 3 = west
    size = 10;

    def __init__(self, pnt):
        self.head = pnt
        self.tail = self.head
        self.body.append(self.head)

    def add_segment(self, pnt):
        self.head = pnt
        self.body.insert(0, self.head)
        try:
            self.tail = self.body.pop(self.size)
        except (IndexError):
            pass

if __name__ == "__main__":
    main()
