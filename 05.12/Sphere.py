class Sphere:
    name = ""
    color = "Red"
    size = "Big"

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        print("Объект создан!")

    def roll(self):
        print(f"Сфера {self.name} покатилась")

    def jump(self):
        print(f"Сфера цвета {self.color} с именем {self.name} и размером {self.size} прыгнула")
