from termcolor import colored
from calendar_icelandic.visualizer import Visualizer

class ColorPrinter(Visualizer):
    """
    Utility class to print colorized text to the terminal using the termcolor package.
    """

    @staticmethod
    def print(text: str, color: str = 'white') -> None:
        """
        Print text in the specified color.

        :param text: The text to be printed.
        :param color: Color to use for the text. Valid colors can be found in the termcolor documentation.
        """
        print(colored(text, color), end='')

    @staticmethod
    def println(text: str, color: str = 'white') -> None:
        """
        Print text in the specified color, followed by a newline.

        :param text: The text to be printed.
        :param color: Color to use for the text. Valid colors can be found in the termcolor documentation.
        """
        ColorPrinter.print(text, color)
        print()  # Move to next line
