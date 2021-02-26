import pytest


def pytest_addoption(parser):
    parser.addoption("--interactive", "--ia", action="store_true",
                     dest='interactive',
                     help="enable iteractive selection of tests after"
                     " collection")


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(session, config, items):
    """called after collection has been performed, may filter or re-order
    the items in-place.
    """
    if not (config.option.interactive and items):
        return
