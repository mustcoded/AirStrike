import pickle

class LevelManager(object):

    def __init__(self, gm):

        self.game_manager = gm
        self.delete_line = False
        self.MAX_LEVEL = 3
        self.level = 1
        self.level_list = []

    def set_level(self):

        try:

            f = open("level.pickle", "rb")
            self.level_list = pickle.load(f)
            self.level = self.level_list[len(self.level_list) - 1]
            if (len(self.level_list) > 5):
                self.level_list.pop(0)

        except EOFError:
            self.level = 1
            self.level_list.append(self.level)

    def save_level(self):
        try:
            self.level_list.append(self.level)
            if(len(self.level_list) > 5):
                self.level_list.pop(0)
            f = open("level.pickle", "wb")
            pickle.dump(self.level_list, f)
            f.close()
        except IOError:
            print('cannot open a file')

    def increase_level(self):

        self.level += 1
        if(self.level >  self.MAX_LEVEL):
            self.game_manager.state = self.game_manager.WIN
            self.level = 1
            self.game_manager.setup(self.level)
        else:
            self.game_manager.state = self.game_manager.NEXT
            self.game_manager.setup(self.level)

    def get_level(self):

        return self.level

    def get_list(self):

        return self.level_list