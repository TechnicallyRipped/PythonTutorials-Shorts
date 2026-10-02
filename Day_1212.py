


from argparse import ArgumentParser

p = ArgumentParser()

p.add_argument("--name")
p.add_argument("--age", type=int)

args = p.parse_args()

print(args.name)
print(args.age)