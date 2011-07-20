#!/usr/bin/python


import sys
import numpy as np
import octree

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        p = f.readlines()
    f.closed


    print "loading carbons..."
    carbons = []
    for i,line in enumerate(p):
        if i % 100000 == 0:
            print "."
        letter, x, y, z = line.split('\t')
        carbons.append([i, float(x), float(y), float(z), 0, 0 ,0])

    bond_len_max = 2
    carbons = np.array(carbons)
    xs = carbons[:,1]
    ys = carbons[:,2]
    zs = carbons[:,3]
    maxx = xs.max()
    minx = xs.min()
    maxy = ys.max()
    miny = ys.min()
    maxz = zs.max()
    minz = zs.min()
    del p


    print maxx,maxy,maxz,minx,miny,minz

    def distance_formula(c1,c2):
        dist = (c2[1] - c1[1])**2 + (c2[2] - c1[2])**2 + (c2[3] - c1[3])**2
        return dist

    print "Creating octree"
    tree = octree.Octree(maxx, maxy, maxz, minx, miny, minz, maxiter=7)
    s = carbons[0]
    for i in s:
        print i
    print "inserting node"
    for i in carbons:
        if i[0] % 100000 == 0:
            print "adding numebr {0}".format(i)
        tree.add_item(i[0], (i[1],i[2],i[3]))

#    for i in carbons:
#        if i[0] % 100000 == 0:
#            print "adding numebr {0}".format(i)
#        tree.add_item(i[0], (i[1],i[2],i[3]))
    #get some data
    print "adding things complete"
    for i in carbons[:10]:
        print i
        entries = tree.find_within_range((i[1], i[2], i[3]), 20000, "cube")
        print entries



