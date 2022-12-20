    """
Agent:
    An entity that perceives its envirment and acts upon that enviroment.

State:
    A configuration of the agent and its enviroment.

Initial State:
    The state in which the agent begins.

Actions:
    Choices that can be made in a state
    
Create a function called actions(s) which takes the state available.

Transistion States:
    
    
Goal Tests:
    A way to dertemin whether a given state is a goal state.
    
Path Costs:
    A numerical cost associated a given path.
    
    """
"""
Search Problem:
    * Initial State
    * Actions
    * Transition Model
    * Goal Test 
    * Path Cost Function 
"""

"""Node
a data structure that keeps track of:
    * a state
    * a parent (node that generated this node). The state before us.
    * an action (action applied to paren to get node)
    * a path cost( from initial stae to node)
"""

"""
Search Algotrims
    Dept-First Search (dfs)
    Breadth-First search (bfs) - Could be Memory Exhaustive 
"""