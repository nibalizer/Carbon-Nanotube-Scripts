
# -*- coding: utf-8 -*-
#python octree implementation
# Code © Spencer Krum June 2011
# Released underl GPLv3 See LICENSE file in this repository

class node():
    """
    Class to be a node in my octree
    """

    def __init__(self,parent, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit):
        self.parent = parent
        self.Xupperlimit = Xupperlimit
        self.Yupperlimit = Yupperlimit
        self.Zupperlimit = Zupperlimit
        self.Xlowerlimit = Xlowerlimit
        self.Ylowerlimit = Ylowerlimit
        self.Zlowerlimit = Zlowerlimit
        self.Xcenter = (self.Xupperlimit + self.Xlowerlimit)/2.
        self.Ycenter = (self.Yupperlimit + self.Ylowerlimit)/2.
        self.Zcenter = (self.Zupperlimit + self.Xlowerlimit)/2.

    parent = None
    value = None
    
    #children
    posXposYposZ = None
    posXposYnegZ = None
    posXnegYposZ = None
    posXposYnegZ = None
    negXposYposZ = None
    negXposYnegZ = None
    negXnegYposZ = None
    negXnegYnegZ = None

    #array of children
    chidren = [posXposYposZ,posXposYnegZ,posXnegYposZ,posXposYnegZ,negXposYposZ,negXposYnegZ,negXnegYposZ,negXnegYnegZ]

    #position in space
    Xupperlimit = None
    Yupperlimit = None
    Zupperlimit = None
    
    Xlowerlimit = None
    Ylowerlimit = None
    Zlowerlimit = None
    def get_array_of_children(self):
        """
        helper function to return array of children
        because there is some weird issue where just setting an 
        array variable isn't cutting it
        """
        children = [self.posXposYposZ,self.posXposYnegZ,self.posXnegYposZ,self.posXposYnegZ,self.negXposYposZ,self.negXposYnegZ,self.negXnegYposZ,self.negXnegYnegZ ]        
        return children

    def print_types(self):
        """
        helper function to printout types of children
        I know, terribly unpythonic of me, rabble rabble
        """
        print type(self.posXposYposZ)
        print type(self.posXposYnegZ)
        print type(self.posXnegYposZ)
        print type(self.posXposYnegZ)
        print type(self.negXposYposZ)
        print type(self.negXposYnegZ)
        print type(self.negXnegYposZ)
        print type(self.negXnegYnegZ)
    def print_info(self):
        """
        helper function to dump node paramaters
        """

        print "parent:\t {0}".format(self.parent)
        print "value:\t {0}".format(self.value)
        
        #children
        print "posXposYposZ: \t {0}".format(self.posXposYposZ)
        print "posXposYnegz: \t {0}".format(self.posXposYnegZ)
        print "posXnegYposZ: \t {0}".format(self.posXnegYposZ)
        print "posXposYnegZ: \t {0}".format(self.posXposYnegZ)
        print "negXposYposZ: \t {0}".format(self.negXposYposZ)
        print "negXposYnegZ: \t {0}".format(self.negXposYnegZ)
        print "negXnegYposZ: \t {0}".format(self.negXnegYposZ)
        print "negXnegYnegZ: \t {0}".format(self.negXnegYnegZ) 

        #position in space
        print "Xupperlimit: \t {0}".format(self.Xupperlimit)
        print "Yupperlimit: \t {0}".format(self.Yupperlimit)
        print "Zupperlimit: \t {0}".format(self.Zupperlimit)
        
        print "Xlowerlimit: \t {0}".format(self.Xlowerlimit)
        print "Ylowerlimit: \t {0}".format(self.Ylowerlimit)
        print "Zlowerlimit: \t {0}".format(self.Zlowerlimit)

        print "Xcenter: \t {0}".format(self.Xcenter)
        print "Ycenter: \t {0}".format(self.Ycenter)
        print "Zcenter: \t {0}".format(self.Zcenter)

            
    def add(self, payload, coord, level):
        
        """
        Create a subnode
        """

        if level == 0:
            self.value.append((coord,payload))

        else:
            level -= 1
            #Determine quadrant
            if coord[0] <= self.Xcenter:
                #negX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.negXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYnegZ.add(payload, coord, level)
                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.negXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYposZ.add(payload, coord, level)
                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.negXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.negXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYposZ.add(payload, coord, level)


            else:
                #posX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.posXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.posXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYposZ.add(payload, coord, level)

                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Zcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.posXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.posXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYposZ.add(payload, coord, level)


        

            
            


