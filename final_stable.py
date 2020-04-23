import tkinter as tk
from tkinter import messagebox
import queue
root = tk.Tk()

HEIGHT = 500
WIDTH = 600
#*******************************************************************#
#*******************************************************************#

class _graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

#*******************************************************************#
#*******************************************************************#

    # Function to add an edge in an undirected graph
    def add_edge(self, src, final):
        # Adding the node to the source node
        #changeing to a directed graph by commenting

        # Adding the source node to the destination as
        self.graph[final].append(src)

#*******************************************************************#
#*******************************************************************#

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            temp = self.graph[i]
            print('{}-'.format(conv_num_to_alpha(i)), end = '')
            for j in range(len(temp)):
                print(conv_num_to_alpha(temp[j]), end = ' ')
            print('')

#*******************************************************************#
#*******************************************************************#

    #Creates a 2D matrix with rows representing levels and columns in those representing the elements at that level
    def create_hierarchy_map(self):
      self.new = [[] for _ in range(max(self.level) + 1)]
      for i in range(len(self.level)):
        self.new[self.level[i]].append(i)
      return self.new

#******************************************************************#

    #Creates a list of elements with their levels as values, using DFS approach(sort of)

    def get_levels(self, node, level, visited):
      if len(self.graph[node]) == 0:
        return 0

      if visited[node] == True:
        return self.level[node]

      for j in self.graph[node]:
        self.level[node] = max(1 + self.get_levels(j, self.level, visited), self.level[node])
      visited[node] = True
      return self.level[node]

#****************************************************************#

    # A function to provide an end-product which is elements organized in hierarchy
    def create_hierarchy(self):
        self.level = [0] * self.V
        visited = [False] * self.V

        #Creates a list of elements with their levels as values
        for i in range(self.V):
          self.get_levels(i, self.level, visited)

        #Creates a 2D matrix with rows representing levels and columns in those representing the elements at that level
        self.create_hierarchy_map()

        return (self.level)

#****************************************************************#
#****************************************************************#

    def print_result(self):
      out = ""
      count_elements = 0
      for level in self.new:
          for element in level:
            count_elements += 1
            if count_elements != self.V:
              out += ("{} < ".format(conv_num_to_alpha(element)))
            else:
              out += ("{}".format(conv_num_to_alpha(element)))
      return (out)
      pass

#*****************************************************************#
#************************END OF CLASS*****************************#

def conert_alph_to_numbers(cin):
    cin = cin.lower()
    return (ord(cin) - 97)

def conv_num_to_alpha(cin):
    cin = int(cin)
    cout = chr(cin + 97)
    return cout.upper()

#*****************************************************************#
#*****************************************************************#

def take_input(graph):
    while True:
        for i in range(len(A)):
          course_1, course_2 = A[i].split('-')
          course_1 = course_1.strip().upper()
          course_2 = course_2.strip().upper()
          if (course_1 == "N") and (course_2 == "N"):
              return
          course_1 = conert_alph_to_numbers(course_1)
          course_2 = conert_alph_to_numbers(course_2)
          graph.add_edge(course_1, course_2)
        return
    pass

#*****************************************************************#

A = []

def func():
    inp = entry1.get()

    A.append(inp)
    clear_scr()

#*****************************************************************#

def clear_all():
    entry.delete(0, tk.END)

def clear_scr():
    entry1.delete(0, tk.END)

def enter():
    a = entry.get()

    try:
        num_vertices = int(a)
    except ValueError:
        print("Bad Entry")
        clear_all()
        entry.insert(0, "Error")
    global hasse
    hasse = _graph(num_vertices)
    while (num_vertices >= 26):
        try:
            print("Bad Entry, Enter course number less than 27\n")
        except ValueError:
            print("Bad Entry")
            clear_all()
            entry.insert(0, "Error")

#*****************************************************************#

def main():
    enter()
    take_input(hasse)
    hasse.create_hierarchy()
    ans = hasse.print_result()
    return (ans)

def throw_away():
    cont = main()
    clear_scr()
    entry1.insert(0, cont)

#************************************************************************************************************#
#************************************************************************************************************#

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.2, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relx= 0.3, relwidth=0.2, relheight=0.4)
label1 = tk.Label(frame, text = "Enter the number of courses", font = 40)
label1.place(rely = 0.5 , relx = 0.05, relwidth = 0.6)

button = tk.Button(frame, text="Enter", font=40, command=lambda: enter())
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.85, relheight=0.4, anchor='n')

button = tk.Button(lower_frame, text="Enter", font=40, command=lambda: func())
button.place(relx=0.72, relheight=0.4, relwidth=0.25)
button = tk.Button(lower_frame, text="Get", font=40, command=lambda: throw_away())
button.place(relx=0.36, rely = 0.7, relheight=0.3, relwidth=0.25)
entry1 = tk.Entry(lower_frame, font=30)
entry1.place( relwidth= 0.7, relheight=0.4)
label1 = tk.Label(lower_frame, text = "Input in the form <course1>-<course2>, eg: A-B", font = 40)
label1.place(rely = 0.42 , relwidth = 1)
root.mainloop()

#***************************END OF CODE*****************************#
