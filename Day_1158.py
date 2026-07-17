


#pip install trimesh
#pip install "pyglet<2"

import trimesh

c = trimesh.creation.capsule(radius=1,
                             height=3,
                             count=[8,8])

c.show()