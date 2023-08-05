import numpy as np


class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def close_L(self, x):
        if 0 <= x <= 50:
            return 1 - x / 50
        return 0

    def moderate_L(self, x):
        if 35 <= x <= 50:
            return x / 15 - 7 / 3
        if 50 < x <= 65:
            return -x / 15 + 13 / 3
        return 0

    def far_L(self, x):
        if 50 < x <= 100:
            return x / 50 - 1
        return 0

    def close_R(self, x):
        if 0 <= x <= 50:
            return -x / 50 + 1
        return 0

    def moderate_R(self, x):
        if 35 <= x <= 50:
            return x / 15 - 7 / 3
        if 50 < x <= 65:
            return -x / 15 + 13 / 3
        return 0

    def far_R(self, x):
        if 50 < x <= 100:
            return x / 50 - 1
        return 0

    def high_right(self, x):
        if -50 <= x <= -20:
            return x / 30 + 50 / 30
        if -20 < x < -5:
            return -1 / 3 - x / 15
        return 0

    def low_right(self, x):
        if -10 > x > -20:
            return x / 10 + 2
        if -10 <= x < 0:
            return - x / 10
        return 0

    def nothing(self, x):
        if -10 <= x <= 0:
            return x / 10 + 1
        if 0 < x <= 10:
            return -x / 10 + 1
        return 0

    def high_left(self, x):
        if 20 <= x < 50:
            return -x / 30 + 50 / 30
        if 20 > x > 5:
            return -1 / 3 + x / 15
        return 0

    def low_left(self, x):
        if 10 < x < 20:
            return -x / 10 + 2
        if 10 >= x > 0:
            return x / 10
        return 0

    def linspace(self, start, end, count):
        dif = (end - start) / count
        res = []
        x = start
        while x < end:
            res.append(x)
            x = x + dif
        return res

    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """

        high_right = min(self.close_L(left_dist), self.far_R(right_dist))
        low_right = min(self.close_L(left_dist), self.moderate_R(right_dist))
        nothing = min(self.moderate_L(left_dist), self.moderate_R(right_dist))
        high_left = min(self.far_L(left_dist), self.close_R(right_dist))
        low_left = min(self.moderate_L(left_dist), self.close_R(right_dist))

        def max_func(x):
            return max(min(low_right, self.low_right(x)),
                       min(high_right, self.high_right(x)),
                       min(low_left, self.low_left(x)),
                       min(high_left, self.high_left(x)),
                       min(nothing, self.nothing(x)))

        s = 0.0
        m = 0.0
        X = self.linspace(-50, 50, 1000)
        delta = X[1] - X[0]
        for i in X:
            U = max_func(i)
            s += U * i * delta
            m += U * delta
        center = 0.0
        if m != 0:
            center = 1.0 * float(s) / float(m)
        return center
    