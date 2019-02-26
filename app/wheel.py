from time import sleep


class Wheel(object):
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    @property
    def width(self):
        sleep(10)
        return self.rim + (self.tire * 2)
