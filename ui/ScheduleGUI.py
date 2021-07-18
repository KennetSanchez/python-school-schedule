import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QApplication


class ScheduleGUI(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.show_main_menu()
        self.initialize_menu()           
    
    # Initialize graphic items.
    def initialize_menu(self):
        self.MENU_add_a_teacher.clicked.connect(self.show_add_a_teacher)
        self.MENU_remove_a_teacher.clicked.connect(self.show_remove_a_teacher)
        self.MENU_edit_a_teacher.clicked.connect(self.show_edit_a_teacher)
        self.MENU_add_a_course.clicked.connect(self.show_add_a_course)
        self.MENU_remove_a_course.clicked.connect(self.show_remove_a_course)
        self.MENU_edit_a_course.clicked.connect(self.show_edit_a_course)
    
    # Windows code.
    def show_main_menu(self):
        uic.loadUi("ui/Menu.ui", self)
    
    def show_add_a_teacher(self):
        uic.loadUi("ui/AddATeacher.ui", self)
    
    def show_remove_a_teacher(self):
        uic.loadUi("ui/RemoveATeacher.ui", self)
        
    def show_edit_a_teacher(self):
        uic.loadUi("ui/EditATeacher.ui", self)        
                 
    def show_add_a_course(self):
        uic.loadUi("ui/AddACourse.ui", self)
    
    def show_remove_a_course(self):
        uic.loadUi("ui/RemoveACourse.ui", self)
        
    def show_edit_a_course(self):
        uic.loadUi("ui/EditACourse.ui", self)    
    
    def show_generate_schedules(self):
        uic.loadUi("ui/GenerateSchedules.ui", self)
        
    def show_schedules(self):
        uic.loadUi("ui/AllSchedules.ui", self)          
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ScheduleGUI()
    GUI.show()
    app.exec()