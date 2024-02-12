import pygame
class Player:
    def __init__(self, screen_width=500, screen_height=500):
        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load('img_and_music/player.jpeg').convert_alpha(),
            (screen_width // 4, screen_height // 4)
        )
        self.__rect = self.__sprite.get_rect()
        self.__rect.x = screen_width // 2 - self.__rect.width // 2
        self.__rect.y = screen_height // 2 - self.__rect.height // 2
        self.text_color=(0,255,0)
        self.font_comicsans = pygame.font.SysFont("comicsansms", 70)
        self.text_img = self.font_comicsans.render("какапо", True, self.text_color)
        self.__color = (255, 0, 0)  # Красный цвет
        self.__horizontal_move_speed = 0
        self.__vertical_move_speed = 0
        self.__speed_max = 10
        self.__speed_up = 0.5
        self.__speed_down = 0.1
        self.__direction = {
            pygame.K_w: False, pygame.K_a: False,
            pygame.K_s: False, pygame.K_d: False
        }

    def get_direction_keys(self):
        return self.__direction.keys()

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.__direction[event.key] = True
        elif event.type == pygame.KEYUP:
            self.__direction[event.key] = False

    def move(self, acceleration_of_gravity):
        self.__horizontal_move_speed += self.__speed_up * \
            (self.__direction[pygame.K_d] - self.__direction[pygame.K_a])
        if not (self.__direction[pygame.K_d] or self.__direction[pygame.K_a]):
            if abs(self.__horizontal_move_speed) < self.__speed_down:
                self.__horizontal_move_speed = 0
            elif self.__horizontal_move_speed > 0:
                self.__horizontal_move_speed -= self.__speed_down
            else:
                self.__horizontal_move_speed += self.__speed_down
        elif self.__horizontal_move_speed > self.__speed_max:
            self.__horizontal_move_speed = self.__speed_max
        elif self.__horizontal_move_speed < -self.__speed_max:
            self.__horizontal_move_speed = -self.__speed_max


        self.__vertical_move_speed += self.__speed_up * \
            (self.__direction[pygame.K_s] - self.__direction[pygame.K_w])
        if not (self.__direction[pygame.K_s] or self.__direction[pygame.K_w]):
            self.__vertical_move_speed += acceleration_of_gravity
        elif self.__vertical_move_speed > self.__speed_max:
            self.__vertical_move_speed = self.__speed_max
        elif self.__vertical_move_speed < -self.__speed_max:
            self.__vertical_move_speed = -self.__speed_max


        self.__rect.x += self.__horizontal_move_speed
        self.__rect.y += self.__vertical_move_speed

    def check_wall_collision(self, screen_width, screen_height):

        if self.__rect.x < 0:
            self.__rect.x = 0
            self.__horizontal_move_speed = 0
        elif self.__rect.x > screen_width - self.__rect.width:
            self.__rect.x = screen_width - self.__rect.width
            self.__horizontal_move_speed = 0
        if self.__rect.y < 0:
            self.__rect.y = 0
            self.__vertical_move_speed = 0
        elif self.__rect.y > screen_height - self.__rect.width:
            self.__rect.y = screen_height - self.__rect.width
            self.__vertical_move_speed = 0
    def draw(self, screen):
        screen.blit(self.__sprite, self.__rect)
        screen.blit(self.text_img, (10, 10))
