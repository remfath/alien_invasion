import pygame


class Ship():
    def __init__(self, setting, screen):
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.ship_speed
        if self.move_left and self.rect.left > 0:
            self.center -= self.setting.ship_speed
        if self.move_up and self.rect.top - self.setting.ship_speed > self.screen_rect.top:
            self.bottom -= self.setting.ship_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.setting.ship_speed

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
