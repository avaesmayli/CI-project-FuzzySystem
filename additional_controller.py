class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def close_c(self, x):
        if 0 <= x < 50:
            return -x / 50 + 1
        return 0

    def moderate_c(self, x):
        if 40 <= x < 50:
            return x / 10 - 4
        if 50 <= x < 100:
            return -x / 50 + 2
        return 0

    def far_c(self, x):
        if 90 <= x < 200:
            return x / 110 - 90 / 110
        if x >= 200:
            return 1
        return 0

    def low_speed(self, x):
        if 0 <= x < 5:
            return x / 5
        if 5 <= x < 10:
            return -x / 5 + 2
        return 0

    def medium_speed(self, x):
        if 0 <= x <= 15:
            return x / 15
        if 15 < x <= 30:
            return -x / 15 + 2
        return 0

    def high_speed(self, x):
        if 25 <= x < 30:
            return x / 5 - 5
        if 30 <= x < 90:
            return -x / 60 + 9 / 6
        return 0

    def __init__(self):
        pass

    def linspace(self, start, end, count):
        dif = (end - start) / count
        res = []
        x = start
        while x < end:
            res.append(x)
            x = x + dif
        return res

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        low = self.close_c(center_dist)
        medium = self.moderate_c(center_dist)
        high = self.far_c(center_dist)

        def max_func(x):
            return max(min(low, self.low_speed(x)),
                       min(high, self.high_speed(x)),
                       min(medium, self.medium_speed(x)))
        s = 0.0
        m = 0.0
        X = self.linspace(0, 90, 1000)
        delta = X[1] - X[0]
        for i in X:
            U = max_func(i)
            s += U * i * delta
            m += U * delta
        center = 0.0
        if m != 0:
            center = 1.0 * (float(s)) / (float(m))
        return center
