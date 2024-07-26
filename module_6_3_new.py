class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        # Используем super() для вызова конструкторов родительских классов
        super().__init__()
        super(Horse, self).__init__()  # Явное указание на вызов конструктора Horse, хотя это и необязательно
        super(Eagle, self).__init__()  # Явное указание на вызов конструктора Eagle, хотя это и необязательно

    def move(self, dx, dy):
        super().run(dx)  # Вызываем метод run из класса Horse
        super().fly(dy)  # Вызываем метод fly из класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


# Пример использования:
p1 = Pegasus()

print(p1.get_pos())  # Вывод начальных позиций
p1.move(10, 15)  # Перемещение на (10, 15)
print(p1.get_pos())
p1.move(-5, 20)  # Перемещение на (-5, 20)
print(p1.get_pos())

p1.voice()  # Вывод звука Pegasus
