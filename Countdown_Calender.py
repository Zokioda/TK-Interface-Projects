import tkinter as tk
import tkinter.ttk as ttk


class CountdownCalender:
    def __init__(self):
        self.__load_event_information__()
        self.__render_information__()

    def __load_event_information__(self):
        self.events = [
            ['Title1', 'Date1', 'Days to go 1', 'To do1'],
            ['Title2', 'Date2', 'Days to go 2', 'To do2'],
            ['Title3', 'Date3', 'Days to go 3', 'To do3'],
        ]

    def __render_information__(self):
        # Creating a window and setting its attributes

        self.window = tk.Tk()
        self.window.title('CountDown Calender')
        self.window.geometry('400x300')
        self.window.resizable(width=False, height=False)

        # Create widgets
        # Combobox
        cmb_event = ttk.Combobox

        # Add the widgets

        # Event Procedure

        self.window.mainloop()


def main():
    cc = CountdownCalender()


main()
