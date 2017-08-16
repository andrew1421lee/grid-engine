from grid import *

def main():
    global instance 
    instance = engine()
    instance.start()

    done = False
    gameover = False
    clock = 0
    slowdown = 4
    while not done:
        key_press = None
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                done = True
            elif events.type == pygame.KEYDOWN:
                key_press = events.key
    
        if clock % slowdown == 0:
            instance.del_rect(lastx, lasty)
            if x < 0 or y < 0 or x >= instance.MAX_X or y >= instance.MAX_Y:
                game_over()
            instance.draw_rect(instance.WHITE, x, y)

        if key_press == pygame.K_UP: facing = 0
        elif key_press == pygame.K_DOWN: facing = 2
        elif key_press == pygame.K_LEFT: facing = 3
        elif key_press == pygame.K_RIGHT: facing = 1
    
        if clock % slowdown == 0 and not gameover:
            lastx = x
            lasty = y
            if facing == 0: y = y - 1 # north
            elif facing == 1: x = x + 1 # east
            elif facing == 2: y = y + 1 # south
            elif facing == 3: x = x - 1 # west
    
        instance.refresh_screen()


        clock = clock + 1
    
        if clock > 10000000:
            clock = 0

def game_over():
    instance.draw_text(instance.WHITE, 30, "GAME OVER MAN")
    gameover = True

class snake:
    head = None
    body = []
    tail = None
    facing = 2 # 0 = north, 1 = east, 2 = south, 3 = west

    def __init__(self, coor):
        head = coor
        tail = head
        body.append(head)

    def add_segment(self, coor):
        body.head = coor
        body.append(head)

if __name__ == "__main__":
    main()
