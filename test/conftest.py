from typing import List
from priost.input.finder import SourceCodeFinder
from _pytest.config import Config
from pytest import *
import logging

def set_logging():
    logger = logging.getLogger("priost")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def pytest_collection_modifyitems(session: Session, config: Config, items: List[Item]):
    logger = set_logging()
    for tc in items:
        logger.debug(f"Processing test case {tc.name}")
        finder = SourceCodeFinder()
        code = finder.find_source_code(tc)





