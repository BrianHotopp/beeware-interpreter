"""
TFT Assistant
"""
import time
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import PIL
import uuid
import asyncio
import pygetwindow as gw
class TFTInterpreter(toga.App):

    def get_tft_window_loc(self) -> tuple:
        """
        Get the location of the TFT window.
        Args:
            self: the current gui object
        Returns:
            window rectangle in terms of left, top, right, bottom
        """
        leagueWindow = gw.getWindowsWithTitle('TFT Interpreter')[0]
        # get the window rectangle
        rect = leagueWindow.get_rect()
        return rect

    def get_tft_window_screenshot(self) -> PIL.Image.Image:
        """
        Get the screenshot of the TFT window.
        Args:
            self: the current gui object
        Returns:
            image object
        """
        im = PIL.ImageGrab.grab(self.get_tft_window_loc())
        return im


    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        recommendations_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        rec_text = toga.MultilineTextInput(readonly=True)
        # set the text box size
        rec_text.style.update(width=800, height=300)


        async def get_recommendations(widget, rec_text_box):
            r = "Recommendation: \n" + str(uuid.uuid4())
            for i in range(50):
                r += "\n" + str(uuid.uuid4())
            print('Got recommendation')
            # convert synchronous call to async
            r = await asyncio.to_thread(self.get_tft_window_loc)
            rec_text_box.value = r



        button = toga.Button(
            'Get Recommendations',
            on_press=get_recommendations,
            style=Pack(padding=5)
        )
        recommendations_box.add(rec_text)
        recommendations_box.add(button)
        main_box.add(recommendations_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return TFTInterpreter()
