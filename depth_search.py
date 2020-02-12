class depth:
    __new_array = [[[0 for k in range(8)] for j in range(40)] for i in range(34)]

    def __init__(self, level, canvas,init_row,init_col,goal_row,goal_col, checkbox, radio):
        self.__set_drawn_canvas(canvas)
        self.__set_level(level)
        self.__init_row = init_row
        self.__init_col = init_col
        self.__goal_row = goal_row
        self.__goal_col = goal_col
        self.__new_breadth(self.__new_array, self.__get_level())

        if checkbox == 1 and radio == 1:
            self.__depth_visited(self.__new_array, self.__get_drawn_canvas())
        elif checkbox == 1 and radio == 2:
            self.__depth_not_visited(self.__new_array, self.__get_drawn_canvas())
        elif checkbox == 1 and radio == 3:
            self.__depth_expanded(self.__new_array, self.__get_drawn_canvas())
        else:
            self.__depth_not_visited(self.__new_array, self.__get_drawn_canvas())

    def __set_drawn_canvas(self, canvas):
        self.__drawn_canvas = canvas

    def __get_drawn_canvas(self):
        return self.__drawn_canvas

    def __set_level(self, level):
        self.__det_level = level

    def __get_level(self):
        return self.__det_level

    def __new_breadth(self, array, canvas_array):
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
                array[i][j][5] = i
                array[i][j][6] = j
                array[i][j][7] = []
                array[i][j][7].append(new)

    def contains(self, row, col, visited_array):
        for i in range(len(visited_array)):
            if row == visited_array[i][5] and col == visited_array[i][6]: return True;
        return False

    def __add_path(self, depth_array, list):
        for i in list[7]:
            depth_array[7].append(i)

    def __store_queue_expanded(self, i, j,list,depth_array, queue, expanded):
        if j - 1 >= 0 and depth_array[i][j - 1][0] == 0 and self.contains(i, j - 1, expanded) == False:
            self.__add_path(depth_array[i][j-1],list)
            queue.append(depth_array[i][j - 1])
            expanded.insert(0, depth_array[i][j - 1])
        if i - 1 >= 0 and depth_array[i - 1][j][0] == 0 and self.contains(i-1, j, expanded) == False:
            self.__add_path(depth_array[i-1][j],list)
            queue.append(depth_array[i - 1][j])
            expanded.insert(0, depth_array[i - 1][j])
        if j + 1 <= 39 and depth_array[i][j + 1][0] == 0 and self.contains(i, j + 1, expanded) == False:
            self.__add_path(depth_array[i][j+1],list)
            queue.append(depth_array[i][j + 1])
            expanded.insert(0,depth_array[i][j + 1])
        if i + 1 <= 33 and depth_array[i + 1][j][0] == 0 and self.contains(i + 1, j, expanded) == False:
            self.__add_path(depth_array[i+1][j],list)
            queue.append(depth_array[i + 1][j])
            expanded.insert(0, depth_array[i + 1][j])

    def __store_queue_visited(self, i, j,list,depth_array, queue, visited):
        if j - 1 >= 0 and depth_array[i][j - 1][0] == 0 and self.contains(i, j - 1, visited) == False:
            self.__add_path(depth_array[i][j-1],list)
            queue.append(depth_array[i][j - 1])
            visited.insert(0, depth_array[i][j - 1])
        if i - 1 >= 0 and depth_array[i - 1][j][0] == 0 and self.contains(i-1, j, visited) == False:
            self.__add_path(depth_array[i-1][j],list)
            queue.append(depth_array[i - 1][j])
            visited.insert(0, depth_array[i - 1][j])
        if j + 1 <= 39 and depth_array[i][j + 1][0] == 0 and self.contains(i, j+1, visited) == False:
            self.__add_path(depth_array[i][j+1],list)
            queue.append(depth_array[i][j + 1])
            visited.append(depth_array[i][j + 1])
        if i + 1 <= 33 and depth_array[i+1][j][0] == 0 and self.contains(i + 1, j, visited) == False:
            self.__add_path(depth_array[i+1][j],list)
            queue.append(depth_array[i + 1][j])
            visited.insert(0, depth_array[i + 1][j])


    def checkIfItcontains(self,main_list,to_search):
        if to_search not in main_list:
            return True

        return False

    def __store_queue(self, i, j, list,depth_array, queue):

        # and depth_array[i][j - 1][0] == 0
        if j - 1 >= 0:
            self.__add_path(depth_array[i][j-1],list)
            queue.append(depth_array[i][j - 1])

        # and depth_array[i - 1][j][0] == 0
        if i - 1 >= 0:
            self.__add_path(depth_array[i-1][j],list)
            queue.append(depth_array[i - 1][j])

        # and depth_array[i][j + 1][0] == 0
        if j + 1 <= 39:
            self.__add_path(depth_array[i][j+1],list)
            queue.append(depth_array[i][j + 1])

            # and depth_array[i + 1][j][0] == 0
        if i + 1 <= 33:
            self.__add_path(depth_array[i+1][j],list)
            queue.append(depth_array[i + 1][j])

        return queue

    def __draw_path_canvas(self, canvas, path):
        for i in range(len(path)):
            canvas.create_rectangle(path[i][0], path[i][1], path[i][2], path[i][3], fill="red")
            canvas.after(30)
            canvas.update()

    def __depth_visited(self, bread_array, canvas):
        visited = []
        visited.append(bread_array[self.__init_row][self.__init_col])
        queue = []
        queue.append(bread_array[self.__init_row][self.__init_col])

        status_loop = True

        while status_loop == True:
            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break
            if queue[-1][5] == self.__goal_row and queue[-1][6] == self.__goal_col:
                status_loop = False
                new = queue.pop()
                self.__draw_path_canvas(canvas, new[7])
                print("reached goal")
                break
            list = queue.pop()
            self.__store_queue_visited(list[5], list[6],list,bread_array, queue, visited)
            canvas.create_rectangle(list[1], list[2], list[3], list[4], fill="blue")
            canvas.after(20)
            canvas.update()

    def __depth_not_visited(self, bread_array, canvas):

        queue = []
        queue.append(bread_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:

            # if len(queue) == 0:
            #     print("Show a dialog message that nothing is achieved")
            #     break;


            if queue[-1][5] == self.__goal_row and queue[-1][6] == self.__goal_col:
                status_loop = False
                new = queue.pop()
                self.__draw_path_canvas(canvas, new[7])
                print("reached goal")
                break

            list = queue.pop()
            # print(list)


            # TODO -> check this function because the queue might be the problem
            queue = self.__store_queue(list[5], list[6],list,bread_array, queue)
            canvas.create_rectangle(list[1], list[2], list[3], list[4], fill="blue")

            print(queue)
            print('\n')
            canvas.after(20)
            canvas.update()


    def __depth_expanded(self, bread_array, canvas):
        expanded = []
        queue = []
        queue.append(bread_array[self.__init_row][self.__init_col])
        status_loop = True

        while status_loop == True:

            print(queue)

            if len(queue) == 0:
                print("Show a dialog message that nothing is achieved")
                break

            if queue[-1][5] == self.__goal_row and queue[-1][6] == self.__goal_col:
                status_loop = False
                new = queue.pop()
                self.__draw_path_canvas(canvas, new[7])
                print(new[7])
                print("reached goal")
                break


            list = queue.pop()
            expanded.append(list)
            self.__store_queue_expanded(list[5], list[6],list,bread_array, queue, expanded)
            canvas.create_rectangle(list[1], list[2], list[3], list[4], fill="blue")
            canvas.after(20)
            canvas.update()