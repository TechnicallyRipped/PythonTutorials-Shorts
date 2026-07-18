


#pip install trimesh
#pip install "pyglet<2"
import trimesh

c1 = trimesh.creation.box(extents=[1,1,1])
c2 = trimesh.creation.box(extents=[2,2,2])

c1.apply_translation([1.5, 0, 0])

combined = c1 + c2

combined.show()