import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.satiety = 10
        self.alive = True
        self.gladness = 40
        self.progress = 0

    def to_eat(self):
        print("Time to eat")
        self.satiety += 12
        self.gladness += 2
        self.progress += 1
    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 5
        self.satiety -= 3
        self.progress += 1
    def to_go_on_toilet(self):
        print("Time to go on toilet")
        self.satiety -= 1
        self.gladness += 0
        self.progress += 2

    def is_alive(self):
        if self.progress < -0.5:
            print("cast out....")
            self.alive = False
        elif self.gladness <=0:
            print("Depresion")
        elif self.progress > 5:
            print("Passed extrenaly..")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")

    def live(self, day):
        day = "Day" + str(day) + 'of' + self.name + "live"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_go_on_toilet()
        self.end_of_day()
        self.is_alive()

barsik = Cat(name="barsik")
for day in range(365):
    if barsik.alive == False:
        break
    barsik.live(day)