class octree():
    """
    class to hold the whole tree
    """
    
    def __init__(self, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin, root_coords=(0,0,0), maxiter=7):
        self.Xmax = Xmax
        self.Ymax = Ymax
        self.Zmax = Xmax
        self.Xmin = Xmin
        self.Ymin = Ymin
        self.Zmin = Zmin
        self.root_coords = root_coords
        self.maxiter = maxiter
        
        self.root = node('root', Xmax, Ymax, Zmax, Xmin, Ymin, Zmin)

    def add_item(self, payload, coord):
        """
        Create recursively create subnodes until maxiter is reached
        then deposit payload in that node
        """

        self.root.add(payload, coord, self.maxiter)

    def find_within_range(self, center, size, shape):
        """
        Return payloads and coordinates of every payload within
        a specified area
        """
        if shape == "box":
            """
            This deals with things around the center of a node in a box shape
            with a radius of 'size'
            It would be totally good to make a spere search space
            """
            """
            It works by making the (correct I think) assumption that the box
            shape has 8 vertices. To determine the overlap between the search
            space and the node area is hard. We can start by identifying which 
            of the 8 children of the current node overlap with the search space.
            The assumption is that if the search box overlaps in any part with
            a child, then the most extreme vertex will be within the child. 

            Let me put it 2 dimensions with ascii art:

            Fig1. A Quadtree Node Space with children space labeled 

            1,-1--------1,0--------1,1
            |           |           |
            |  child_4  |  child_1  |
            |           |           |
           -1,0---------0,0--------1,0
            |           |           |
            |  child_3  |  child_2  | 
            |           |           |
          (-1,-1)-----(-1,0)-----(-1,1)

            
            The four children of this node are:

            child_1 has the following attributes 

            . node name is posXposY
            . initial value is Null
            . Once recursively filled out, its value is another node
            . it represents the rectangular area between ((0,0),(1,0)) and ((1,0), (1,1))
            . its center is at the center of the rectangular area it represents

             
            Children _2, _3, _4 are much the same

            Fig2. Quadtree Node Space with superimposed search space 


            /-----------------------\ 
            |           |           |
            |           |           |
            |     |-------|         |
            |-----|-------|---------| 
            |     |     | |         |
            |     |-------|         | 
            |           |           |
            \-----------------------/  


            Fig3. Fig2 Zoomed

            /---------------------------------------------------------------\
            |                                                ||   <child_1> |
            |    <child_4>                                   ||  <point A>  |
            |                                                ||        |    |
            |                <selection space>               ||        V    |
            |    0+++++++++++++++++++++++++++++++++++++++++++++++++++++0    |
            |    +                                           ||<exact  +    |
            |    +                             <x-axis>      || center>+    |
            |====+===========================================%%========+====|
            |    +                                           ||        +    |
            |    +                                           ||        +    |
            |    +                                           ||        +    |
            |    +                                          ^||        +    |
            |    +                                          y||        +    |
            |    +                                          -||        +    |
            |    +                                          a||        +    |
            |    +                                          x||        +    |
            |    +                                          i||        +    |
            |    +                                          s||        +    |
            |    +                                          v||        +    |
            |    +                                           ||        +    |
            |    +                                           ||        +    |
            |    0+++++++++++++++++++++++++++++++++++++++++++++++++++++0    |
            |             <child_3>                          ||   <child_2> |
            \---------------------------------------------------------------/


            Fig4. Quadtree Node Space with different superimposed search space 


            /-----------------------\ 
            |           |           |
            |           |           |
            |     |---| |           |
            |-----|---|-------------| 
            |     |   | |           |
            |     |---| |           | 
            |           |           |
            \-----------------------/  


            Fig5. Fig2 Zoomed

            /---------------------------------------------------------------\
            |                                                ||             |
            |    <child_4>                                   ||  <child_1>  |
            |                                    <point B>   ||             |
            |                <selection space>   |           ||             |
            |    0+++++++++++++++++++++++++++0 <--           ||             |
            |    +                           +               ||<exact       |
            |    +                           + <x-axis>      || center>     |
            |====+===========================+===============%%=============|
            |    +                           +               ||             |
            |    +                           +               ||             |
            |    +                           +               ||             |
            |    +                           +              ^||             |
            |    +                           +              y||             |
            |    +                           +              -||             |
            |    +                           +              a||             |
            |    +                           +              x||             |
            |    +                           +              i||             |
            |    +                           +              s||             |
            |    +                           +              v||             |
            |    +                           +               ||             |
            |    +                           +               ||             |
            |    0+++++++++++++++++++++++++++0               ||             |
            |             <child_3>                          ||   <child_2> |
            \---------------------------------------------------------------/



            What we see in Fig2/3 vs Figi4/5 is illustrated by point A, point B
            Points A, B are the points that are the most positive in both X and
            Y. We see that if and only if this 'upper rightmost' point is within 
            child 1, then there is space in the selection overlapping part of 
            child 1. This also follows for children_2, _3, _4 and generalizes to
            the 3D space of the octree. 

            So our litmus test for 'does the selection overlap with a
            childspace?' is whether or not the most extreme(bad wording I know) 
            part of that selection is within the childspace. 
            
            """
            Xedge_max = self.center[0] + size
            Xedge_min = self.center[0] - size
            Yedge_max = self.center[1] + size
            Yedge_min = self.center[1] - size
            Zedge_max = self.center[2] + size
            Zedge_min = self.center[2] - size

            corner1 = (Xedge_max, Yedge_max, Zedge_max)
            corner2 = (Xedge_max, Yedge_max, Zedge_min)
            corner3 = (Xedge_max, Yedge_min, Zedge_max)
            corner4 = (Xedge_max, Yedge_min, Zedge_min)
            corner5 = (Xedge_min, Yedge_max, Zedge_max)
            corner6 = (Xedge_min, Yedge_max, Zedge_min)
            corner7 = (Xedge_min, Yedge_min, Zedge_max)
            corner8 = (Xedge_min, Yedge_min, Zedge_min)
            corners = [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8]
            
            investigating = []
            for node in [self.root]:
                table = ((corner1[0] > self.root.center[0]),(corner[1] > self.root.center[1]),(corner[2] > self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.posXposYposZ)
                table = ((corner2[0] > self.root.center[0]),(corner[1] > self.root.center[1]),(corner[2] < self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.posXposYnegZ)
                table = ((corner3[0] > self.root.center[0]),(corner[1] < self.root.center[1]),(corner[2] > self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.posXnegYposZ)
                table = ((corner4[0] > self.root.center[0]),(corner[1] < self.root.center[1]),(corner[2] < self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.posXnegYnegZ)
                table = ((corner5[0] < self.root.center[0]),(corner[1] > self.root.center[1]),(corner[2] > self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.negXposYposZ)
                table = ((corner6[0] < self.root.center[0]),(corner[1] > self.root.center[1]),(corner[2] < self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.negXposYnegZ)
                table = ((corner7[0] < self.root.center[0]),(corner[1] < self.root.center[1]),(corner[2] > self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.negXnegYposZ)
                table = ((corner8[0] < self.root.center[0]),(corner[1] < self.root.center[1]),(corner[2] < self.root.center[2]))
                if not False in table:
                    investigating.append(self.root.negXnegYnegZ)

        

def find_closest_three(x, y, z, tree):
    """
    function to find the closest three data points to
    a given data point
    """
    #brief sanity checking
    if (x >= tree.Xmax or x <= tree.Xmin):
        print "Fail, out of range"
    if (y >= tree.Ymax or y <= tree.Ymin):
        print "Fail, out of range"
    if (z >= tree.Zmax or z <= tree.Zmin):
        print "Fail, out of range"

    #find the node by coords
    for level in range(tree.maxiter):
        pass



    


if __name__ == "__main__":
    print "Creating octree"
    tree = octree(100,100,100, -100, -100, -100)
    print "inserting node"
    tree.add_item("derp", (10.34251,10.1234,10.9876))
    print "Great success"
    
    #get some data
    tree.root.print_info()
    for child in tree.root.chidren:
        print type(child)
    tree.root.print_types()
    for child in tree.root.get_array_of_children():
        try:
            grandchild = child.get_array_of_children()
        except AttributeError:
            print type(child)



