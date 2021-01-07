import shutil
import fnmatch
import os
import time
import datetime


def fs01():
    # cwd - current working directory, 현재 작업 공간
    print(os.getcwd())

    # 부모 폴더로 이동
    os.chdir("../")
    print(os.getcwd())

    # 조부모 폴더로 이동
    os.chdir("../../")
    print(os.getcwd())

    # 절대 경로로 이동
    os.chdir("c:/")
    print(os.getcwd())


def fs02():
    # 절대 경로 생성 후, 파일 만들기
    file_path = os.path.join(os.getcwd(), "my_file.txt")
    print(file_path)


def fs03():
    # 파일 경로에서 폴더 정보 가져오기
    # r는 문자를 그대로 읽음
    temp = os.path.dirname(
        r"D:\HWD\webprograming\Nomad\RPA_Basic\2_desktop\my_file.txt")
    print(temp)


def fs04():
    # 파일 정보 가져오기

    # 파일의 생성 날짜
    ctime = os.path.getctime("11_file_system.py")
    print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))


def fs05():
    # 파일의 수정 날짜
    mtime = os.path.getmtime("11_file_system.py")
    print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

    # 파일의 마지막 접근 날짜
    atime = os.path.getatime("11_file_system.py")
    print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))


def fs06():
    # 파일 크기

    # 바이트 단위로 파일 크기 가져오기
    size = os.path.getsize("11_file_system.py")
    print(size)


def fs07():
    # 파일 목록 가져오기
    # print(os.listdir())
    print(os.listdir("../"))


def fs08():
    # 하위 폴더 모두 포함 파일 목록 가져오기

    # result = os.walk("../")
    result = os.walk(".")
    # print(result)

    for root, dirs, files in result:
        print(root, dirs, files)


def fs09():
    # 폴더 내에서 특정 패턴을 가진 파일들을 찾기
    # import fnmatch

    pattern = "*.py"
    result = []

    for root, dirs, files in os.walk("."):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))

    print(result)


def fs10():
    # 주어진 경로가 파일인지 폴더인지 확인

    # 폴더여서 True
    print(os.path.isdir("../RPA_BASIC"))

    # 파일이 아니어서 False
    print(os.path.isfile("../RPA_BASIC"))

    # 주의 - 해당하는 파일이나 폴더가 없다면 False가 뜬다
    # 그래서 해당 파일이나 폴더가 존재하는지 확인해야한다

    if os.path.exists("../RPA_BASIC"):
        print("존재")
    else:
        print("존재 안함")


def fs11():
    # 파일 만들기

    # 빈 파일 생성
    open("new_file.txt", "a").close()


def fs12():
    # 파일 이름 변경
    os.rename("new_file.txt", "new_file_rename.txt")


def fs13():
    # 파일 삭제
    os.remove("new_file_rename.txt")


def fs14():
    # 폴더 만들기

    # 현재 경로 기준으로 폴더 생성
    os.mkdir("new_folder")

    # 절대 경로 기준으로 폴더 생성
    # os.mkdir("c:/new_folder")


def fs15():
    # 하위 폴더를 가지는 폴더 생성
    os.makedirs("new_folders/a/b/c")


def fs16():
    # 폴더 삭제

    # 폴더 안이 비었을때만 삭제 가능
    os.rmdir("new_folder")


def fs17():
    # import shutil
    # shutil - shell utilities

    # 폴더 안이 비어있지 않아도 삭제 가능
    # 모든 파일이 삭제되므로 주의
    shutil.rmtree("new_folders")

def fs18():
    # 파일 복사하기
    # 어떤 파일을 폴더 안으로 복사하기

    # shutil.copy(원본 경로, 대상 경로)
    # shutil.copy("log.txt", "../")

    # 원본 경로, 대상 경로/이름 변경
    shutil.copy("log.txt", "../log_copy.txt")

    # shutil.copyfile(원본 경로, 대상 경로/이름)

    # shutil.copy2(원번 경로, 대상 경로/폴더)
    # copy, copyfile : 메타 정보 복사  안함
    # copy2 : 메타 정보 복사함
    # 4:45:56 참고

def fs19():
    # 폴더 복사

    # 원본 경로, 대상 경로
    shutil.copytree("test_folder", "test_folder2")

def fs20():
    # 폴더 이동
    
    shutil.move("test_folder", "test_folder3")
    # 대상 폴더가 없다면, 원본 폴더 이름 변경

def init():
    fs18()


init()
