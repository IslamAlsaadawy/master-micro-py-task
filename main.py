
import sys
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,  QLabel, QLineEdit,QPushButton,QMessageBox, QApplication
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np



# only allowing this operations to be done
allowed_ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "**": lambda a, b: a ** b
}
class Window(QWidget):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Function Plot")
        self.setMinimumSize(800,600)
        v_layout = QVBoxLayout()
        h_input_layout = QHBoxLayout()

        #Labels, inputs and buttons

        function_label = QLabel("Enter a function: ")
        self.function_text_input = QLineEdit()
        
        xmin_label = QLabel("Minimum x value: ")
        self.xmin_text_input = QLineEdit()

        xmax_label = QLabel("Maximum x value: ")
        self.xmax_text_input =  QLineEdit()

        plot_function_button = QPushButton("Plot")
        plot_function_button.clicked.connect(self.plot_function) # still to be implemented

        instructions_button = QPushButton("Instructions")
        instructions_button.clicked.connect(self.show_instructions)

        #Adding the widgets to the H box
        h_input_layout.addWidget(instructions_button)
        h_input_layout.addWidget(function_label)
        h_input_layout.addWidget(self.function_text_input)

        h_input_layout.addWidget(xmin_label)
        h_input_layout.addWidget(self.xmin_text_input)


        h_input_layout.addWidget(xmax_label)
        h_input_layout.addWidget(self.xmax_text_input)

        h_input_layout.addWidget(plot_function_button)

        #Add matplot figure,and canvas one that fits with QT and add it to v layout
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        v_layout.addWidget(self.canvas)

        #add the H layout to the v layout and set default to v
        v_layout.addLayout(h_input_layout)
        self.setLayout(v_layout)
    
    def error_box(self,message):
            error_box =  QMessageBox()
            error_box.setIcon(QMessageBox.Critical)
            error_box.setWindowTitle("Error")
            error_box.setText(f"Invalid input: {message}")
            error_box.setStandardButtons(QMessageBox.Ok)
            error_box.exec_()
            self.xmin_text_input.setText("")
            self.xmax_text_input.setText("")
            return
    
    def show_instructions(self):
        instructions = [
            "Welcome to the Function Plotter!\n\n. Made by Islam Ashraf",
            "Enter a mathematical function in the text box labeled 'Enter a mathematical function'.","The only allowed operations are +, -, /, *, ^. ",
            "Enter the minimum and maximum values of x in the text boxes labeled 'Minimum x value' and 'Maximum x value'.",
            "Click the 'Plot' button to plot the function.\n\nThe plot will appear in the window above the input boxes.",
            "If you enter an invalid input, an error message will appear.\n\nYou can then correct your input and try again.",
            "Enjoy using the Function Plotter!"
        ]
        
        for i, instruction in enumerate(instructions):
            message_box = QMessageBox()
            message_box.setWindowTitle("Instructions")
            message_box.setText(instruction)

            if i == len(instructions) - 1:
             message_box.setStandardButtons(QMessageBox.Ok)
            else:
                message_box.addButton("Next", QMessageBox.AcceptRole)
                message_box.setStandardButtons(QMessageBox.Cancel)
            ret = message_box.exec_()
            if ret == QMessageBox.Ok:
                break

            if ret == QMessageBox.Cancel:
                break
             

    def plot_function(self):
        functionn_input = self.function_text_input.text()
            # might need to change to text first check later!!
        functionn_input = functionn_input.replace("^", "**")
        #AS mentioned in the rquriment and i am trying to meet it that to raise to the power ^ should be used not ** will be switched during runtime


        try:
            xmin = float(self.xmin_text_input.text())
            xmax = float(self.xmax_text_input.text())
            x = np.linspace(xmin,xmax,100)
            if(xmin > xmax):
                self.error_box("Xmin is larger than Xmax")

            y = eval(functionn_input, allowed_ops, {'x': x})


        except Exception as err:
            self.error_box(err)
       
       
     #clear old figure for new one to exist
        self.figure.clear()
        plot = self.figure.add_subplot(111)
        try:
            plot.plot(x,y, color='blue')
            plot.set_title("Function Plot")
            plot.set_xlabel("X values")
            plot.set_ylabel("Y values")
            self.canvas.draw()
        except Exception as err:
             self.error_box(err)



if not QApplication.instance():
    app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())



