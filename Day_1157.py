

#pip install trimesh
#pip install "pyglet<2"

import trimesh

c = trimesh.creation.cylinder(radius=1,
                              height=2,
                              sections=8)

c.show()