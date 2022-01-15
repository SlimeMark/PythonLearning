class Destroyer(): #定义对象类为“驱逐舰”

    def __init__(self,name,types):

        self.name = name
        self.types = types
    def attack(self):

        print("ATK")