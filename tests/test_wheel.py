from app.wheel import Wheel


class TestWheel(object):
    def test_calculates_diameter(self):
        wheel = Wheel(26, 1.5)
        assert 29 == wheel.diameter
