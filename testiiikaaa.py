import pygame
from gtts import gTTS
import os
class Player:
    def __init__(self, screen_width, screen_height):
        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load('player.jpeg').convert_alpha(),
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

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.__width = screen_width
        self.__height = screen_height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg_color = (255, 255, 255)  # Белый цвет

        self.__fps = 60
        self.__clock = pygame.time.Clock()

        self.__game_end = False
        self.__acceleration_of_gravity = 9.8 / self.__fps

        self.__player = Player(self.__width, self.__height)

    def __del__(self):
        pygame.quit()

    def run(self):
        while not self.__game_end:
            self.__check_events()
            self.__move()
            self.__logic()
            self.__draw()

            self.__clock.tick(self.__fps)

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True
            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and\
               event.key in self.__player.get_direction_keys():
                self.__player.check_event(event)

    def __move(self):
        self.__player.move(self.__acceleration_of_gravity)

    def __logic(self):
        self.__player.check_wall_collision(self.__width, self.__height)

    def __draw(self):
        self.__screen.fill(self.__bg_color)
        self.__player.draw(self.__screen)
        pygame.display.flip()
audio=gTTS(text='Он толстенький,он очаровательный ,он пахнет мёдом!Это же попугай какапо',
        lang='ru',
        slow=False)
audio.save('file.mp3')
os.system('start file.mp3')
# Главная функция этого Python-файла
def main():
    game = Game(720, 480)  # Создание объекта игры
    game.run()  # Запуск игры


if __name__ == "__main__":  # Если файл запущен как исполняемый
    main()  # Запустить главную функцию