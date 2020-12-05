import os
import platform
from datetime import datetime as dt
import pyfiglet
from color import color, COLOR_RESET


class Console:
    def __init__(self, app_name, log_file_name):
        logo_font = 'larry3d'
        custom_fig = pyfiglet.Figlet(font=logo_font, width=1000)
        self.logo = custom_fig.renderText(app_name)[:-1]  # [:-1] to remove trailing enter

        self._log = []
        self.log_display_length = 15
        self.log_file_name = log_file_name
        self.pin = ""

        if not self.log_file_name.endswith('.log'):
            self.log_file_name += ".log"

    def __save_log_entry(self, log_entry):
        with open(self.log_file_name, 'a') as f:
            f.write(log_entry + "\n")

    def clear_screen(self):
        command = "clear" if platform.system() != "Windows" else "cls"
        os.system(command)

    def __get_time_stamp(self):
        return f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]"

    def __get_pin(self):
        if type(self.pin) == str:
            return self.pin
        else:
            return self.pin()

    def __output(self):
        self.clear_screen()

        # logo
        print(f"{color(fg='red')}{self.logo}{COLOR_RESET}", end="")

        # pinned data
        print(self.__get_pin())

        # log
        print("> === [ LOG ] ===")
        for log_entry in self._log:
            print(log_entry)

    def log(self, text):
        log_entry = f"{self.__get_time_stamp()} {text}"
        self._log.append(log_entry)
        self.__save_log_entry(log_entry)
        self.__output()


if __name__ == "__main__":
    console = Console('Coding Traders', 'test_log')
    console.log("test")
