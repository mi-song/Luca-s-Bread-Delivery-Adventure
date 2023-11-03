import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목 설정
pygame.display.set_caption("Drag & Drop and Change Image Demo")


# 드래그 가능한 객체 클래스
class Draggable:
    def __init__(self, image_path, drop_image_path, x, y, width, height):
        original_image = pygame.image.load(image_path)
        self.original_image = pygame.transform.scale(original_image, (width, height))
        drop_image = pygame.image.load(drop_image_path)
        self.drop_image = pygame.transform.scale(drop_image, (width, height))
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.original_pos = (x, y)  # 원래 위치 저장
        self.dragging = False
        self.dropped = False
        self.drop_time = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.dropped:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP and self.dragging:
            self.dragging = False
            self.dropped = True
            self.drop_time = pygame.time.get_ticks()  # 드롭 시간 기록
            self.change_image(self.drop_image)  # 드롭 이미지로 변경

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x, mouse_y = event.pos
            self.rect.x = mouse_x + self.offset_x
            self.rect.y = mouse_y + self.offset_y

    def change_image(self, new_image):
        self.image = new_image

    def reset_after_delay(self):
        if self.dropped and pygame.time.get_ticks() - self.drop_time > 3000:  # 3초가 지났는지 확인
            self.change_image(self.original_image)  # 원래 이미지로 변경
            self.rect.topleft = self.original_pos  # 원래 위치로 이동
            self.dropped = False  # 드래그 상태 초기화

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# 드래그 객체 생성 (원본 이미지와 드롭 이미지 경로를 제공)
draggable = Draggable('C:/Users/rlaqhdrb/Desktop/pygame/밀가루.png', 'C:/Users/rlaqhdrb/Desktop/pygame/소금.png', 100, 100, 100, 100)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        draggable.handle_event(event)

    draggable.reset_after_delay()  # 상태를 확인하고 필요한 경우 리셋

    # 화면 색상 설정 (RGB)
    screen.fill((255, 255, 255))

    # 드래그 객체 그리기
    draggable.draw(screen)

    # 게임 화면 다시 그리기
    pygame.display.update()

# pygame 종료
pygame.quit()