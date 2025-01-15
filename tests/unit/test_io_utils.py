"""
Test documentation for  assignment5.io_utilis.py
"""
import os
import pytest


from assignment5.io_utils import get_filehandle, is_gene_file_valid

# pylint: disable = C0116
# pylint: disable = C0103

FILE_TO_TEST = "test_file.txt"


def test_existing_get_filehandle_for_reading():
    # does it open a file for reading
    # create a test file
    _create_file_for_testing(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    # does it open a file for writing
    # test
    test = get_filehandle(FILE_TO_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_OSError():
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_ValueError():
    # does it raise Value Error
    # this should exit
    _create_file_for_testing(FILE_TO_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)


def _create_file_for_testing(file):
    # not actually run, they are just helper functions for the test script
    # create a test file
    open(file, "w").close()


def test_is_gene_file_valid():
    # Test case 1: File exists
    valid = "./assignment5/A1BG.unigene"
    assert is_gene_file_valid(valid) is True
    
