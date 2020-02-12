import math

class greedy:
    __new_array = [[[0 for k in range(9)] for j in range(40)] for i in range(34)]

    def __init__(self,level,canvas,init_row,init_col,goal_row,goal_col,checkbox,radio):
        self.__set_drawn_canvas(canvas)
        self.__set_level(level)
        self.__init_row = init_row
        self.__init_col = init_col
        self.__goal_row = goal_row
        self.__goal_col = goal_col
        self.__new_greedy(self.__new_array,self.__get_level())

        if checkbox ==1 and radio ==1:
            self.__greedy_visited(self.__new_array, self.__get_drawn_canvas())
        elif checkbox == 1 and radio == 2:
            self.__greedy_not_visited(self.__new_array, self.__get_drawn_canvas())
        elif checkbox == 1 and radio == 3:
            self.__greedy_expanded(self.__new_array, self.__get_drawn_canvas())
        else:
            self.__greedy_not_visited(self.__new_array, self.__get_drawn_canvas())

    def __set_drawn_canvas(self,canvas):
        self.__drawn_canvas = canvas

    def __get_drawn_canvas(self):
        return self.__drawn_canvas

    def __set_level(self,level):
        self.__det_level = level

    def __get_level(self):
        return self.__det_level

    #def __calculate_distance(self,)
    def __calculate(self,array,curr_x1,curr_y1,curr_x2,curr_y2,goal_x1,goal_y1,goal_x2,goal_y2):
        array[5] = math.sqrt(pow(curr_x1-goal_x1,2)+pow(curr_y1-goal_y1,2)+pow(curr_x2-goal_x2,2)+pow(curr_y2-goal_y2,2))

    def __new_greedy(self,array,canvas_array):
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
                array[i][j][8] = []
                array[i][j][8].append(new)

    def contains(self,row,col,visited_array):
        for i in range(len(visited_array)):
            if row == visited_array[i][6] and col == visited_array[i][7]: return True;
        return False

    def __add_path(self,greedy_array,list):
        for i in list[8]:
            greedy_array[8].append(i)

    def __store_queue_expanded(self,i,j,list,heur_array,queue,expanded):
        if j - 1 >= 0 and heur_array[i][j - 1][0] == 0 and self.contains(i, j-1, expanded) == False:
            self.__calculate(heur_array[i][j-1],heur_array[i][j-1][1], heur_array[i][j-1][2],heur_array[i][j-1][3],heur_array[i][j-1][4],
            heur_array[self.__goal_row][self.__goal_col][1], heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3], heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i][j-1],list)
            queue.append(heur_array[i][j - 1])
        if i - 1 >= 0 and heur_array[i - 1][j][0] == 0 and self.contains(i-1, j, expanded) == False:
            self.__calculate(heur_array[i-1][j], heur_array[i-1][j][1], heur_array[i-1][j][2],heur_array[i-1][j][3], heur_array[i-1][j][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i-1][j],list)
            queue.append(heur_array[i - 1][j])
        if j + 1 <= 39 and heur_array[i][j + 1][0] == 0 and self.contains(i, j+1, expanded) == False:
            self.__calculate(heur_array[i][j+1], heur_array[i][j+1][1], heur_array[i][j+1][2],heur_array[i][j+1][3], heur_array[i][j+1][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i][j+1],list)
            queue.append(heur_array[i][j + 1])
        if i + 1 <= 33 and heur_array[i + 1][j][0] == 0 and self.contains(i+1, j, expanded) == False:
            self.__calculate(heur_array[i+1][j], heur_array[i+1][j][1], heur_array[i+1][j][2],heur_array[i+1][j][3], heur_array[i+1][j][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i+1][j],list)
            queue.append(heur_array[i + 1][j])

    def __store_queue_visited(self,i,j,list,heur_array,queue,visited):
        if j - 1 >= 0 and heur_array[i][j - 1][0] == 0 and self.contains(i,j-1,visited) == False:
            self.__calculate(heur_array[i][j - 1], heur_array[i][j - 1][1], heur_array[i][j - 1][2],heur_array[i][j - 1][3], heur_array[i][j - 1][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i][j - 1], list)
            queue.append(heur_array[i][j - 1])
            visited.append(heur_array[i][j-1])
        if i - 1 >= 0 and heur_array[i - 1][j][0] == 0 and self.contains(i-1,j,visited) == False:
            self.__calculate(heur_array[i-1][j], heur_array[i-1][j][1], heur_array[i-1][j][2],heur_array[i-1][j][3], heur_array[i-1][j][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i - 1][j], list)
            queue.append(heur_array[i - 1][j])
            visited.append(heur_array[i-1][j])
        if j + 1 <= 39 and heur_array[i][j + 1][0] == 0 and self.contains(i,j+1,visited) == False:
            self.__calculate(heur_array[i][j+1], heur_array[i][j+1][1], heur_array[i][j+1][2],heur_array[i][j+1][3], heur_array[i][j+1][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i][j+1],list)
            queue.append(heur_array[i][j + 1])
            visited.append(heur_array[i][j+1])
        if i + 1 <= 33 and heur_array[i + 1][j][0] == 0 and self.contains(i+1,j,visited) == False:
            self.__calculate(heur_array[i+1][j], heur_array[i+1][j][1], heur_array[i+1][j][2],heur_array[i+1][j][3], heur_array[i+1][j][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i+1][j],list)
            queue.append(heur_array[i + 1][j])
            visited.append(heur_array[i+1][j])

    def __store_queue(self,i,j,list,heur_array,queue):
        if j - 1 >= 0 and heur_array[i][j - 1][0] == 0:
            self.__calculate(heur_array[i][j-1], heur_array[i][j-1][1], heur_array[i][j-1][2],heur_array[i][j-1][3], heur_array[i][j-1][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i][j-1],list)
            queue.append(heur_array[i][j - 1])
        if i - 1 >= 0 and heur_array[i - 1][j][0] == 0:
            self.__calculate(heur_array[i-1][j], heur_array[i-1][j][1], heur_array[i-1][j][2],heur_array[i-1][j][3], heur_array[i-1][j][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i-1][j],list)
            queue.append(heur_array[i - 1][j])
        if j + 1 <= 39 and heur_array[i][j + 1][0] == 0:
            self.__calculate(heur_array[i][j + 1], heur_array[i][j + 1][1], heur_array[i][j + 1][2],heur_array[i][j + 1][3], heur_array[i][j + 1][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i][j+1],list)
            queue.append(heur_array[i][j + 1])
        if i + 1 <= 33 and heur_array[i + 1][j][0] == 0:
            self.__calculate(heur_array[i+1][j], heur_array[i+1][j][1], heur_array[i+1][j][2],heur_array[i+1][j][3], heur_array[i+1][j][4],
            heur_array[self.__goal_row][self.__goal_col][1],heur_array[self.__goal_row][self.__goal_col][2],
            heur_array[self.__goal_row][self.__goal_col][3],heur_array[self.__goal_row][self.__goal_col][4])
            self.__add_path(heur_array[i+1][j], list)
            queue.append(heur_array[i + 1][j])


    def __draw_path_canvas(self,canvas,path):
        for i in range(len(path)):
            canvas.create_rectangle(path[i][0],path[i][1],path[i][2],path[i][3],fill="red")
            canvas.after(20)
            canvas.update()

    def __greedy_visited(self,greedy_array,canvas):
        visited = []
        visited.append(greedy_array[self.__init_row][self.__init_col])
        queue = []
        queue.append(greedy_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:
            queue.sort(key=lambda x: x[5])
            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break
            if queue[0][6] == self.__goal_row and queue[0][7] == self.__goal_col:
                status_loop = False
                new = queue.pop(0)
                self.__draw_path_canvas(canvas, new[8])
                print("reached goal")
                break
            list = queue.pop(0)
            self.__store_queue_visited(list[6],list[7],list,greedy_array,queue,visited)
            canvas.create_rectangle(list[1],list[2],list[3],list[4],fill="blue")
            canvas.after(20)
            canvas.update()

    def __greedy_not_visited(self,greedy_array,canvas):
        queue = []
        queue.append(greedy_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:
            queue.sort(key=lambda x: x[5])

            print(queue)

            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break

            num = len(queue)
            if queue[0][6] == self.__goal_row and queue[0][7] == self.__goal_col:
                status_loop = False
                new = queue.pop(0)
                self.__draw_path_canvas(canvas, new[8])
                print("reached goal")
                break
            list = queue.pop(0)
            self.__store_queue(list[6], list[7],list,greedy_array, queue)
            canvas.create_rectangle(list[1], list[2], list[3], list[4], fill="blue")
            canvas.after(20)
            canvas.update()

    def __greedy_expanded(self,greedy_array,canvas):
        expanded = []
        queue = []
        queue.append(greedy_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:
            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break;
            if queue[0][6] == self.__goal_row and queue[0][7] == self.__goal_col:
                status_loop = False
                new = queue.pop(0)
                self.__draw_path_canvas(canvas, new[8])
                print("reached goal")
                break
            list = queue.pop(0)
            expanded.append(list)
            expanded.sort(key=lambda x: x[5])
            self.__store_queue_expanded(list[6], list[7],list,greedy_array, queue,expanded)
            queue.sort(key=lambda x: x[5])
            canvas.create_rectangle(list[1], list[2], list[3], list[4], fill="blue")
            canvas.after(20)
            canvas.update()