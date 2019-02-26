from pytest import approx
from app.gear import Gear
from app.wheel import Wheel


class TestGear(object):
    def test_calculates_gear_inches(self):
        gear = Gear(chainring=52, cog=11, wheel=Wheel(rim=26, tire=1.5))
        assert 137.1 == approx(gear.gear_inches, 0.1)
