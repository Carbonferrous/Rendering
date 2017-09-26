# -*- coding: utf-8 -*-
from math import cos, sin


def ray_casting(ray, objects):
    maxdistance = 50
    color = (100, 100, 100)  # background color
    for o in objects:
        t = o.intersects(ray)
        if t > 0 and t < maxdistance:
            maxdistance = t
            color = o.texture(ray, t)
    return color


def ray_tracing(ray):
    pass


def path_tracing(ray, depth, maxdepth=5):
    pass
# wireframe render
#    scene manipulation
# path tracing
#    brdf


def driver(pic, samples, objects, render='ray_trace'):
    im = pic.load()
    cameraloc = objects[0].loc
    camerarot = objects[0].rot
    npicsize = pic.size[1]
    mpicsize = pic.size[0]
    haov = objects[0].angle_of_view[0]
    vaov = objects[0].angle_of_view[1]
    for i in range(npicsize):
        for j in range(mpicsize):
            color = (0, 0, 0)
            a = -vaov/npicsize*i + vaov/2 + camerarot[1]
            b = haov/mpicsize*j - haov/2 + camerarot[0]
            ray = [cameraloc, (cos(a)*cos(b), cos(a)*sin(b), sin(a))]
            for n in range(samples):
                c = ray_casting(ray, objects)
                color = tuple(color[m]+c[m] for m in range(3))
            im[j, i] = tuple(int(color[n]/samples) for n in range(3))
#        if i % 100 == 0:
#            print(int(i*100/npicsize), '%')
