import sys
import pyautogui
import time


def handle_file_menu():
    start = time.time()

    file_menu = pyautogui.locateOnScreen("file_menu.png")

    print(file_menu)

    # pyautogui.click(file_menu)

    print("handle_file_menu", time.time() - start)


def handle_all_image():
    # 같은 이미지 모든 것 가져오기
    temp_all = pyautogui.locateAllOnScreen()

    for i in temp_all:
        print(i)
        pyautogui.click(i)


def handle_grayscale():
    start = time.time()

    # 속도 개선, 이미지를 비교할 때 흑백으로 전환해서 비교
    # 정확도가 떨어짐
    file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)

    print(file_menu)

    print("handle_grayscale", time.time() - start)


def handle_guide_position():
    start = time.time()

    # 속도 개선, 위치 범위를 지정해줌
    file_menu = pyautogui.locateOnScreen(
        "file_menu.png", region=(25, 80, 386, 283))

    print(file_menu)

    print("handle_guide_position", time.time() - start)


def handle_accuracy():
    start = time.time()

    # 정확도 개선
    # pipenv install opencv-python
    # confidence = 0.9 가 기본
    file_menu = pyautogui.locateOnScreen("file_menu.png", confidence=0.9)

    print(file_menu)

    print("handle_accuracy", time.time() - start)


def handle_wait_target():
    # 자동화 대상이 바로 보여지지 않는 경우
    # 계속 기다리기
    temp = pyautogui.locateOnScreen("temp.png")

    while temp is None:
        temp = pyautogui.locateOnScreen("temp.png")
        print(temp)

    pyautogui.click(temp)


def handle_timeout_target():

    timeout = 10

    start = time.time()

    temp = None

    while temp is None:
        temp = pyautogui.locateOnScreen("temp.png")
        end = time.time()

        if end - start > timeout:
            print("시간 종료")
            sys.exit()

    print(temp)


def init():
    # pyautogui.mouseInfo()
    # handle_file_menu()
    # handle_grayscale()
    handle_guide_position()
    # handle_accuracy()
    # handle_wait_target()
    # handle_timeout_target()


init()
