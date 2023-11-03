import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 860
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목 설정
pygame.display.set_caption("kiki")


class Character:
    def __init__(self, image_path, x, y, speed):
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (int(102.4), int(179.2)))  # 이미지 크기 조정
        self.x = x
        self.y = y
        self.speed = speed
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.to_x = 0
        self.to_y = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.to_x -= self.speed
            elif event.key == pygame.K_RIGHT:
                self.to_x += self.speed
            elif event.key == pygame.K_UP:
                self.to_y -= self.speed
            elif event.key == pygame.K_DOWN:
                self.to_y += self.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.to_y = 0

    def update(self, dt):
        self.x += self.to_x * dt
        self.y += self.to_y * dt
        self.x = max(0, min(screen_width - self.width, self.x))
        self.y = max(0, min(screen_height - self.height, self.y))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


# 캐릭터 객체 생성
character = Character('C:/Users/rlaqhdrb/Desktop/pygame/3_witch.png', screen_width / 2, screen_height / 2, 1000)

# 게임 루프
running = True
while running:
    dt = pygame.time.Clock().tick(60) / 1000  # 프레임 당 경과 시간(ms -> s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        character.handle_event(event)

    character.update(dt)

    # 화면 색상 설정 (RGB)
    screen.fill((255, 255, 255))

    # 캐릭터 그리기
    character.draw(screen)

    # 게임 화면 다시 그리기
    pygame.display.update()

# pygame 종료
pygame.quit()
