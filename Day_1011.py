


values = [10,2,4]
weights = [0.75,0.20,0.05]

r = sum(v*w for v,w in zip(values,weights))/sum(weights)
print(r)