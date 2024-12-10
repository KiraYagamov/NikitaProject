from random import randint

class Bot:
    def __init__(self, id: int, name: str, left: int, right: int):
        self.id = id
        self.name = name
        self.left = left
        self.right = right
        print(f"Бот {self.id} - {self.name} создан!")


    def ask(self) -> int:
        ask = randint(self.left, self.right)
        print(f"Бот {self.id} - {self.name} думает, что это {ask}")
        return ask
