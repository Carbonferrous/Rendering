# -*- coding: utf-8 -*-
import obj
import render_engine
import PIL
import math

#read/load file/scene, need to change to modified .stl
#   render type, render size, number of objects
#   camera info:
#       location, rotation/pointing direction
#       focal length
#       sensor size
#   for each object:
#       number of triangles
#           for each triangle:
#               normal vector (i, j, k)
#               vertex 1 (x, y, z)
#               vertex 2 (x, y, z)
#               vertex 3 (x, y, z)
#   image render size, camera location, background, objects in scene
#flag = True
#objects = []
#read_name_object = {"sphere": obj.sphere, "camera": obj.camera}
#with open("test.scene", 'r') as f:
#    width, height = list(map(int, f.readline().strip().split()))
#    for line in f:
#        a = line.strip()
#        if not a == '':
#            a = a.split()
#            objects += [read_name_object[a[0]](*a[1:])]
#print(objects)

# temperary declaration of simple scene for testing. final will include file
# reader.
# objects is [camera, light, things]
width = 720
height = 720

objects = []
objects += [obj.camera((0, -5, 0), [math.pi/2, 0], 35, [24, 24])]
objects += [obj.light((0, 2, 2), 1)]
objects += [obj.sphere((0, 0, 0), 1)]

# create image
samples = 1
for i in range(312, 360, 3):
    objects[0].loc = (5*math.cos(i*math.pi/180), 5*math.sin(i*math.pi/180), 0)
    objects[0].rot = [math.pi+i*math.pi/180, 0]
    pic = PIL.Image.new("RGB", (width, height), 255)
    # render image
    render_engine.driver(pic, samples, objects, 'path_trace')
    # save and display image
    pic.save('renders\\'+str(i)+'.png')
pic.show()
