from typing import List
import inspect


from _pytest.config import Config
from pytest import *


def pytest_collection_modifyitems(session: Session, config: Config, items: List[Item]):
    for tc in items:
        print()





