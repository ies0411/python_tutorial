# example1
class Vector(object):
    def __init__(self, *args):
        """
        create v = Vector(5,10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        represent
        """
        return "vector(%r,%r)" % (self._x, self._y)

    def __add__(self, other):
        """
        add
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        """
        mul
        """
        return Vector(self._x * y, self._y * y)


v1 = Vector(5, 7)
v2 = Vector(15, 73)
v3 = Vector()

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
