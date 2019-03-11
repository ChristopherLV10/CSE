class Burst(object):
    def __init__(self, name, carrier):
        self.bullets_left = 30
        self.name = name
        self.magazine = True
        self.carrier = carrier

    def press_trigger(self):
        self.bullets_left -= 3
        self.magazine = True
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 30
        print("Now I have 30 bullets")


gun = Burst(name=Burst, carrier=True)
gun.press_trigger()
gun.press_trigger()
gun.press_trigger()
gun.reload()
gun.press_trigger()
