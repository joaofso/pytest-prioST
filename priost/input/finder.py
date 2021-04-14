from pytest import Function
import os
from typing import List

class SourceCodeFinder:

    BDD_ENDING = "pytest_bdd/scenario.py"

    def find_source_code(self, test_case: Function):
        location_info = test_case.location
        module_path = location_info[0]
        test_method_name = location_info[2]
        root_dir = test_case.fspath.dirname


        if module_path.endswith(self.BDD_ENDING):
            # look for feature file
            return self._find_bdd_scenario(root_dir, test_method_name)
        else:
            # look for python code
            self._find_python_test()

    def _find_bdd_scenario(self, root: str, test_method_name: str) -> List[str]:
        scenario_name_tokens = test_method_name.split("_")[1:]
        for dirpath, subdirs, filenames in os.walk(root):
            for file in filenames:
                if file.endswith(".feature"):
                    full_path = os.path.join(dirpath, file)
                    with open(full_path, "r") as feature_file:
                        found_scenario = False
                        scenario_lines = []
                        for line in feature_file:
                            if all(token in line for token in ["Scenario"] + scenario_name_tokens) and not found_scenario:
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

    def _find_python_test(self):
        pass
