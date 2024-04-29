import pygame
from player import Player
from gtts import gTTS
import os

class Game:
    def __init__(self, screen_width:int=500, screen_height:int=500)->None:
        """ 
        Создает объект для управления игрой. 
        
        :param screen_width: Ширина экрана
        :param screen_height: Высота экрана
        """
        pygame.init()
        self.__width:int = screen_width
        self.__height:int = screen_height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg_color:tuple = (255, 255, 255)  # Белый цвет

        self.__fps:int = 60
        self.__clock = pygame.time.Clock()

        self.__game_end:bool = False
        self.__acceleration_of_gravity:float= 9.8 / self.__fps

        self.__player:Player = Player(self.__width, self.__height)

    def __del__(self)->None:
        """ 
        Вызывается при удалении объекта Game. Освобождает ресурсы.
        """
        pygame.quit()

    def run(self)->None:
        """ 
        Запускает основной игровой цикл.
        """
        self.audio()
        while not self.__game_end:
            self.__check_events()
            self.__move()
            self.__logic()
            self.__draw()
            self.__clock.tick(self.__fps)
    def __check_events(self)->None:
        """ 
        Проверяет события ввода игры.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end:bool = True
            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and\
               event.key in self.__player.get_direction_keys():
                self.__player.check_event(event)

    def __move(self)->None:
        """ 
        Обрабатывает перемещение игрока.
        """
        self.__player.move(self.__acceleration_of_gravity)

    def __logic(self)->None:
        """ 
        Обрабатывает логику игры.
        """
        self.__player.check_wall_collision(self.__width, self.__height)

    def __draw(self)->None:
        """ 
        Отображает игровые объекты на экране.
        """
        self.__screen.fill(self.__bg_color)
        self.__player.draw(self.__screen)
        pygame.display.flip()
    @staticmethod
    def audio()->None:
        """ 
        Воспроизводит аудио-сообщение о попугае.
        """
        audio_d=gTTS(text='Он толстенький,он очаровательный ,он пахнет мёдом!Это же попугай какапо',
            lang='ru',
            slow=False)
        audio_d.save('img_and_music/file.mp3')
        os.system('start img_and_music/file.mp3')     
        