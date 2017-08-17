from grid import *
from random import randint

def game_over():
    global instance, gameover
    instance.draw_text(instance.WHITE, 35, (100,100), "GAME OVER")
    gameover = True
    instance.refresh_screen()

def draw_score(score):
    instance.draw_rect(instance.WHITE, point(0, 0))
    instance.draw_rect(instance.WHITE, point(1, 0))
    instance.draw_rect(instance.WHITE, point(0, 1))
    instance.draw_rect(instance.WHITE, point(1, 1))
    instance.draw_rect(instance.WHITE, point(2, 0))
    instance.draw_rect(instance.WHITE, point(2, 1))
    instance.del_rect(point(0, 0))
    instance.del_rect(point(1, 0))
    instance.del_rect(point(0, 1))
    instance.del_rect(point(1, 1))
    instance.del_rect(point(2, 0))
    instance.del_rect(point(2, 1))
    instance.draw_text(instance.WHITE, 15, (5, 5), str(score))

def main():
    global instance, gameover, apple
    instance = engine()
    instance.start()
    gameover = False
    done = False
    clock = 0
    slowdown = 3
    snek = snake(point(0, 0))
    draw_score(snek.size)
    while not done:
        key_press = None
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                done = True
            if gameover and events.type == pygame.KEYDOWN:
                gameover = False
                snek = snake(point(0, 0))
                instance.clear_screen()
            elif events.type == pygame.KEYDOWN:
                key_press = events.key
    
        if clock % slowdown == 0:
            instance.del_rect(snek.tail)
            if snek.head.x < 0 or snek.head.y < 0 or snek.head.x >= instance.MAX_X or snek.head.y >= instance.MAX_Y:
                game_over()
            else:
                instance.draw_rect(instance.WHITE, snek.head)
                instance.draw_rect(instance.WHITE, snek.fruit)

        if key_press == pygame.K_UP and not snek.facing == 2: snek.facing = 0
        elif key_press == pygame.K_DOWN and not snek.facing == 0: snek.facing = 2
        elif key_press == pygame.K_LEFT and not snek.facing == 1: snek.facing = 3
        elif key_press == pygame.K_RIGHT and not snek.facing == 3: snek.facing = 1
 
        if clock % slowdown == 0 and not gameover:
            if snek.facing == 0: snek.add_segment(point(snek.head.x, snek.head.y - 1))# north
            elif snek.facing == 1: snek.add_segment(point(snek.head.x + 1, snek.head.y)) # east
            elif snek.facing == 2: snek.add_segment(point(snek.head.x, snek.head.y + 1)) # south
            elif snek.facing == 3: snek.add_segment(point(snek.head.x - 1, snek.head.y))
    
        #print(str(snek.tail.x) + ", " + str(snek.tail.y))
        #print(gameover)
        if not gameover:
            instance.refresh_screen()

        clock = clock + 1
    
        if clock > 10000000:
            clock = 0

    #instance.print_matrix()

class snake:
    default_size = 3
    head = None
    body = []
    tail = None
    facing = 2 # 0 = north, 1 = east, 2 = south, 3 = west
    size = 3;
    fruit = None

    def __init__(self, pnt):
        self.head = pnt
        self.tail = self.head
        self.body.append(self.head)
        
        self.place_fruit()
        #print(self.fruit)

    def add_segment(self, pnt):
        if self.check_self(pnt):
            game_over()
        if self.check_fruit(pnt):
            self.size = self.size + 1
            self.place_fruit()
            draw_score(self.size)
        self.head = pnt
        self.body.insert(0, self.head)
        try:
            self.tail = self.body.pop(self.size)
        except (IndexError):
            pass

    def place_fruit(self):
        placed = False
        while not placed:
            m_y = randint(0, instance.MAX_Y - 1)
            m_x = randint(0, instance.MAX_X - 1)
            if not self.check_self(point(m_x, m_y)):
                self.fruit = point(m_x, m_y)
                placed = True
    
    def check_fruit(self, pnt):
        if pnt == self.fruit:
            return True
        return False

    def check_self(self, pnt):
        for seg in self.body:
            if seg == pnt:
                return True
        return False

if __name__ == "__main__":
    main()
