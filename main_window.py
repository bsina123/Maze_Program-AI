from tkinter import *



class main_window:
    def __init__(self):
        self.__width = 1200
        self.__height = 700
        self.__title = "Maze Solver"

    def set_width(self,width):
        self.__width = width

    def set_height(self,height):
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def create_window(self):
        window = Tk()

        window["bg"]='#2BBBAD'

        window.attributes('-fullscreen',True)
        window.bind('<Escape>',lambda e:window.destroy())

        window.title(self.__title)
        window.wm_minsize(self.get_width(),self.get_height())
        return window