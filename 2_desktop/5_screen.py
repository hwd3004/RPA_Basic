import pyautogui

# 스크린샷 찍기


def handle_screenshot():
    img = pyautogui.screenshot()

    # 파일로 저장, 듀얼모니터 사용중인데 1번 모니터만 저장됨
    img.save("screenshot.png")


def handle_pixel():
    # 385,97 37,37,37 #252525
    pixel = pyautogui.pixel(385, 97)
    print(pixel)

    temp = pyautogui.pixelMatchesColor(385, 97, (37, 22, 37))
    print(temp)

    return 0


def init():
    # handle_screenshot()
    # pyautogui.mouseInfo()
    handle_pixel()


init()
