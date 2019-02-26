from pytest import approx
from app.wheel import Wheel


class TestWheel(object):
    def test_calculates_width(self):
        wheel = Wheel(26, 1.5)
        assert 29 == approx(wheel.width, 0.01)
