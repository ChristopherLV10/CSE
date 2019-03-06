class Consumable(object):
    def __init__(self, name):
        self.name = name


class Shield(Consumable):
    def __init__(self, name):
        super(Shield, self).__init__(name)
