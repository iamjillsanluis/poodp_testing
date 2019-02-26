from pytest import approx
from app.wheel import Wheel


class TestWheel(object):
    def setup(self):
        self.wheel = Wheel(26, 1.5)

    def test_implements_the_diameterizable_interface(self):
        assert hasattr(self.wheel, 'diameter')

    def test_calculates_diameter(self):
        assert 29 == approx(self.wheel.diameter, 0.01)
