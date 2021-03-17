from pytest_bdd import scenarios, parsers, given

scenarios('feature')

def test_simple_testing():
    print("Done")

@given(parsers.parse("I run the command"))
def run_command():
    print("Command run")