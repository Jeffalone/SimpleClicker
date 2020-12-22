import pyautogui
import keyboard
import sys
import time
import win32api
import config


def auto_click():
    mouse_position = win32api.GetCursorPos()
    while True:
        curr_pos = win32api.GetCursorPos()
        if keyboard.is_pressed(config.PAUSE_KEY) or keyboard.is_pressed(config.QUIT_KEY):
            break
        elif curr_pos != mouse_position and config.autoStop:
            break
        else:
            pyautogui.click()


if __name__ == '__main__':
    while True:
        if keyboard.is_pressed(config.START_KEY) and config.inputEnable:
            auto_click()

        if keyboard.is_pressed(config.START_KEY) and keyboard.is_pressed(config.PAUSE_KEY):
            config.inputEnable = not config.inputEnable
            time.sleep(0.5)

        if keyboard.is_pressed(config.QUIT_KEY) and config.inputEnable:
            sys.exit("Program Exited by User.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
