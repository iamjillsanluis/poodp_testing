from app.wheel import Wheel


class Gear(object):
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire

    @property
    def gear_inches(self):
        return self.ratio * Wheel(self.rim, self.tire).diameter

    @property
    def ratio(self):
        return self.chainring / self.cog
