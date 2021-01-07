import pyperclip
import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

w.activate()


def keyboard_write():
    pyautogui.write("12345")

    # 한글 안됨
    # 1초씩 적기
    pyautogui.write("asdfg", interval=1)


def keyboard_write02():
    pyautogui.write(["t", "e", "s", "t", "left",
                     "left", "right", "l", "a", "enter"], interval=1)


def keyboard_write03():
    # 특수문자, shift 4 -> $
    pyautogui.keyDown("shift")
    pyautogui.press("4")
    pyautogui.keyUp("shift")


def keyboard_write04():
    # press("a")
    pyautogui.keyUp("a")
    # ctrl + a
    pyautogui.keyUp("ctrl")


def keyboard_write05():
    # ctrl, alt, shift, a 순서로 눌렀다가, 역순으로 땜
    pyautogui.hotkey("ctrl", "alt", "shift", "a")


def keyboard_write06():
    # 한글 출력을 위해서 pyperclip 설치
    # "한글출력" 글자를 클립보드에 저장
    pyperclip.copy("한글출력")

    pyautogui.hotkey("ctrl", "v")

def init():
    # keyboard_write()
    # keyboard_write02()
    # keyboard_write03()
    # keyboard_write04()
    # keyboard_write05()
    keyboard_write06()


init()
