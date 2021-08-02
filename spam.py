
import re
import pyautogui
import time
import pyperclip


def inputCode(num, line):
    if re.match('^LOL\w{10,11}', line):
        print(f"input {num + 1}: {line}")

        pyperclip.copy(line)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

        # Accpet code
        time.sleep(1)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")

        # Done
        time.sleep(1)
        pyautogui.press("tab")
        pyautogui.press("enter")

        # Re input
        time.sleep(1)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
    else:
        print(f"Skip {num + 1}: {line}")


breakpoint = {'found': False, 'num': 0}
print(breakpoint['found'])

def checkBreakpoint():
    for num, line in enumerate(f):
        if re.match('>', line):
          breakpoint['found'] = True
          breakpoint['num'] = num


print('Click to input code for begin!')

time.sleep(3)

f = open("data", encoding="utf8")

print('begin')

for num, line in enumerate(f):
  inputCode(num, line)

print('done')
