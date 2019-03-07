class Consumable(object):
    def __init__(self, name):
        self.name = name


class Armor(object):
    def __init__(self, name):
        self.name = name


class Helmet(Armor):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.name = name
        self.shield = 10


class Shield(Consumable):
    def __init__(self, name):
        super(Shield, self).__init__(name)
        self.name = name
        self.shield = 0
    
    def use(self):
        self.shield += 50
        print("Now I have", self.shield, "shield")


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


class DMR(Weapon):
    def __init__(self, name):
        super(DMR, self).__init__(name)
        self.bullets_left = 12

    def press_trigger(self):
        self.bullets_left -= 1
        print("Oh I have", self.bullets_left, "bullets left.")

    def reload(self):
        self.bullets_left = 12
        print("Now I have 12 bullets")
