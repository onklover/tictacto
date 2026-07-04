import pygame

screen = pygame.display.set_mode([300, 300])

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
while True:
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
        x += 0.05
    if up == True:
        y += 0.05
    if down == True:
        y -= 0.05
    if left == True:
        x -= 0.05
    
    if (x >= 65 and y >= 15) and (x <= 110 and y <= 60):
        gage += 0.01
    else:
        gage = 0

    if gage >= 100:
        isIn = 0
        gage = 100
    else:
        isIn = 5

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), (60, 10, 100, 100), isIn)
    pygame.draw.rect(screen, (0, 255, 0), (60, 120, gage, 10))
    a = 63
    for i in range(10):
        pygame.draw.rect(screen, (0,0,0), (a ,120,5,10))
        a+=10
    pygame.display.flip()