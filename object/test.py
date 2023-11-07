import pygame

import sys
sys.path.append('..')

from imagepath import *

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목 설정
pygame.display.set_caption("Drag & Drop and Change Image Demo")

# Additional images list
a1 = 'C:/Users/Main/Desktop/배경제거/크루와상 반죽_.png'
a2 = 'C:/Users/Main/Desktop/배경제거/크루와상_.png'
a3 = 'C:/Users/Main/Desktop/배경제거/크루와상2_.png'

empty_pot = pygame.image.load('C:/Users/Main/Desktop/배경제거/빈냄비_.png').convert_alpha()  # 빈 냄비 이미지
full_pot = pygame.image.load('C:/Users/Main/Desktop/배경제거/물냄비_.png').convert_alpha()  # 물이 찬 냄비 이미지
flour_pot = pygame.image.load('C:/Users/Main/Desktop/배경제거/밀가루냄비_.png').convert_alpha()  # 밀가루

# 초기 알파 값 설정
alpha_value = 0
full_pot.set_alpha(alpha_value)

additional_images = [a1, a2, a3]  # etc.
additional_surfaces = []

# Load and transform additional images
for img_path in additional_images:
    img = pygame.image.load(img_path)
    additional_surfaces.append(pygame.transform.scale(img, (100, 100)))

# Current index for additional images and a flag to stop cycling images
current_index = 0
stop_cycling = False

flour_rect = flour_image.get_rect(topleft=(700, 100))

# A simple function to draw the additional image at a fixed position
def draw_additional_image(surface, index, position=(300, 300)):
    surface.blit(additional_surfaces[index], position)


# 드래그 가능한 객체 클래스
class Draggable:
    def __init__(self, image_path, drop_image_path, collide_image_path, x, y, width, height, obj_type):
        self.offset_x = None
        print(f"Width: {width}, Height: {height}")
        self.type = obj_type
        try:
            self.original_image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        except Exception as e:
            print(f"Error loading original image: {e}")
            self.original_image = None

        self.drop_image = pygame.transform.scale(pygame.image.load(drop_image_path), (width, height))
        # Load the collide image if a path is provided
        # self.collide_image = None
        if collide_image_path is not None:
            self.collide_image = pygame.transform.scale(pygame.image.load(collide_image_path), (width, height))
        else:
            self.collide_image = None

        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.original_pos = (x, y)
        self.dragging = False
        self.dropped = False
        self.drop_time = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.dragging and self.dropped:
                    self.change_image(self.original_image)
                    self.rect.topleft = self.original_pos
                    self.dropped = False

                # self.dragging = True
                # mouse_x, mouse_y = event.pos
                # self.offset_x = self.rect.x - mouse_x
                # self.offset_y = self.rect.y - mouse_y

                # 드래그 시작
                else:
                    self.dragging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.rect.x - mouse_x
                    self.offset_y = self.rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.dragging:
                self.dragging = False
                self.dropped = True
                if self.type == 'spoon':
                    self.image = self.original_image  # Revert to the original image
                    self.rect.topleft = self.original_pos  # Reset to the original position
                else:
                    pass
                self.drop_time = pygame.time.get_ticks()
                self.change_image(self.drop_image)

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x, mouse_y = event.pos
            self.rect.x = mouse_x + self.offset_x
            self.rect.y = mouse_y + self.offset_y
            if self.rect.colliderect(flour_rect):
                self.image = self.collide_image  # Change to the spoon with powder image

    def draw(self, surface):
        if self.image is not None:
            surface.blit(self.image, self.rect)

    def change_image(self, new_image):
        self.image = new_image


water_draggable = Draggable(water_image_path, pouring_water_image_path, None, 200, 200, 100, 100, 'water')
milk_draggable = Draggable(milk_image_path, pouring_milk_image_path, None, 50, 50, 100, 100, 'milk')
spoon_draggable = Draggable(spoon_image_path, spoon_image_path, spoon_with_powder_image_path, 120, 120, 100, 100, 'spoon')


# Timer for changing the additional image
change_image_event = pygame.USEREVENT + 1

# Flag to indicate if the timer is set
timer_set = False

pot_filled = False

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

        water_draggable.handle_event(event)
        milk_draggable.handle_event(event)
        spoon_draggable.handle_event(event)

    # If the Draggable object is dropped and the timer is not already set, start the timer
    if water_draggable.dropped and not stop_cycling and not timer_set:
        pygame.time.set_timer(change_image_event, 1500)
        timer_set = True

    # 물이 드롭되었는지 확인
    if water_draggable.dropped:
        # 물 채우기 효과
        if alpha_value < 255:
            alpha_value += 1  # 알파 값을 서서히 증가
            full_pot.set_alpha(alpha_value)
        else:
            pot_filled = True

    # If the Draggable object has been reset, stop the timer
    if not water_draggable.dragging and not water_draggable.dropped and timer_set:
        pygame.time.set_timer(change_image_event, 0)
        timer_set = False

    # If the Draggable object is dropped and the timer is not already set, start the timer
    if milk_draggable.dropped and not stop_cycling and not timer_set:
        pygame.time.set_timer(change_image_event, 1500)
        timer_set = True

    # If the Draggable object has been reset, stop the timer
    if not milk_draggable.dragging and not milk_draggable.dropped and timer_set:
        pygame.time.set_timer(change_image_event, 0)
        timer_set = False

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the flour image
    screen.blit(flour_image, flour_rect)

    if pot_filled == False:
        screen.blit(empty_pot, (0, 0))

    # 물이 찬 냄비 이미지를 알파값과 함께 그림 (물이 채워지는 효과)
    if water_draggable.dropped or pot_filled == True:
        screen.blit(full_pot, (0, 0))

    # Draw the additional image
    draw_additional_image(screen, current_index)

    # Draw the draggable objects
    water_draggable.draw(screen)
    milk_draggable.draw(screen)
    spoon_draggable.draw(screen)  # Draw the spoon draggable

    # Update the display
    pygame.display.update()

    # fps 조절
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()