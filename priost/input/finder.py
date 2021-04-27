from pytest import Function
import os
from typing import List
import logging
import inspect
import importlib.util


class SourceCodeFinder:

    BDD_ENDING = "pytest_bdd/scenario.py"

    def __init__(self):
        self.logger = self.set_logging()

    @staticmethod
    def set_logging():
        logger = logging.getLogger("priost.SourceCodeFinder")
        return logger

    def find_source_code(self, test_case: Function):
        location_info = test_case.location
        module_path = location_info[0]
        test_method_name = location_info[2]
        root_dir = test_case.fspath.dirname
        if module_path.endswith(self.BDD_ENDING):
            # look for feature file
            self.logger.info(f"{test_case.name} is a BDD test case")
            return self._find_bdd_scenario(root_dir, test_method_name)
        else:
            # look for python code
            self.logger.info(f"{test_case.name} is a python test case")
            self._find_python_test(test_case.fspath.purebasename, test_case.fspath.strpath, test_method_name)

    def _find_bdd_scenario(self, root: str, test_method_name: str) -> List[str]:
        scenario_name_tokens = test_method_name.split("_")[1:]
        scenario_lines = []
        for dirpath, subdirs, filenames in os.walk(root):
            for file in filenames:
                if file.endswith(".feature"):
                    full_path = os.path.join(dirpath, file)
                    with open(full_path, "r") as feature_file:
                        found_scenario = False
                        for line in feature_file:
                            if all(token in line for token in ["Scenario"] + scenario_name_tokens) and not found_scenario:
                                self.logger.info(f"BDD scenario {test_method_name} found in {full_path}")
                                found_scenario = True
                                scenario_lines.append(line.strip())
                                continue
                            if found_scenario:
                                if "Scenario:" not in line:
                                    scenario_lines.append(line.strip())
                                else:
                                    break
                        if found_scenario:
                            return scenario_lines
        if not scenario_lines:
            self.logger.error(f"The source for {test_method_name} was not found")
            raise FileNotFoundError("")

    def _find_python_test(self, module_name: str, module_path: str, test_method_name: str):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        func = getattr(module, test_method_name)
        self.logger.info(f"The test method {test_method_name} from {module_name} was found in {module_path}")
        return inspect.getsource(func)
