import pygame

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지 로드


empty_pot = pygame.image.load('C:/Users/82103/Desktop/pygame/assets/냄비1.png').convert_alpha()  # 빈 냄비 이미지
full_pot = pygame.image.load('C:/Users/82103/Desktop/pygame/assets/물냄비1.png').convert_alpha()  # 물이 찬 냄비 이미지

# 초기 알파 값 설정
alpha_value = 0
full_pot.set_alpha(alpha_value)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 물 채우기 효과
    if alpha_value < 255:
        alpha_value += 1  # 알파 값을 서서히 증가
        full_pot.set_alpha(alpha_value)

    # 화면을 먼저 빈 냄비로 채움
    screen.blit(empty_pot, (0, 0))

    # 그 위에 물이 찬 냄비 이미지를 알파값과 함께 그림
    screen.blit(full_pot, (0, 0))

    # 화면 갱신
    pygame.display.flip()

    # FPS 조절
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
