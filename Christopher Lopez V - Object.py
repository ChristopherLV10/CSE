class Gun(object):
    def __init__(self, shoot, reload, bullets_left=30):
        self.shoot = shoot
        self.reload = reload
        self.bullets_left = bullets_left

