class Wheel(object):
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    @property
    def diameter(self):
        return self.rim + (self.tire * 2)
