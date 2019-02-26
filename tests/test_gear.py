from pytest import approx
from app.gear import Gear


class DiameterDouble(object):
    @property
    def diameter(self):
        return 10


class TestGear(object):
    def test_calculates_gear_inches(self):
        gear = Gear(chainring=52, cog=11, wheel=DiameterDouble())
        assert 47.27 == approx(gear.gear_inches, 0.1)
