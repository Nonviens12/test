class Cheese:
    def __init__(self, name, amount):
        self.name = name
        print("Создан сыр", name)
        self.amount = amount


    def info(self):
        print(f"{self.name} лежит, пищевая ценность {self.amount}")



class Mouse:

    def __init__(self, name, h, e):
        self.name = name
        self.health = h
        self.energy = e
        print("Мышка сосиска", self.name)


    def eating(self, cheese):
        print(f"{self.name} ест")
        self.health += cheese.amount
        if self.health > 50:
            print(f"{self.name} перерождение в БАРСИКА!!!!!!!!!!!!")
            self.health += 10
            self.energy += 50
        if self.health < 0:
            print(f"{self.name},умер,но с честью")

    def energizen(self):
        while self.energy > 0 :
            print(f"{self.name} бежит")
            self.energy -= 5
            if self.energy < 5:
                print(f"{self.name} устал")

    def info(self):
        print(f"Мышь - {self.name} - {self.health} - {self.energy}")



Mickey = Mouse("Микки", 100, 100)
lamber = Cheese("Ламбер", 5)
moldy = Cheese("c плесенью", 10)
random = Cheese("рандом", 40)

Mickey.info()
Mickey.energizen()
Mickey.info()

Mickey.eating(moldy)
Mickey.info()

