from typing import List
from priost.input.finder import SourceCodeFinder
from _pytest.config import Config
from pytest import *


def pytest_collection_modifyitems(session: Session, config: Config, items: List[Item]):
    for tc in items:
        finder = SourceCodeFinder()
        code = finder.find_source_code(tc)
        print(code)





