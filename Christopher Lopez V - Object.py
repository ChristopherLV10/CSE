class Burst(object):
    def __init__(self, name, carrier):
        self.bullets_left = 30
        self.name = name
        self.magazine = True
        self.carrier = carrier
        self.safety_mode = False

    def press_trigger(self):
        self.bullets_left -= 3
        self.magazine = True
        self.safety_mode = False
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 30
        self.magazine = True
        print("Now I have 30 bullets")


gun = Burst(name=Burst, carrier=True)
gun.press_trigger()
gun.press_trigger()
gun.press_trigger()
gun.reload()
gun.press_trigger()

GREEN = '\033[32m'  # Green Text
print(GREEN + "This is some green text!")
