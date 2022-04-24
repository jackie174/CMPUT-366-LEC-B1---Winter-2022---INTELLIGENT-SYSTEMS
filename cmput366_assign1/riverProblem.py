#reference:
#url: https://mark-borg.github.io/blog/2016/river-crossing-puzzles/
#author: Mark Borg
#date: 02 Nov 2016
#why cite: 
#I use graph structure from the website to build arcs
#more details in the readme.pdf

"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""
from searchProblem import Search_problem, Arc

class River_problem(Search_problem):

    def start_node(self):
        """returns start node"""

        start = ["fa_x", "fo_x", "h_x", "g_x"]
        return start
    
    def is_goal(self,node):
        """is True if node is a goal"""

        goals= ["fa_y", "fo_y", "h_y", "g_y"]
        return node == goals

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        """
        fa_x: farmer on the side x
        fo_x: fox on the side x
        g_x: garin on the side x
        h_x: hen on the side x
        convert x to y to show that they are on the side y
        Just follow the graph, it is directs on both sides
        """
        #go to frontward
        if node == ["fa_x", "fo_x", "h_x", "g_x"]:
            return [Arc(["fa_x", "fo_x", "h_x", "g_x"], ["fa_y", "fo_x", "h_y", "g_x"], 1)] #0-1
        elif node ==["fa_y", "fo_x", "h_y", "g_x"]:
            return [Arc(["fa_y", "fo_x", "h_y", "g_x"], ["fa_x", "fo_x", "h_y", "g_x"], 1)] #1-2
        elif node == ["fa_x", "fo_x", "h_y", "g_x"]:
            return [Arc(["fa_x", "fo_x", "h_y", "g_x"], ["fa_y", "fo_y", "h_y", "g_x"], 1), Arc(["fa_x", "fo_x", "h_y", "g_x"], ["fa_y", "fo_x", "h_y", "g_y"], 1) ] #2-3 #2-4
        elif node == ["fa_y", "fo_x", "h_y", "g_y"]:
            return [Arc(["fa_y", "fo_x", "h_y", "g_y"], ["fa_x", "fo_x", "h_x", "g_y"], 1)] #4-6
        elif node == ["fa_y", "fo_y", "h_y", "g_x"]:
            return [Arc(["fa_y", "fo_y", "h_y", "g_x"], ["fa_x", "fo_y", "h_x", "g_x"], 1)] #3-5
        elif node ==["fa_x", "fo_y", "h_x", "g_x"]:
            return [Arc(["fa_x", "fo_y", "h_x", "g_x"], ["fa_y", "fo_y", "h_x", "g_y"], 1)] #5-7
        elif node ==["fa_x", "fo_x", "h_x", "g_y"]:
            return [Arc(["fa_x", "fo_x", "h_x", "g_y"], ["fa_y", "fo_y", "h_x", "g_y"], 1)] #6-7
        elif node == ["fa_y", "fo_y", "h_x", "g_y"]:
            return [Arc(["fa_y", "fo_y", "h_x", "g_y"], ["fa_x", "fo_y", "h_x", "g_y"], 1)] #7-8
        elif node ==["fa_x", "fo_y", "h_x", "g_y"]:
            return [Arc(["fa_x", "fo_y", "h_x", "g_y"], ["fa_y", "fo_y", "h_y", "g_y"], 1)] #8-9
        #go to backward
        elif node == ["fa_x", "fo_y", "h_x", "g_y"]:
            return [Arc(["fa_x", "fo_y", "h_x", "g_y"], ["fa_y", "fo_y", "h_x", "g_y"], 1)] #8-7
        elif node ==["fa_y", "fo_y", "h_x", "g_y"]:
            return [Arc(["fa_y", "fo_y", "h_x", "g_y"],["fa_x", "fo_x", "h_x", "g_y"],  1), Arc(["fa_x", "fo_y", "h_x", "g_x"], ["fa_y", "fo_y", "h_x", "g_y"], 1)] #7-6 #7-5
        elif node ["fa_x", "fo_y", "h_x", "g_x"]:
            return [Arc( ["fa_x", "fo_y", "h_x", "g_x"], ["fa_y", "fo_y", "h_y", "g_x"],1)] #5-3
        elif node ["fa_x", "fo_x", "h_x", "g_y"]:
            return [Arc( ["fa_x", "fo_x", "h_x", "g_y"], ["fa_y", "fo_x", "h_y", "g_y"],1)] #6-4
        elif node ["fa_y", "fo_y", "h_y", "g_x"]:
            return [Arc(["fa_y", "fo_y", "h_y", "g_x"],["fa_x", "fo_x", "h_y", "g_x"],  1)] #3-2
        elif node :
            return [Arc(["fa_x", "fo_x", "h_y", "g_x"], ["fa_y", "fo_x", "h_y", "g_y"], 1) ] #4-2
        elif node ==["fa_x", "fo_x", "h_y", "g_x"]:
            return [Arc(["fa_x", "fo_x", "h_y", "g_x"],["fa_y", "fo_x", "h_y", "g_x"],  1)] #2-1
        else:
            return [] # assume farmer does not take items 

    def heuristic(self,node):
        """Gives the heuristic value of node n."""
        
        #len(node) -1 is only count for animals expect the farmer
        if "fa_x" in node:
            return 2*(len(node)-1) -1
        else:
            return 2*(len(node)-1)
    

