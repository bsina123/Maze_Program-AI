from _tkinter import *
import math

class a_star():
    __level_heuristic = [[[0 for k in range(11)]for j in range(40)]for i in range(34)] #
    __status_goal = False

    def __init__(self,level,canvas,init_row,init_col,goal_row,goal_col,checkbox,radio):
        self.__set_drawn_canvas(canvas)
        self.__set_level(level)
        self.__init_row = init_row
        self.__init_col = init_col
        self.__goal_row = goal_row
        self.__goal_col = goal_col
        # this initializes an heuristic array
        self.__pop_heuri_list(self.__level_heuristic,self.__get_level())

        # if checkbox == 1 and radio is equal to 1 then the heuristic_visited function is called
        if checkbox ==1 and radio ==1:
            self.__heur_visited(self.__level_heuristic, self.__get_drawn_canvas())
        # if checkbox == 1 and radio == 2 then the heuristic not visited function is called
        elif checkbox == 1 and radio == 2:
            self.__heur_not_visited(self.__level_heuristic, self.__get_drawn_canvas())
        #  if checkbox == 1 and radio == 3 then the heursitic expanded function is called
        elif checkbox == 1 and radio == 3:
            self.__heur_expanded(self.__level_heuristic, self.__get_drawn_canvas())
        else: # if only the checkbox is taken then the heuristic not visited function is called
            self.__heur_not_visited(self.__level_heuristic, self.__get_drawn_canvas())

    # this function initializes the drawn canvas
    def __set_drawn_canvas(self,canvas):
        self.__drawn_canvas = canvas

    # this returns the alredy drawn level canvas
    def __get_drawn_canvas(self):
        return self.__drawn_canvas

    # this initializes the array taken from main.py
    def __set_level(self,level):
        self.__det_level = level

    # this function return the initialized array from the main.py
    def __get_level(self):
        return self.__det_level

    # calculatiing the heuristic value
    def __calculate_heuristic_value(self,x1_curr,y1_curr,x2_curr,y2_curr,x1_goal,y1_goal,x2_goal,y2_goal):
        return math.sqrt(pow(x1_curr-x1_goal,2)+pow(y1_curr-y1_goal,2)+pow(x2_curr-x2_goal,2)+pow(y2_curr-y2_goal,2))

    # this creates a three dimensional array with its specific heuristic values
    def __pop_heuri_list(self,array,canvas_array):
        for i in range(len(array)):
            for j in range(len(array[i])):
                new = []
                array[i][j][0] = canvas_array[i][j][0]
                array[i][j][1] = canvas_array[i][j][1]
                new.append(array[i][j][1])
                array[i][j][2] = canvas_array[i][j][2]
                new.append(array[i][j][2])
                array[i][j][3] = canvas_array[i][j][3]
                new.append(array[i][j][3])
                array[i][j][4] = canvas_array[i][j][4]
                new.append(array[i][j][4])
                array[i][j][6] = i
                array[i][j][7] = j
                if i==33 and j==39: array[i][j][5]=0
                else: array[i][j][5] = self.__calculate_heuristic_value(array[i][j][1],array[i][j][2],array[i][j][3],array[i][j][4],
                canvas_array[self.__goal_row][self.__goal_col][1],canvas_array[self.__goal_row][self.__goal_col][2],
                canvas_array[self.__goal_row][self.__goal_col][3],canvas_array[self.__goal_row][self.__goal_col][4])
                array[i][j][8] = 1 # defining the cost for each cell equal to one
                array[i][j][10] = []
                array[i][j][10].append(new)

    def __draw_path_canvas(self, canvas, path):
        for i in range(len(path)):
            canvas.create_rectangle(path[i][0], path[i][1], path[i][2], path[i][3], fill="red")
            canvas.after(20)
            canvas.update()

    def __add_path(self,heur_array,list):
        for i in list[10]:
            heur_array[10].append(i)

    # this function checks if a certain nodes is already visited or expanded
    def contains(self,row,col,visited_array):
        for i in range(len(visited_array)):
            if row == visited_array[i][6] and col == visited_array[i][7]: return True;
        return False

    # this function checks if two blocks have the same cost and keeps only one
    # this function is used during the searh for expanded in order to find the most optimum search
    def __check_redundancy(self,queue):
        list_redund = []
        if(len(queue)) != 1:
            for i in range(0,len(queue)-1,1):
                if queue[i][5] == queue[i+1][5]:
                    print(i+1)
                    list_redund.append(i+1)
        if len(list_redund) > 0:
            for i in range(len(list_redund)):
                queue.pop(list_redund[i]-i)


    # this function stores the children in case of expanded search
    def __store_queue_expanded(self,i,j,list,heur_array,queue,expanded):
        if j - 1 >= 0 and heur_array[i][j - 1][0] == 0 and self.contains(i, j - 1, expanded) == False:
            heur_array[i][j-1][8] = heur_array[i][j-1][8] + heur_array[i][j][8]
            heur_array[i][j-1][9] = heur_array[i][j-1][8] + heur_array[i][j-1][5]
            self.__add_path(heur_array[i][j-1],list)
            queue.append(heur_array[i][j - 1])
            expanded.insert(0, heur_array[i][j - 1])
        if i - 1 >= 0 and heur_array[i - 1][j][0] == 0 and self.contains(i-1, j, expanded) == False:
            heur_array[i-1][j][8] = heur_array[i-1][j][8] + heur_array[i][j][8]
            heur_array[i-1][j][9] = heur_array[i-1][j][8] + heur_array[i-1][j][5]
            self.__add_path(heur_array[i-1][j],list)
            queue.append(heur_array[i - 1][j])
            expanded.insert(0, heur_array[i - 1][j])
        if j + 1 <= 39 and heur_array[i][j + 1][0] == 0 and self.contains(i, j + 1, expanded) == False:
            heur_array[i][j+1][8] = heur_array[i][j+1][8] + heur_array[i][j][8]
            heur_array[i][j+1][9] = heur_array[i][j+1][8] + heur_array[i][j+1][5]
            self.__add_path(heur_array[i][j+1],list)
            queue.append(heur_array[i][j + 1])
            expanded.append(heur_array[i][j + 1])
        if i + 1 <= 33 and heur_array[i + 1][j][0] == 0 and self.contains(i + 1, j, expanded) == False:
            heur_array[i+1][j][8] = heur_array[i+1][j][8] + heur_array[i][j][8]
            heur_array[i+1][j][9] = heur_array[i+1][j][8] + heur_array[i+1][j][5]
            self.__add_path(heur_array[i+1][j],list)
            queue.append(heur_array[i + 1][j])
            expanded.insert(0, heur_array[i + 1][j])

    # this function stores the children in case of visited search
    def __store_queue_visited(self,i,j,list,heur_array,queue,visited):
        if j - 1 >= 0 and heur_array[i][j - 1][0] == 0 and self.contains(i,j-1,visited) == False:
            heur_array[i][j-1][8] = heur_array[i][j-1][8] + heur_array[i][j][8]
            heur_array[i][j-1][9] = heur_array[i][j-1][8] + heur_array[i][j-1][5]
            self.__add_path(heur_array[i][j-1],list)
            queue.append(heur_array[i][j - 1])
            visited.insert(0,heur_array[i][j-1])
        if i - 1 >= 0 and heur_array[i - 1][j][0] == 0 and self.contains(i-1,j,visited) == False:
            heur_array[i-1][j][8] = heur_array[i-1][j][8] + heur_array[i][j][8]
            heur_array[i-1][j][9] = heur_array[i-1][j][8] + heur_array[i-1][j][5]
            self.__add_path(heur_array[i-1][j],list)
            queue.append(heur_array[i - 1][j])
            visited.insert(0,heur_array[i-1][j])
        if j + 1 <= 39 and heur_array[i][j + 1][0] == 0 and self.contains(i,j+1,visited) == False:
            heur_array[i][j+1][8] = heur_array[i][j+1][8] + heur_array[i][j][8]
            heur_array[i][j+1][9] = heur_array[i][j+1][8] + heur_array[i][j+1][5]
            self.__add_path(heur_array[i][j+1],list)
            queue.append(heur_array[i][j + 1])
            visited.insert(0,heur_array[i][j+1])
        if i + 1 <= 33 and heur_array[i + 1][j][0] == 0 and self.contains(i+1,j,visited) == False:
            heur_array[i + 1][j][8] = heur_array[i + 1][j][8] + heur_array[i][j][8]
            heur_array[i + 1][j][9] = heur_array[i + 1][j][8] + heur_array[i+1][j][5]
            self.__add_path(heur_array[i+1][j],list)
            queue.append(heur_array[i + 1][j])
            visited.insert(0,heur_array[i+1][j])

    # this function stores the children in case for not visited search
    def __store_queue(self,i,j,list,heur_array,queue):
        if j - 1 >= 0 and heur_array[i][j - 1][0] == 0:
            heur_array[i][j-1][8] = heur_array[i][j-1][8] + heur_array[i][j][8]
            heur_array[i][j-1][9] = heur_array[i][j-1][8] + heur_array[i][j-1][5]
            self.__add_path(heur_array[i][j-1],list)
            queue.insert(0,heur_array[i][j - 1])
        if i - 1 >= 0 and heur_array[i - 1][j][0] == 0:
            heur_array[i - 1][j][8] = heur_array[i - 1][j][8] + heur_array[i][j][8]
            heur_array[i - 1][j][9] = heur_array[i - 1][j][8] + heur_array[i-1][j][5]
            self.__add_path(heur_array[i-1][j],list)
            queue.insert(0,heur_array[i - 1][j])
        if j + 1 <= 39 and heur_array[i][j + 1][0] == 0:
            heur_array[i][j+1][8] = heur_array[i][j+1][8] + heur_array[i][j][8]
            heur_array[i][j+1][9] = heur_array[i][j+1][8] + heur_array[i][j+1][5]
            self.__add_path(heur_array[i][j+1],list)
            queue.insert(0,heur_array[i][j + 1])
        if i + 1 <= 33 and heur_array[i + 1][j][0] == 0:
            heur_array[i + 1][j][8] = heur_array[i + 1][j][8] + heur_array[i][j][8]
            heur_array[i + 1][j][9] = heur_array[i + 1][j][8] + heur_array[i+1][j][5]
            self.__add_path(heur_array[i+1][j],list)
            queue.insert(0,heur_array[i+1][j])

    # the heur visited contains the main logic of searching algorithm
    def __heur_visited(self,heur_array,canvas):
        visited = []
        visited.append(heur_array[self.__init_row][self.__init_col])
        queue = []
        queue.append(heur_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:
            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break;
            if queue[0][6] == self.__goal_row and queue[0][7] == self.__goal_col:
                new = queue.pop(0)
                self.__draw_path_canvas(canvas, new[10])
                status_loop = False
                print("reached goal")
                break
            list = queue.pop(0)
            self.__store_queue_visited(list[6],list[7],list,heur_array,queue,visited)
            queue.sort(key=lambda x: x[9])
            canvas.create_rectangle(list[1],list[2],list[3],list[4],fill="blue")
            canvas.after(20)
            canvas.update()



    # this function contains the main logic of heur_not_visited searching algorithm
    def __heur_not_visited(self,heur_array,canvas):
        queue = []
        queue.append(heur_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:
            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break;
            if queue[0][6] == self.__goal_row and queue[0][7] == self.__goal_col:
                new = queue.pop(0)
                self.__draw_path_canvas(canvas, new[10])
                status_loop = False
                print("reached goal")
                break
            list = queue.pop(0)
            self.__store_queue(list[6], list[7],list,heur_array, queue)
            queue.sort(key=lambda x: x[9])
            canvas.create_rectangle(list[1], list[2], list[3], list[4], fill="blue")
            canvas.after(20)
            canvas.update()

    # this function containg the expanded searching algorithm procedure
    def __heur_expanded(self,heur_array,canvas):
        expanded = []
        queue = []
        queue.append(heur_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:
            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break;
            if queue[0][6] == self.__goal_row and queue[0][7] == self.__goal_col:
                new = queue.pop(0)
                self.__draw_path_canvas(canvas, new[10])
                status_loop = False
                print("reached goal")
                break
            list = queue.pop(0)
            expanded.append(list)
            self.__check_redundancy(queue)
            self.__store_queue_expanded(list[6], list[7],list,heur_array, queue,expanded)
            queue.sort(key=lambda x: x[9])
            canvas.create_rectangle(list[1], list[2], list[3], list[4], fill="blue")
            canvas.after(20)
            canvas.update()