"""
Example solution for the River Problem.
"""
from collections import namedtuple
from searchProblem import Search_problem, Arc

State = namedtuple("State", ['here', 'other', 'loc'])

class River_problem(Search_problem):
    def __init__(self, n_grain=1, capacity=1, animal_sz=1):
        super(River_problem, self).__init__()
        self.n_grain = n_grain
        self.capacity = capacity
        self.animal_sz = animal_sz
        
    def start_node(self):
        """returns start node"""
        return State(here=set(['fox', 'hen', 'grain']),
                     other=set([]),
                     loc='left')
                     
        
    def is_goal(self,node):
        """is True if node is a goal"""
        return (node.loc=='right' and
                node.here==set(['fox', 'hen', 'grain']) and
                node.other==set([]))

    def is_valid(self,node):
        """is True if node does not violate any constraints"""

        # don't leave the hen with the grain
        if 'hen' in node.other and 'grain' in node.other:
            return False

        # don't leave the fox with the hen
        if 'fox' in node.other and 'hen' in node.other:
            return False
        return True

    def _make_arc(self, node, obj):
        """return arc to a single neighbour for moving obj from node, or [] if not valid.
           if obj is None, move without carrying anything."""
        if obj is not None and obj not in node.here:
            return []

        new_here = set(node.other)
        new_other = set(node.here)

        if obj is not None:
            new_here.add(obj)
            new_other.remove(obj)

        dest = State(loc = ('right' if node.loc=='left' else 'left'),
                     here=new_here,
                     other=new_other)

        if self.is_valid(dest):
            return [Arc(node, dest, 1, 'move-%s' % ('empty' if obj is None else obj))]
        else:
            return []
        
        
    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        return (self._make_arc(node, None) +
                self._make_arc(node, 'hen') +
                self._make_arc(node, 'grain') +
                self._make_arc(node, 'fox'))
        
    def heuristic(self,n):
        """Gives the heuristic value of node n.
        Returns 0 if not overridden."""
        if n.loc == 'left':
            # need to move right for each obj, and left for each obj but the last
            return max(2 * len(n.here) - 1, 1)
        elif n.loc == 'right':
            # need to return, and then right for each obj, plus another return for all but the last
            return 2 * len(n.other)
        else:
            raise AssertionError('invalid location')

def main():
    from searchGeneric import AStarSearcher
    s = AStarSearcher(River_problem())
    path = s.search()
    if path:
        print("Path found (cost=%s)\n%s" % (path.cost, path))
        return path

if __name__ == '__main__':
    main()
