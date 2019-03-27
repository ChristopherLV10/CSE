shield = 0


class Consumable(object):
    def __init__(self, name):
        self.name = name


class Backpack(object):
    def __init__(self, name):
        self.name = name


class Bag(Backpack):
    def __init__(self, name):
        super(Bag, self).__init__(name)
        self.name = name


class Key(object):
    def __init__(self, name):
        self.name = name


class EntranceKey(Key):
    def __init__(self, name):
        super(EntranceKey, self).__init__(name)
        self.name = name


class VaultKey(Key):
    def __init__(self, name):
        super(VaultKey, self).__init__(name)
        self.name = name


class Map(object):
    def __init__(self, name):
        self.name = name


class VOG(Map):
    def __init__(self, name):
        super(VOG, self).__init__(name)


class HealthPotion(Consumable):
    def __init__(self, name):
        super(HealthPotion, self).__init__(name)
        self.name = name
        self.health = 0

    def heal(self):
        print("I just gained 50 health")
        self.health += 50


class Armor(object):
    def __init__(self, name):
        self.name = name


class Helmet(Armor):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.name = name
        self.shield = 12.5


class Chest(Armor):
    def __init__(self, name):
        super(Chest, self).__init__(name)
        self.name = name
        self.shield = 12.5


class Greaves(Armor):
    def __init__(self, name):
        super(Greaves, self).__init__(name)
        self.name = name
        self.shield = 12.5


class Gauntlets(Armor):
    def __init__(self, name):
        super(Gauntlets, self).__init__(name)
        self.name = name
        self.shield = 12.5


class ShieldPotion(Consumable):
    def __init__(self, name):
        super(ShieldPotion, self).__init__(name)
        self.name = name
        self.shield = 0
    
    def use(self):
        self.shield += 50
        print("Now I have", self.shield, "shield")


class Weapon(object):
    def __init__(self, name):
        self.name = name


class Sword(Weapon):
    def __init__(self, name):
        super(Sword, self). __init__(name)
        self.durability = 5

    def slash(self):
        self.durability = 5
        print("My sword's about to break, I can only slash", self.durability, "more times")


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


class Grenade(Weapon):
    def __init__(self, name):
        super(Grenade, self).__init__(name)
        self.name = name
