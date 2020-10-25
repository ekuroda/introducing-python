class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class SmartPhone():
    def does(self):
        return 'ring'


class Robot():
    def __init__(self, laser, claw, smart_phone):
        self.laser = laser
        self.claw = claw
        self.smart_phone = smart_phone

    def does(self):
        return f"laser:{self.laser.does()}, " + \
            f"claw:{self.claw.does()}, " + \
            f"smart_phone:{self.smart_phone.does()}"


r = Robot(Laser(), Claw(), SmartPhone())
print(r.does())
