import pygame
import sys
sys.path.append('..')

from imagepath import *

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# 색상 정의
BLACK = (0, 0, 0)


# 이미지 로딩
pot_image_original = pygame.image.load(pot_image_path)  # 냄비 이미지
stir_image_original = pygame.image.load(stick_image_path)  # 막대기 이미지
changed_pot_image_original = pygame.image.load(dough_image_path)  # 변할 냄비 이미지

pot_image = pygame.transform.scale(pot_image_original, (int(pot_image_original.get_width() * 0.5), int(pot_image_original.get_height() * 0.5)))
stir_image = pygame.transform.scale(stir_image_original, (int(stir_image_original.get_width() * 0.2), int(stir_image_original.get_height() * 0.2)))
pot_image_changed = pygame.transform.scale(changed_pot_image_original, (int(changed_pot_image_original.get_width() * 0.5), int(changed_pot_image_original.get_height() * 0.5)))

# 위치 설정
pot_rect = pot_image.get_rect(center=(screen_width//2, screen_height//2))
stir_rect = stir_image.get_rect()

# 이미지 변경 플래그, 충돌 시작 시간 및 드래그 상태 변수
image_changed = False
collision_start_time = None
stir_dragging = False
stir_original_pos = (screen_width // 2, screen_height // 2)  # 막대기의 초기 위치

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stir_rect.collidepoint(event.pos):
                stir_dragging = True
                stir_offset_x = stir_rect.x - event.pos[0]
                stir_offset_y = stir_rect.y - event.pos[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            stir_dragging = False
            # 드랍하면 원래 위치로
            stir_rect.x = stir_original_pos[0]
            stir_rect.y = stir_original_pos[1]
        elif event.type == pygame.MOUSEMOTION:
            if stir_dragging:
                # 드래그 중이면 막대기 이미지 위치 업데이트
                mouse_x, mouse_y = event.pos
                stir_rect.x = mouse_x + stir_offset_x
                stir_rect.y = mouse_y + stir_offset_y

    # 충돌 감지 및 이미지 변경 처리
    if pot_rect.colliderect(stir_rect):
        if collision_start_time is None:
            # 충돌 시작 시간 기록
            collision_start_time = pygame.time.get_ticks()
        else:
            # 현재 시간과 충돌 시작 시간의 차이 계산
            if (pygame.time.get_ticks() - collision_start_time) >= 3000:
                image_changed = True
    else:
        # 충돌이 끝나면 시간 기록 리셋
        collision_start_time = None

    # 화면 업데이트
    screen.fill(BLACK)
    if image_changed:
        screen.blit(pot_image_changed, pot_rect)
    else:
        screen.blit(pot_image, pot_rect)
    screen.blit(stir_image, stir_rect)

    pygame.display.flip()
    clock.tick(60)
