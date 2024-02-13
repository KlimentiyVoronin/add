import pygame
from player import Player
from gtts import gTTS
import os

class Game:
    def __init__(self, screen_width=500, screen_height=500):
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
        self.audio()
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
    @staticmethod
    def audio():
        audio_d=gTTS(text='Он толстенький,он очаровательный ,он пахнет мёдом!Это же попугай какапо',
            lang='ru',
            slow=False)
        audio_d.save('img_and_music/file.mp3')
        os.system('start img_and_music/file.mp3')
        