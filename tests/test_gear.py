from unittest.mock import Mock

from pytest import approx
from app.gear import Gear


class DiameterDouble(object):
    @property
    def diameter(self):
        return 10


class TestGear(object):
    def setup(self):
        self.observer = Mock()
        self.gear = Gear(chainring=52, cog=11, wheel=DiameterDouble(), observer=self.observer)

    def test_calculates_gear_inches(self):
        assert 47.27 == approx(self.gear.gear_inches, 0.1)

    def test_notifies_observers_when_cogs_change(self):
        self.gear.set_cog(27)
        self.observer.changed.assert_called_once_with(52, 27)

    def test_notifies_observers_when_chainrings_change(self):
        self.gear.set_chainring(42)
        self.observer.changed.assert_called_once_with(42, 11)
