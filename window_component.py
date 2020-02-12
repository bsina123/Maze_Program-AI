from tkinter import *
from main_window import main_window
class window_component(main_window):

    def __init__(self):
        super().__init__()
        self.__set_parent(self.create_window())
        self.__set_canvas_width(self.get_width())
        self.__set_canvas_height(self.get_height())

    def __set_parent(self,window):
        self.__parent = window

    def get_parent(self):
        return self.__parent

    def __set_canvas_width(self,width):
        self.__canvas_width = width-400

    def __get_canvas_width(self):
        return self.__canvas_width

    def __set_canvas_height(self,height):
        self.__canvas_height = height-20

    def __get_canvas_height(self):
        return self.__canvas_height

    def create_canvas(self,parent):
        return Canvas(parent,width=self.__get_canvas_width(),height=self.__get_canvas_height(),bg="white")

    def cr_width_entry(self,parent,value):
        width_variable = IntVar()
        return Entry(parent,text=value)

    def cr_height_entry(self,parent,value):
        height_variable = IntVar()
        return Entry(parent,text=value)

    def cr_check_button(self,parent,text):
         self.v_check = IntVar()
         return Checkbutton(parent,text=text)

    def cre_radio_button(self,parent,text):
        return Radiobutton(parent,text=text)