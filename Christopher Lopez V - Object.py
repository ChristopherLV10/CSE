class Weapon(object):
    def __init__(self, name):
        self.name = name


class Burst(Weapon):
    def __init__(self, name):
        super(Burst, self).__init__(name)
        self.bullets_left = 30

    def press_trigger(self):
        self.bullets_left -= 3
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 30
        print("Now I have 30 bullets")


gun = Burst(name=Burst)
gun.press_trigger()
gun.press_trigger()
gun.press_trigger()
gun.reload()
gun.press_trigger()
