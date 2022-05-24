# Word Guess
# Copyright (C) 2022 Michael Rutherford
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import random
import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QFont


class PlotWindow(QWidget):
    """
    Class to display statistics window
    """

    def __init__(self):
        super(PlotWindow, self).__init__()
        self.create_scores()
        self.create_plot()

    def create_scores(self):
        """
        Read scores from a file and store them in a list
        """

        self.score_list = []
        with open("data/scores.txt", "r+") as f:
            self.score_list = f.read().splitlines()
        for i in range(0, len(self.score_list)):
            self.score_list[i] = int(self.score_list[i])

    def create_plot(self):
        """
        Defines the PyQtGraph plot and populates it with data
        """

        self.plot_layout = QHBoxLayout()
        self.setLayout(self.plot_layout)

        pg.setConfigOption("background", "#ffffff")
        pg.setConfigOption("foreground", "#000000")

        self.bargraph_plot = pg.plot()
        self.setWindowTitle("Statistics")
        self.bargraph_plot.setMouseEnabled(x=False, y=False)
        self.bargraph_plot.getAxis("bottom").setTickSpacing(1, 1)
        self.bargraph_plot.getViewBox().invertY(True)
        self.bargraph_plot.setYRange(1, 6, padding=0.1)
        if not self.score_list:
            self.bargraph_plot.setXRange(1, 5, padding=0.1)
        self.bargraph_plot.setLabels(
            title="Score Distribution", left="Score", bottom="Frequency"
        )
        self.bargraph_plot.hideButtons()

        self.x = [
            self.score_list.count(1),
            self.score_list.count(2),
            self.score_list.count(3),
            self.score_list.count(4),
            self.score_list.count(5),
            self.score_list.count(6),
        ]
        self.y = [1, 2, 3, 4, 5, 6]

        bargraph = pg.BarGraphItem(
            x0=0, y=self.y, height=0.6, width=self.x, brush="grey"
        )
        bargraph.setOpts()
        self.bargraph_plot.addItem(bargraph)

        clear_button = QPushButton("Clear scores", self)
        clear_button.clicked.connect(self.clear_scores)

        self.plot_layout.addWidget(
            self.bargraph_plot, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.plot_layout.addWidget(
            clear_button, alignment=QtCore.Qt.AlignmentFlag.AlignBottom
        )

    def clear_scores(self):
        """
        Clear the scores from the score file and reset_values bar graph window
        """

        open("data/scores.txt", "w").close()
        self.x = []
        self.bargraph_plot.setXRange(1, 5, padding=0.1)
        self.bargraph_plot.plot(self.x, self.y, clear=True)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.create_header()
        self.create_labels()
        self.create_guesses()
        self.create_content()
        self.create_input()
        self.create_main()

        self.reset_values()

    def create_header(self):
        """
        Defines the header widgets and packs them into the header layout
        """

        self.header_box = QGroupBox()
        self.header_layout = QHBoxLayout()
        self.header_box.setLayout(self.header_layout)
        self.header_box.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        self.info_button = QPushButton("ℹ️", self)
        self.info_button.clicked.connect(self.show_info)
        self.info_button.setFixedWidth(45)
        self.info_button.setFixedHeight(45)

        header_title = QLabel(self)
        header_title.setText("Word Guess")
        header_title.setFont(QFont("Arial", 24))
        header_title.setStyleSheet("color: black")
        header_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        stats_button = QPushButton("📊", self)
        stats_button.clicked.connect(self.show_plot)
        stats_button.setFixedWidth(45)
        stats_button.setFixedHeight(45)

        self.header_layout.addWidget(
            self.info_button, alignment=QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.header_layout.addWidget(
            header_title, 1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        self.header_layout.addWidget(
            stats_button, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )

    def create_labels(self):
        """
        Defines the label widgets and packs them into the label layout
        """

        self.label_box = QGroupBox()
        self.label_layout = QVBoxLayout()
        self.label_box.setLayout(self.label_layout)

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)

        self.label1.setText("1/6")
        self.label2.setText("2/6")
        self.label3.setText("3/6")
        self.label4.setText("4/6")
        self.label5.setText("5/6")
        self.label6.setText("6/6")

        self.label1.setFont(QFont("Arial", 24))
        self.label2.setFont(QFont("Arial", 24))
        self.label3.setFont(QFont("Arial", 24))
        self.label4.setFont(QFont("Arial", 24))
        self.label5.setFont(QFont("Arial", 24))
        self.label6.setFont(QFont("Arial", 24))

        self.label1.setFixedHeight(50)
        self.label2.setFixedHeight(50)
        self.label3.setFixedHeight(50)
        self.label4.setFixedHeight(50)
        self.label5.setFixedHeight(50)
        self.label6.setFixedHeight(50)

        self.label1.setStyleSheet("color: grey")
        self.label2.setStyleSheet("color: grey")
        self.label3.setStyleSheet("color: grey")
        self.label4.setStyleSheet("color: grey")
        self.label5.setStyleSheet("color: grey")
        self.label6.setStyleSheet("color: grey")

        self.label_layout.addWidget(
            self.label1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        self.label_layout.addWidget(
            self.label2, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.label_layout.addWidget(
            self.label3, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.label_layout.addWidget(
            self.label4, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.label_layout.addWidget(
            self.label5, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.label_layout.addWidget(
            self.label6, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )

    def create_guesses(self):
        """
        Defines the guess label widgets and packs them into the guess layout
        """

        self.guess_box = QGroupBox()
        guess_layout = QVBoxLayout()
        self.guess_box.setLayout(guess_layout)

        self.guess1 = QLabel(self)
        self.guess2 = QLabel(self)
        self.guess3 = QLabel(self)
        self.guess4 = QLabel(self)
        self.guess5 = QLabel(self)
        self.guess6 = QLabel(self)

        self.guess1.setFont(QFont("Courier", 24))
        self.guess2.setFont(QFont("Courier", 24))
        self.guess3.setFont(QFont("Courier", 24))
        self.guess4.setFont(QFont("Courier", 24))
        self.guess5.setFont(QFont("Courier", 24))
        self.guess6.setFont(QFont("Courier", 24))

        self.guess1.setFixedHeight(50)
        self.guess2.setFixedHeight(50)
        self.guess3.setFixedHeight(50)
        self.guess4.setFixedHeight(50)
        self.guess5.setFixedHeight(50)
        self.guess6.setFixedHeight(50)

        self.guess1.setFixedWidth(200)
        self.guess2.setFixedWidth(200)
        self.guess3.setFixedWidth(200)
        self.guess4.setFixedWidth(200)
        self.guess5.setFixedWidth(200)
        self.guess6.setFixedWidth(200)

        self.guess1.setStyleSheet("background-color: lightgrey")
        self.guess2.setStyleSheet("background-color: lightgrey")
        self.guess3.setStyleSheet("background-color: lightgrey")
        self.guess4.setStyleSheet("background-color: lightgrey")
        self.guess5.setStyleSheet("background-color: lightgrey")
        self.guess6.setStyleSheet("background-color: lightgrey")

        self.guess1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.guess2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.guess3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.guess4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.guess5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.guess6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        guess_layout.addWidget(
            self.guess1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        guess_layout.addWidget(
            self.guess2, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        guess_layout.addWidget(
            self.guess3, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        guess_layout.addWidget(
            self.guess4, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        guess_layout.addWidget(
            self.guess5, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        guess_layout.addWidget(
            self.guess6, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )

    def create_content(self):
        """
        Defines the layout to pack and combine the label and guess boxes
        """

        self.content_box = QGroupBox()
        self.content_layout = QHBoxLayout()
        self.content_box.setLayout(self.content_layout)
        self.label_box.setStyleSheet("background-color: transparent; border: None")
        self.guess_box.setStyleSheet("background-color: transparent; border: None")

        self.content_layout.addWidget(
            self.label_box, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )
        self.content_layout.addWidget(
            self.guess_box, alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )

    def create_input(self):
        """
        Defines the input widgets and packs them into the input layout
        """

        self.user_input_box = QGroupBox()
        self.input_layout = QHBoxLayout()
        self.user_input_box.setLayout(self.input_layout)

        self.input_box = QLineEdit(self)
        self.input_box.setFont(QFont("Courier", 24))
        self.input_box.setMinimumWidth(200)
        self.input_box.returnPressed.connect(self.submit_guess)

        guess_button = QPushButton("Guess", self)
        guess_button.clicked.connect(self.submit_guess)
        guess_button.setStyleSheet("font-size: 12pt")
        guess_button.setMinimumWidth(75)
        guess_button.setMinimumHeight(45)

        self.input_layout.addWidget(
            self.input_box, alignment=QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.input_layout.addWidget(
            guess_button, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )

    def create_main(self):
        """
        Defines the main window and packs the header, content, and input boxes inside
        """

        self.win = QWidget()
        self.setWindowTitle("Word Guess")
        self.main_layout = QVBoxLayout()
        self.win.setLayout(self.main_layout)
        self.setCentralWidget(self.win)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(
            self.header_box, alignment=QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.main_layout.addWidget(
            self.content_box,
            alignment=QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignBottom,
        )
        self.main_layout.addWidget(
            self.user_input_box,
            alignment=QtCore.Qt.AlignmentFlag.AlignCenter
            | QtCore.Qt.AlignmentFlag.AlignBottom,
        )

    def reset_values(self):
        """
        Defines and sets all program values to a default value
        """

        self.guess = ""
        self.answer = ""
        self.revealed_answer = ""
        self.guess_count = 0

        word_list = []
        with open("data/words.txt", "r") as f:
            word_list = f.read().splitlines()

        self.answer = random.choice(word_list)

        self.guess1.setText("     ")
        self.guess2.setText("     ")
        self.guess3.setText("     ")
        self.guess4.setText("     ")
        self.guess5.setText("     ")
        self.guess6.setText("     ")
        self.input_box.setText("")

    def submit_guess(self):
        """
        Processes user input and handles when the game ends
        """

        self.guess = self.input_box.text().lower()
        self.input_box.clear()
        self.revealed_answer = ["", "", "", "", ""]
        self.answer_dict = {}

        if self.error_check() == True:
            return

        # Create a dictionary of letter frequency in the answer
        for i in self.answer:
            if i in self.answer_dict:
                self.answer_dict[i] += 1
            else:
                self.answer_dict[i] = 1

        self.set_color()

        if self.guess_count == 0:
            self.guess1.setText("".join(self.revealed_answer))
            self.guess_count = self.guess_count + 1
        elif self.guess_count == 1:
            self.guess2.setText("".join(self.revealed_answer))
            self.guess_count = self.guess_count + 1
        elif self.guess_count == 2:
            self.guess3.setText("".join(self.revealed_answer))
            self.guess_count = self.guess_count + 1
        elif self.guess_count == 3:
            self.guess4.setText("".join(self.revealed_answer))
            self.guess_count = self.guess_count + 1
        elif self.guess_count == 4:
            self.guess5.setText("".join(self.revealed_answer))
            self.guess_count = self.guess_count + 1
        elif self.guess_count == 5 and self.guess != self.answer:
            self.guess6.setText("".join(self.revealed_answer))
            self.show_game_over(False)

        if self.guess == self.answer:
            with open("data/scores.txt", "a+") as f:
                f.write(str(self.guess_count) + "\n")
            self.show_game_over(True)

    def error_check(self):
        """
        Returns a boolean representing if there is an error with the user input
        """

        if len(self.guess) != 5:
            error_window = QMessageBox(self)
            error_window.setWindowTitle("Error")
            error_window.setText("Guesses must be exactly 5 letters long.")
            error_window.show()
            return True

        if self.guess.isalpha() != True:
            error_window = QMessageBox(self)
            error_window.setWindowTitle("Error")
            error_window.setText("Guesses must contain only letters.")
            error_window.show()
            return True

        return False

    def set_color(self):
        """
        Iterates through the user input and sets the color for each letter
        """

        # Iterate through guess to determine green letters
        for i in range(0, len(self.guess)):
            if self.guess[i] == self.answer[i]:
                self.revealed_answer[i] = (
                    '<span style=" color: #ffffff; background-color:#008800;" >'
                    + self.guess[i]
                    + "</span>"
                )
                self.answer_dict[self.guess[i]] -= 1

        # Iterate through guess to determine yellow letters
        for i in range(0, len(self.guess)):
            if (
                self.revealed_answer[i] != ""
                or self.guess[i] not in self.answer
                or self.answer_dict[self.guess[i]] == 0
            ):
                continue

            self.revealed_answer[i] = (
                '<span style=" color: #ffffff; background-color:#aaaa00;" >'
                + self.guess[i]
                + "</span>"
            )
            self.answer_dict[self.guess[i]] -= 1

        # Iterate through guess to determine grey letters
        for i in range(0, len(self.guess)):
            if self.revealed_answer[i] != "":
                continue
            self.revealed_answer[i] = (
                '<span style=" color: #ffffff; background-color:#555555;" >'
                + self.guess[i]
                + "</span>"
            )

    def show_info(self):
        """
        Creates a pop-up window with program information
        """

        info_window = QMessageBox(self)
        info_window.setWindowTitle("Info")
        info_window.setText(
            "Word Guess is a Python implementation of Wordle.\n\nBy: Michael Rutherford\n\nCopyright 2022"
        )
        info_window.show()

    def show_plot(self):
        """
        Creates an instance of the plot window and displays it
        """

        self.new_window = PlotWindow()
        self.new_window.show()

    def show_game_over(self, status):
        """
        Displays a window with the game result and a prompt to play again
        """

        game_over_window = QMessageBox(self)
        game_over_window.setWindowTitle("Game Over")

        if status == True:
            game_over_window.setText(
                "Correct! " + str(self.guess_count) + "/6\nPlay again?"
            )
        else:
            game_over_window.setText(
                "Correct answer: " + str(self.answer) + "\nPlay again?"
            )
        game_over_window.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        game_over_window.show()

        reply = game_over_window.exec()
        if reply == QMessageBox.StandardButton.Yes:
            self.reset_values()
        elif reply == QMessageBox.StandardButton.No:
            exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
