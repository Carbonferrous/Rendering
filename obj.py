# -*- coding: utf-8 -*-
# ojbects, scene description object properties
class Obj:
    def __init__(self):
        self.name = ""
        self.loc = (0, 0, 0)
        self.rot = [0, 0, 0]
        self.scale = [1, 1, 1]
        self.data = []
    def apply_scale(self):
        pass
    def apply_rotation(self):
        pass

class sphere(Obj):
    def __init__(self, radius, center):
        Obj.__init__(self)
        self.radius = radius
        self.loc = center
    def isintersecting(self, ray):
        pass

class camera(Obj):
    def __init__(self):
        Obj.__init__(self)
#        self.loc = location
#        self.rot = rotation
#        self.focus
    