


#pip install trimesh
#pip install "pyglet<2"
import trimesh

s = trimesh.creation.icosphere(radius=2,
                               subdivisions=1)

s.show()