# -*- coding: utf-8 -*-
import obj
import render_engine
import PIL

#read/load file/scene, need to change to json (readable scene description)
#   image render size, camera location, background, objects in scene
flag = True
objects = []
read_name_object = {"sphere": obj.sphere, "camera": obj.camera}
with open("test.scene", 'r') as f:
    width, height = list(map(int, f.readline().strip().split()))
    for line in f:
        a = line.strip()
        if not a == '':
            a = a.split()
            objects += [read_name_object[a[0]](*a[1:])]
print(objects)

#
#wireframe render
#    scene manipulation
#path tracing
#    brdf

#create image
samples = 256
pic = PIL.Image.new("RGB", (width, height), 0)
# begin render
im = pic.load()
for i in range(pic.size[1]):
    for j in range(pic.size[0]):
        color = (0, 0, 0)
        for n in range(samples):
            ray = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            c = render_engine.path_trace(ray, 0)
            color = tuple(color[m]+c[m] for m in range(3))
        im[i, j] = tuple(int(color[n]/samples) for n in range(3))

# save and display image
pic.save('test.png')
pic.show()
