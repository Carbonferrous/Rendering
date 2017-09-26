# -*- coding: utf-8 -*-
# ojbects, scene description object properties
import math


# rays of form ([origin], [direction])
def ray_normalize(ray):
    rd = ray[1]
    norm = math.sqrt(rd[0]**2 + rd[1]**2 + rd[2]**2)
    rd = list(i/norm for i in rd)
    return [ray[0], rd]


# default object, with location, rotation, scale, and other data
class Obj:
    def __init__(self):
        self.name = ""
        self.loc = (0, 0, 0)
        self.rot = [0, 0]
        self.scale = [1, 1, 1]
        self.data = []

    def apply_scale(self):
        pass

    def apply_rotation(self):
        pass

    def intersects(self, ray):
        '''determines if the given ray intersects the object.
           -1 is returned if false'''
        return -1

    def texture(self, ray, t):
        x = ray[0][0] + t*ray[1][0]
        y = ray[0][1] + t*ray[1][1]
        z = ray[0][2] + t*ray[1][2]
        return (int(x*255/self.radius), int(y*255/self.radius), int(z*255/self.radius))


class sphere(Obj):
    def __init__(self, center, radius):
        Obj.__init__(self)
        self.name = 'sphere'
        self.radius = radius
        self.loc = center

    def intersects(self, ray):
        ray = ray_normalize(ray)
        r0, rd = ray
        x0, y0, z0 = r0
        xd, yd, zd = rd
        xc, yc, zc = self.loc
        B = 2 * (xd * (x0 - xc) + yd * (y0 - yc) + zd * (z0 - zc))
        C = (x0 - xc)**2 + (y0 - yc)**2 + (z0 - zc)**2 - self.radius**2
        disc = B**2 - 4*C
        if disc < 0:
            return -1
        t0 = (- B - disc**(1/2)) / 2
        if t0 > 0:
            return t0
        t1 = (- B + disc**(1/2)) / 2
        return t1


class camera(Obj):
    def __init__(self, location, rotation, focus, sensor_size):
        Obj.__init__(self)
        self.loc = location
#        self.pointing = pointing
        self.rot = rotation
        self.name = 'camera'
        self.focus = focus
        self.sensor_size = sensor_size
        self.angle_of_view = [2*math.atan(sensor_size[0]/(2*focus)), 2*math.atan(sensor_size[1]/(2*focus))]


class light(Obj):
    def __init__(self, location, intensity):
        Obj.__init__(self)
        self.loc = location
        self.intensity = intensity


class material:
    def __init__(self, image, size):
        pass
        