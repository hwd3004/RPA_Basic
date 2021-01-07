import pyautogui

# 3초 대기
pyautogui.sleep(3)
print(pyautogui.position())

# 1초동안 이 좌표로 이동 후, 마우스 클릭
# click()은 mouseDown()과 mouseUp()을 합친 메소드
# pyautogui.click(-1882, 226, duration=1)

# 더블 클릭
# pyautogui.doubleClick()

# 500번 클릭
# pyautogui.click(clicks=500)

# 마우스 우클릭
# pyautogui.rightClick()

# 마우스 휠버튼 클릭
# pyautogui.middleClick()

# 드래그
# pyautogui.drag(100, 100, duration=1)
# pyautogui.dragTo(1500, 500, duration=1)

# 양수이면 위 방향으로, 음수이면 아래 방향으로 숫자값만큼 스크롤
pyautogui.scroll(300)