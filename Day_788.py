



def jaccard_dist(s1,s2):
    intersection_ = len(s1 & s2)
    union_ = len(s1 | s2)
    return(1-(intersection_/union_))

x = {1,2,3}
y = {2,3,4,5}

print(jaccard_dist(x,y))
















