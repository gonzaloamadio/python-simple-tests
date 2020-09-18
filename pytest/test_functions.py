import pytest, mock, os

from functions import function1, function2

@pytest.fixture
def empty_folders(tmpdir_factory):
    out_folder = tmpdir_factory.mktemp("out")
    in_folder = tmpdir_factory.mktemp("in")
    reports_folder = tmpdir_factory.mktemp("reports")
    return in_folder, out_folder, reports_folder


@pytest.mark.skip(msg="This test will fail, as folders used in functions are not created")
def test_function_1(empty_folders):
    in_folder, out_folder, rep_folder = empty_folders
    in_folder = in_folder.strpath
    out_folder = out_folder.strpath
    rep_folder = rep_folder.strpath

    # Ass this folders are not parameters of the function, mock them.
    with mock.patch('functions.OUTPUT_FOLDER', out_folder):
            with mock.patch('functions.REPORTS_FOLDER', rep_folder):
                function1()

    # (Pdb) OUTPUT_FOLDER
    # '/tmp/pytest-of-gamadio/pytest-61/out0'
    # (Pdb) folder
    # 'out'

    # As wee see, deafult value is set at import time, so mock is not considered
    # https://stackoverflow.com/questions/24021491/python-unittest-mock-is-it-possible-to-mock-the-value-of-a-methods-default-arg


def test_function_1_2(empty_folders):
    in_folder, out_folder, rep_folder = empty_folders
    in_folder = in_folder.strpath
    out_folder = out_folder.strpath
    rep_folder = rep_folder.strpath

    # With this mock imported constant
    with mock.patch('functions.OUTPUT_FOLDER', out_folder):

        # With this, patch arguments default values
        # Python 2
        # function2.func_defaults = (out_folder, in_folder)
        # Python 3
        function2.__defaults__ = (out_folder, rep_folder)
        function1.__defaults__ = (out_folder,)

        function1()
