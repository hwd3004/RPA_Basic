import pyautogui

# pyautogui.mouseInfo()

# False로 하면 종료 안됨
# pyautogui.failSafeCheck = False
# 반복문이 실행되는 동안, 마우스를 모니터의 구석 4곳 중 하나에 접근시키면 종료됨

# 모든 동작에 1초씩 sleep 적용
# pyautogui.PAUSE = 1

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)