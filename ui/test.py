import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목 설정
pygame.display.set_caption("UI Demo")


class UI:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.visible = False
        self.close_button = pygame.Rect(self.rect.topright, (20, 20))  # 'X' 버튼의 Rect

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.visible:
                self.visible = True
            elif self.close_button.collidepoint(event.pos) and self.visible:
                self.visible = False

    def draw(self, surface):
        if self.visible:
            surface.blit(self.image, self.rect)
            # 'X' 버튼 그리기 (실제 게임에서는 'X' 이미지를 사용하는 것이 좋습니다)
            pygame.draw.rect(surface, (255, 0, 0), self.close_button)
            pygame.draw.line(surface, (255, 255, 255), self.close_button.topleft, self.close_button.bottomright, 3)
            pygame.draw.line(surface, (255, 255, 255), self.close_button.topright, self.close_button.bottomleft, 3)


# UI 객체 생성
ui = UI('C:/Users/rlaqhdrb/Desktop/pygame/resource/밀가루.png', 100, 100)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ui.handle_event(event)

    # 화면 색상 설정 (RGB)
    screen.fill((255, 255, 255))

    # UI 그리기
    ui.draw(screen)

    # 게임 화면 다시 그리기
    pygame.display.update()

# pygame 종료
pygame.quit()
