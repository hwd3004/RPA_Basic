import pyperclip
import sys
import pyautogui


pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")
pyautogui.sleep(2)


window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]


def q02():

    if window.isMaximized == False:
        window.maximize()


def q03():
    btn_text = pyautogui.locateOnScreen("text.png")

    if btn_text:
        pyautogui.click(btn_text, duration=0.5)
    else:
        print("찾기 실패")
        sys.exit()


def q04(text):
    # 흰 영역 클릭

    # 한글 입력하기 위해서
    # import pyperclip

    pyautogui.click(200, 200, duration=0.5)

    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


def q05():
    pyautogui.sleep(5)

    window.close()
    pyautogui.sleep(0.5)
    pyautogui.press("n")


def init():
    q02()
    q03()
    q04("파이썬 업무자동화")
    q05()


init()
