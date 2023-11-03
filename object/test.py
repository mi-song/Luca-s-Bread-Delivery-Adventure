import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목 설정
pygame.display.set_caption("Drag & Drop and Change Image Demo")

# Additional images list
a1 = 'C:/Users/rlaqhdrb/Desktop/pygame/resource/크루와상 반죽.png'
a2 = 'C:/Users/rlaqhdrb/Desktop/pygame/resource/크루와상.png'
a3 = 'C:/Users/rlaqhdrb/Desktop/pygame/resource/크루와상2.png'

additional_images = [a1, a2, a3]  # etc.
additional_surfaces = []

# Load and transform additional images
for img_path in additional_images:
    img = pygame.image.load(img_path)
    additional_surfaces.append(pygame.transform.scale(img, (100, 100)))

# Current index for additional images and a flag to stop cycling images
current_index = 0
stop_cycling = False

# A simple function to draw the additional image at a fixed position
def draw_additional_image(surface, index, position=(300, 300)):
    surface.blit(additional_surfaces[index], position)


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # 드래그 상태가 아니고, 드롭된 상태에서 클릭했을 때, 원래 이미지와 위치로 복귀
                if not self.dragging and self.dropped:
                    self.change_image(self.original_image)
                    self.rect.topleft = self.original_pos
                    self.dropped = False
                # 드래그 시작
                else:
                    self.dragging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.rect.x - mouse_x
                    self.offset_y = self.rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP and self.dragging:
            # 드래그 종료
            self.dragging = False
            self.dropped = True
            self.drop_time = pygame.time.get_ticks()
            self.change_image(self.drop_image)

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            # 드래그 중 이미지 이동
            mouse_x, mouse_y = event.pos
            self.rect.x = mouse_x + self.offset_x
            self.rect.y = mouse_y + self.offset_y

    def change_image(self, new_image):
        self.image = new_image

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# 드래그 객체 생성 (원본 이미지와 드롭 이미지 경로를 제공)
draggable = Draggable('C:/Users/rlaqhdrb/Desktop/pygame/resource/밀가루.png', 'C:/Users/rlaqhdrb/Desktop/pygame/resource/소금.png', 100, 100, 100, 100)

# Timer for changing the additional image
change_image_event = pygame.USEREVENT + 1

# Flag to indicate if the timer is set
timer_set = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == change_image_event and not stop_cycling:
            # Increment the index but stop cycling after the last image
            if current_index < len(additional_surfaces) - 1:
                current_index += 1
            else:
                # Once the last image is reached, stop the cycling
                stop_cycling = True
                pygame.time.set_timer(change_image_event, 0)  # Stop the timer
                timer_set = False

        draggable.handle_event(event)

    # If the Draggable object is dropped and the timer is not already set, start the timer
    if draggable.dropped and not stop_cycling and not timer_set:
        pygame.time.set_timer(change_image_event, 1500)
        timer_set = True

    # If the Draggable object has been reset, stop the timer
    if not draggable.dragging and not draggable.dropped and timer_set:
        pygame.time.set_timer(change_image_event, 0)
        timer_set = False

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the additional image
    draw_additional_image(screen, current_index)

    # Draw the draggable object
    draggable.draw(screen)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()