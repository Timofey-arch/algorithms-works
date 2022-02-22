class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return ((point.x >= self.x - self.w) and (point.x <= self.x + self.w)
                and (point.y >= self.y - self.h) and (point.y <= self.y + self.h))


class Quadtree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False
        self.NE = None
        self.NW = None
        self.SE = None
        self.SW = None

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        ne = Rectangle(x + w / 2, y - h / 2, w / 2, h / 2)
        self.NE = Quadtree(ne, self.capacity)
        nw = Rectangle(x - w / 2, y - h / 2, w / 2, h / 2)
        self.NW = Quadtree(nw, self.capacity)
        se = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        self.SE = Quadtree(se, self.capacity)
        sw = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        self.SW = Quadtree(sw, self.capacity)
        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.NE.insert(point):
                return True
            elif self.NW.insert(point):
                return True
            elif self.SE.insert(point):
                return True
            elif self.SW.insert(point):
                return True
