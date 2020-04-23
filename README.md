# Semester-Project
Inputting a Hasse diagram and outputting an ordering for the same
The solution to the given problem can be summarized in the following steps:
Storing the given directed edges between two courses in a list. 
Using the list to calculate the levels of each course. 
Using this hierarchy to create a structure, which we will call Neem for this project. Neem emulates the functioning of Hasse Diagram on a computer screen. 
Printing this Hasse Diagram from its lowest levels to the highest level in sequential order. 
This output is considered as the result of the given problem. 
Key: 
Directed Edges: The connection described between two courses is only one-sided, that is, if the given edge is A - B, it implies that we can do course B only after doing course A. 

Levels: The levels of each course refer to their position in the structure created which emulates the Hasse Diagram. A structure such as: 

    - C -
  -       -
A           B
			Fig. 1A 

In this structure, the levels for A and B are 0, whereas the level for C is 1. Further details regarding its calculation are mentioned under the Execution category. 

Neem: A structure used in the solution to emulate the functioning of a Hasse Diagram.
Execution: 
We use the Graph data structure as the foundation for Neem. When the user provides input to the program, the input is stored as a branch in Neem. For eg: If the input is A-C, we form a branch starting from A to C as in Fig. 1A. 
In this branch, we can only move from A to C and not the other way around. Hence, the formation of a directed edge. 	
Once we form the whole structure, we calculate the levels of each course in Neem.  We calculate the levels by scanning every element using a recurrence function get_levels(). There are two cases: 
The element does not have any children, it’s termed as a leaf node and we assign it level 0. 
The element has children, we move to one of the children. We have two further subcases here: 
 If the level for the child has been calculated, we return the level back to the parent and add 1 to it. 
If the level for the child is not calculated yet, we calculate the level by calling the same recurrence function, get_levels() on the child. 
Similarly, we move on to the next child(if any) and perform the same steps as above. 
The level for the current element is the maximum of all the levels returned from the children. 
Once all the levels are calculated, we print Neem by first creating a matrix where rows represent the levels in Neem and the elements of these rows represent the course that has been assigned that level. 
Finally, we print this matrix and achieve the required output. 

Keyword:
Children: The courses connected to the course into consideration where the courses are a requirement for the current course. 

Leaf Node: The course in Neem does not have any children or no prior requirement to pursue the course. 


