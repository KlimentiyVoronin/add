"""Класс Игрока """
import pygame
class Player:
    def __init__(self, screen_width:int=500, screen_height:int=500)->None:
        """
        Инициализация игрока 

        :param screen_width: Ширина экрана 
        :param screen_height: Высота экрана
        """ 
        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load('playa.jpeg').convert_alpha(),
            (screen_width // 4, screen_height // 4)
        )
        self.__rect = self.__sprite.get_rect()
        self.__rect.x= screen_width // 2 - self.__rect.width // 2
        self.__rect.y = screen_height // 2 - self.__rect.height // 2
        self.text_color:tuple=(0,255,0)
        self.font_comicsans = pygame.font.SysFont("comicsansms", 70)
        self.text_img = self.font_comicsans.render("какапо", True, self.text_color)
        self.__horizontal_move_speed = 0
        self.__vertical_move_speed = 0
        self.__speed_max:int = 10
        self.__speed_up:float = 0.5
        self.__speed_down:float = 0.1
        self.__direction:dict = {
            pygame.K_w: False, pygame.K_a: False,
            pygame.K_s: False, pygame.K_d: False
        }

    def get_direction_keys(self)->None:
        """Получение доступных клавиш направления""" 
        return self.__direction.keys()

    def check_event(self, event:str)->None:
        """
        Проверка события 
        
        :param event: Событие
        """
        if event.type == pygame.KEYDOWN:
            self.__direction[event.key] = True
        elif event.type == pygame.KEYUP:
            self.__direction[event.key] = False

    def move(self, acceleration_of_gravity)->None:
        """
        Движение игрока

        :param acceleration_of_gravity: Ускорение свободного падения
        """ 
        self.__horizontal_move_speed += self.__speed_up * \
            (self.__direction[pygame.K_d] - self.__direction[pygame.K_a])
        if not (self.__direction[pygame.K_d] or self.__direction[pygame.K_a]):
            if abs(self.__horizontal_move_speed) < self.__speed_down:
                self.__horizontal_move_speed:int = 0
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

    def check_wall_collision(self, screen_width:int, screen_height:int):
        """
        Проверка столкновений со стенами 

        :param screen_width: Ширина экрана 
        :param screen_height: Высота экрана
        """ 
        if self.__rect.x < 0:
            self.__rect.x= 0
            self.__horizontal_move_speed:int = 0
        elif self.__rect.x > screen_width - self.__rect.width:
            self.__rect.x = screen_width - self.__rect.width
            self.__horizontal_move_speed:int = 0
        if self.__rect.y < 0:
            self.__rect.y = 0
            self.__vertical_move_speed:int = 0
        elif self.__rect.y > screen_height - self.__rect.width:
            self.__rect.y = screen_height - self.__rect.width
            self.__vertical_move_speed:int = 0
    def draw(self, screen:str)->None:
        """
        Отрисовка игрока на экране 

        :param screen: Экран
        """ 
        screen.blit(self.__sprite, self.__rect)
        screen.blit(self.text_img, (10, 10))
