def circle(point, circ):
    return point in circ


class Circle:
    def __init(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, point):
        x = point[0] - self.centre[0]
        y = point[0] - self.centre[0]
        if self.radius * self.radius >= x*x + y*y:
            return True
