import logging
from datetime import datetime


def get_log():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    # debug < info < warning < error < critical
    logging.debug("개발 단계")
    logging.info("자동화 수행 준비")
    logging.warning("경고")
    logging.error("에러 발생")
    logging.critical("복구가 불가능한 심각한 문제")


def get_log02():
    # 터미널과 파일에 함께 로그 남기기
    log_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s")
    logger = logging.getLogger()

    # 로그 레벨 설정
    logger.setLevel(logging.DEBUG)

    # 스트림
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)

    # 파일
    filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
    file_handler = logging.FileHandler(filename, encoding="utf-8")
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    logger.debug("로그를 남겨보는 테스트")


def init():
    # get_log()
    get_log02()


init()
