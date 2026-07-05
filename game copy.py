import pygame

screen = pygame.display.set_mode([1000, 500])

FPS = 60
clock = pygame.time.Clock()

# for i in range(100000):
#     print(i)
x = 10
y = 10
isIn = 5
is_right_key_down = False
left = False
up = False
down = False
gage = 0


x_wall = 500
y_wall = 0
w_wall = 50
h_wall = 200

is_switch_on = False

while True:
    wall = (x < 0 or y < 0) and (x > 250 or y > 250)
    # print(1)
    for event in pygame.event.get():
        print(x , y)
        
        if event.type == 768:
            if event.key == 1073741906:
                down = True
            if event.key == 1073741903:
                # x+=10
                is_right_key_down = True
            if event.key == 1073741904:
                left = True
            if event.key == 1073741905:
                up = True

        # if x <= 0:
        #     left = False
        # elif x >= 250:
        #     is_right_key_down = False
        # elif y <= 0:
        #     up = False
        # elif y >= 250:
        #     down = False

        if event.type == 769:
            if event.key == 1073741906:
                down = False
            if event.key == 1073741903:
                is_right_key_down = False
            if event.key == 1073741904:
                left = False
            if event.key == 1073741905:
                up = False
        

        if event.type == 256:
            break

    if event.type == 256:
        break

    if is_right_key_down == True:
        x += 3#.05
    if up == True:
        y += 3#.05
    if down == True:
        y -= 3#.05
    if left == True:
        x -= 3#.05

    # 세로 벽 못넘어가도록 x 좌표 제한
    # if x >= x_wall - 50 and y < 200 and x < 510:
    #     x = 500 - 50
    #     # x = x_wall - 50
    # if x <= 550 and y < 200:
    #     x = 550
    if x_wall <= x + 50 and x <= x_wall + 50:
        is_switch_on = True




    # if x >= 250 - 50:
    #     x = 250 - 50

    # if y >= 250 - 50:
    #     y = 250 - 50

    if (x >= 65 and y >= 15) and (x <= 110 and y <= 60):
        gage += 3
    else:
        gage = 0

    if gage >= 100:
        isIn = 0
        gage = 100
    else:
        isIn = 5

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (60, 10, 100, 100), isIn)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), (60, 120, gage, 10))
    a = 63
    for i in range(10):
        pygame.draw.rect(screen, (0,0,0), (a ,120,5,10))
        a+=10

    # 세로 벽
    if is_switch_on == True:
        pygame.draw.rect(screen, (0, 255, 0), (x_wall, y_wall, w_wall, h_wall))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (x_wall, y_wall, w_wall, h_wall))
    # pygame.draw.rect(screen, (255, 0, 0), (x_wall / 2, y_wall, w_wall, h_wall))
    # pygame.draw.rect(screen, (255, 0, 0), (0, 250, h_wall*3, w_wall))

    pygame.display.flip()

    clock.tick(FPS)