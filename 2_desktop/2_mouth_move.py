import pyautogui

# 마우스 이동

# 절대 좌표로 마우스를 이동
# pyautogui.moveTo(100, 100)

# 2초 동안 이동
# pyautogui.moveTo(100, 100, duration=2)

# 상대 좌표로 이동
# pyautogui.move(100, 100)

# 현재 마우스 좌표 확인
# print(pyautogui.position())
p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)