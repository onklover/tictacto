import pygame

screen = pygame.display.set_mode([1000, 500])

FPS = 60
clock = pygame.time.Clock()
x = 10
y = 10
is_right_key_down = False
left = False
up = False
down = False
space = False

bullet_list = []

while True:
    # 이벤트 감지
    for event in pygame.event.get():
        # print(event)
        print(bullet_list)
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

            if event.key == 32:
                space = True

            
        if event.type == 769:
            if event.key == 1073741906:
                down = False
            if event.key == 1073741903:
                is_right_key_down = False
            if event.key == 1073741904:
                left = False
            if event.key == 1073741905:
                up = False

            if event.key == 32:
                space = False

    # 업데이트
    if is_right_key_down == True:
        x += 3#.05
    if up == True:
        y += 3#.05
    if down == True:
        y -= 3#.05
    if left == True:
        x -= 3#.05

    if space == True:
        bullet_list.append([x, y])

    for i in range(len(bullet_list)):
        bullet_list[i][1] -= 10

    # 그리기 
    screen.fill((0, 0, 0))
    # if space == True:
        # shootx = x
        # shooty = y
        # if space:
        #     shooty-=10
        #     pygame.draw.rect(screen, (0, 255, 0), (shootx+20,shooty-10,10,30))
    for i in range(len(bullet_list)):
        try:
            shootx, shooty = bullet_list[i]
        except:
            pass
        shooty -= 10
        pygame.draw.rect(screen, (0, 255, 0), (shootx+20,shooty-10,10,30))
        try:
            if shooty < 0:
                del bullet_list[i]
        except:
            pass

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (255,255,0), (100,100,100,100))
    pygame.display.flip()

    clock.tick(FPS)