import sys
import bpy
import json
import codecs

# get args from console
count = int(sys.argv[-1])

C = bpy.context
depsgraph = C.evaluated_depsgraph_get()

# set geometry node parameter
bpy.data.node_groups["test"].nodes['Resample Curve'].inputs[2].default_value = count

# make sure call this method to update data!!
bpy.context.view_layer.update()

data = []

# if the object is instance, we can record its value of transform matrix
for object_instance in depsgraph.object_instances:
    obj = object_instance.object
    if object_instance.is_instance:
        print(object_instance.matrix_world)
        data.append(object_instance.matrix_world)
print("count: ", len(data))