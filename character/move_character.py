import pygame

screen_width = 1280
screen_height = 860

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

