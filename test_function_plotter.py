import sys
from PySide2.QtWidgets import QApplication
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
from main import Window



def test_plot_function(qtbot):
    window = Window()
    qtbot.addWidget(window)
    qtbot.keyClicks(window.function_text_input, "2*x")
    qtbot.keyClicks(window.xmin_text_input, "2")
    qtbot.keyClicks(window.xmax_text_input, "10")
    qtbot.mouseClick(window.plot_function_button, Qt.LeftButton)
    line = window.canvas.axes.lines[0]
    assert line.get_xdata()[0] == 2
    assert line.get_xdata()[-1] == 10
    assert line.get_ydata()[0] == 4
    assert line.get_ydata()[-1] == 20