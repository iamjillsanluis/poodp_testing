class Gear(object):
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    @property
    def gear_inches(self):
        return self.ratio * self.wheel.diameter

    @property
    def ratio(self):
        return self.chainring / self.cog
