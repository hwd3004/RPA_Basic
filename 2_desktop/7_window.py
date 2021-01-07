import pyautogui


def get_window():
    # 현재 활성화된 창 (vscode)
    fw = pyautogui.getActiveWindow()

    # 창의 제목 정보
    print(fw.title)

    # 창의 크기 정보
    print(fw.size)

    # 창의 좌표 정보
    print(fw.left, fw.top, fw.right, fw.bottom)

    pyautogui.click(fw.left + 10, fw.top + 20)


def get_all_window():
    # for w in pyautogui.getAllWindows():
    #     print(w)

    # for w in pyautogui.getWindowsWithTitle("제목 없음"):
    #     print(w)

    w = pyautogui.getWindowsWithTitle("제목 없음")[0]
    print(w)

    # 현재 활성화가 되지 않았다면
    if w.isActive == False:
        # 활성화 (맨앞으로 가져오기)
        w.activate()

    if w.isMaximized == False:
        # 최대화
        w.maximize()

    if w.isMinimized == False:
        # 최소화
        w.minizied()

    # 화면 원상복구
    w.restore()

    # 윈도우 닫기
    # w.close()


def init():
    # get_window()
    get_all_window()


init()
