class Gear(object):
    def __init__(self, chainring, cog, wheel, observer):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
        self.observer = observer

    @property
    def gear_inches(self):
        return self.ratio * self.wheel.diameter

    @property
    def ratio(self):
        return self.chainring / self.cog

    def set_cog(self, new_cog):
        self.cog = new_cog
        self._changed()

    def set_chainring(self, new_chainring):
        self.chainring = new_chainring
        self._changed()

    def _changed(self):
        self.observer.changed(self.chainring, self.cog)
