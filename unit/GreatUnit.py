class GreatUnit(object):
    """docstring for GreatUnit"""

    def __init__(self):
        super(GreatUnit, self).__init__()
        self.happy = True
        self.madd = False

    def list_stepper(self, _list, step):
        return _list[::step]
