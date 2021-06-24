class Student:
    """A sample Student class"""

    def __init__(self, first, last, roll_no, rank):
        self.first = first
        self.last = last
        self.roll_no = roll_no
        self.rank = rank

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}', {})".format(self.first, self.last, self.roll_no, self.rank)