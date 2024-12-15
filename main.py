from logic import *

def main():
    """
    Creates and runs PyQt6

    This function sets up the QApplication, creates a Logic window,
    and starts the event loop.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()