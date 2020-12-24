from openpyxl import Workbook

# pipenv install pillow
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("img.jpg")

# C3 위치에 img.jpg 파일의 이미지 삽입
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")