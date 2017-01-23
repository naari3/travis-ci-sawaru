from unit import GreatUnit


class TestUpload:

    @classmethod
    def setup_class(cls):
        cls.unit = GreatUnit()

    def test_list_step(self):
        result = self.unit.list_stepper([i for i in range(10)], 2)
        assert result == [0, 2, 4, 6, 8]

    def test_happy(self):
        assert self.unit.happy
