from logging import exception


from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    """
    Logic class for handling the main window's and operation

    Inherits from QMainWindow and Ui_MainWindow.
    """
    def __init__(self):
        """
        Creates the Logic class, sets up UI, and connects submit button.
        """
        super().__init__()
        self.setupUi(self)
        self.infoMessage.setStyleSheet("color: red")
        self.voteCounter()
        self.submitButton.clicked.connect(lambda : self.submit())

    def voteCounter(self):
        """
        Counts the votes for both 'Jane' and 'John' by reading from the 'vote.csv' file
        and updates the vote count on the app
        """
        self.janeVoteCount = 0
        self.johnVoteCount = 0
        with open('vote.csv', 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                candidateName = line.split()
                if candidateName[1] == 'Jane':
                    self.janeVoteCount += 1
                elif candidateName[1] == 'John':
                    self.johnVoteCount += 1

        self.janeCount.setText(str(self.janeVoteCount))
        self.johnCount.setText(str(self.johnVoteCount))

    def uncheckRadio(self):
        """
        Unchecks the radio buttons for both 'Jane' and 'John'.
        This method is to make sure people know that a new voter is needed
        """
        self.janeButton.setAutoExclusive(False)
        self.janeButton.setChecked(False)
        self.janeButton.setAutoExclusive(True)
        self.johnButton.setAutoExclusive(False)
        self.johnButton.setChecked(False)
        self.johnButton.setAutoExclusive(True)


    def submit(self):
        """
         Handles the submission of the vote. Validates the user input (ID and selected candidate)
         and writes to 'vote.csv' the id and the person they are voting for
         """
        try:
            name = self.idTextBox.text()
            personVoted = ''
            if len(name) != 8:
                raise TypeError
            name = int(name)
            name = str(name)
            exist = False

            if not self.janeButton.isChecked() and not self.johnButton.isChecked():
                raise Exception('Pick A Candidate')

            if self.johnButton.isChecked():
                personVoted = 'John'
            if self.janeButton.isChecked():
                personVoted = 'Jane'


            with open('vote.csv', 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    firstNum = line.split()
                    if name == firstNum[0]:
                        self.infoMessage.setText('Number already exist')
                        exist = True
                        break
                    exist = False


                if not exist:
                    with open('vote.csv', 'a') as file:
                        file.write(f'{name} {personVoted}\n')

            self.uncheckRadio()
            self.idTextBox.setText('')
            self.infoMessage.setText('')
            self.voteCounter()

        except ValueError:
            self.infoMessage.setText('Only Numbers Allowed')
        except TypeError:
            self.infoMessage.setText('Need 8 Numbers')
        except Exception as e:
            self.infoMessage.setText('Pick a candidate')




