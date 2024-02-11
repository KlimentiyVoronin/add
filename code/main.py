from game import Game
from gtts import gTTS
import os
def main():
    audio()
    game = Game(720, 480)  # Создание объекта игры
    game.run()
def audio():
    audio=gTTS(text='Он толстенький,он очаровательный ,он пахнет мёдом!Это же попугай какапо',
        lang='ru',
        slow=False)
    audio.save('img and music/file.mp3')
    os.system('start img and music/file.mp3')
if __name__ == "__main__":  # Если файл запущен как исполняемый
    main()  # Запустить главную функцию