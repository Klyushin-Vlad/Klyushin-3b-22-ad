class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self, time):
        print(self.name, " пройдет путь в ", self.speed * time, " м за ", time, " час(ов)")


class СrawlerRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory


class WheelsRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand