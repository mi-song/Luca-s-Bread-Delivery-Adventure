import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목 설정
pygame.display.set_caption("UI Interaction Demo")


def scale_image(image, max_width, max_height):
    # 원본 이미지의 크기와 비율을 구합니다.
    original_width, original_height = image.get_size()
    ratio = min(max_width / original_width, max_height / original_height)

    # 새로운 크기를 계산합니다.
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)

    # 이미지를 새로운 크기로 조정합니다.
    return pygame.transform.scale(image, (new_width, new_height))


class UI:
    def __init__(self, ui_image_path, content_image_path, close_button_path, x, y, max_width, max_height):
        # UI 배경 이미지
        ui_image = pygame.image.load(ui_image_path)
        self.ui_image = scale_image(ui_image, max_width, max_height)
        self.rect = self.ui_image.get_rect(topleft=(x, y))

        # 열릴 이미지
        content_image = pygame.image.load(content_image_path)
        self.content_image = scale_image(content_image, screen_width, screen_height)
        self.content_rect = self.content_image.get_rect(center=(screen_width // 2, screen_height // 2))

        # 닫기 버튼 이미지
        close_image = pygame.image.load(close_button_path)
        self.close_image = scale_image(close_image, 20, 20)  # 예를 들어 'X' 버튼의 최대 크기를 20x20으로 설정
        self.close_button_rect = self.close_image.get_rect(topright=(self.content_rect.right, self.content_rect.top))

        self.visible = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.visible:
                # UI 이미지 클릭
                self.visible = True
            elif self.close_button_rect.collidepoint(event.pos) and self.visible:
                # 닫기 버튼 클릭
                self.visible = False

    def draw(self, surface):
        # UI 배경 이미지 그리기
        surface.blit(self.ui_image, self.rect)

        # 열린 이미지와 닫기 버튼 그리기
        if self.visible:
            surface.blit(self.content_image, self.content_rect)
            surface.blit(self.close_image, self.close_button_rect)


# UI 객체 생성 (실제 이미지 경로로 변경해야 함)
ui = UI('C:/Users/rlaqhdrb/Desktop/pygame/resource/밀가루.png', 'C:/Users/rlaqhdrb/Desktop/pygame/resource/소금.png',
        'C:/Users/rlaqhdrb/Desktop/pygame/resource/버터.png', 50, 50, 50, 50)

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
