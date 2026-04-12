

from rich.tree import Tree
from rich import print

tree = Tree("Project")

tree.add("app.py")

folder = tree.add("data")
folder.add("users.csv")
folder.add("sales.csv")

print(tree)