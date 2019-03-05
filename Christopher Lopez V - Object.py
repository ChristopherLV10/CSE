class Weapon(object):
    def __init__(self, shoot, reload, bullets_left=30):
        self.shoot = shoot
        self.reload = reload
        self.bullets_left = bullets_left

    def press_trigger(self):
        print("")
        bullets_left -= 1




