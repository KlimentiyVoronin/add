from game import Game
def main()->None:
    '''
    Создает объект класса Game и запускает игру
    
    :game: Объект класса Game
    '''
    game:Game=Game(720,480)
    game.run()

if __name__ == "__main__": 
    main() 