import bpy  

verts = [
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0),
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0)
]

faces = [
    (0, 1, 2, 3),
    (4, 7, 6, 5),
    (0, 4, 5, 1),
    (1, 5, 6, 2),
    (2, 6, 7, 3),
    (4, 0, 3, 7)
]  

mesh_data = bpy.data.meshes.new("cube_mesh_data")
mesh_data.from_pydata(verts, [], faces)
mesh_data.update()

obj = bpy.data.objects.new("My_Object", mesh_data)
col =  bpy.data.collections["Collection"]
col.objects.link(obj)