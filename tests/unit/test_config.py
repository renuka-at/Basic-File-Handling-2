"""
Test documentation for assignment5.config
"""
from assignment5.config import get_extension_for_unigene, get_directory_for_unigene, get_keyword_for_hosts,\
    get_error_string_4_PermissionError, get_error_string_4_TypeError, get_error_string_4_ValueError, \
    get_error_string_4_opening_file_OSError, get_error_string_4_opening_directory_OSError,\
    get_error_string_4_FileNotFoundError, MyOSError

_DIRECTORY_FOR_UNIGENE = "/Users/renuka.15/PycharmProjects/assignment5/venv/assignment5_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"
FILE_TO_TEST = "test_file.txt"
MODE = "r"


def test_get_directory_for_unigene():
    assert get_directory_for_unigene() == _DIRECTORY_FOR_UNIGENE


def test_get_extension_for_unigene():
    assert get_extension_for_unigene() == _FILE_ENDING_FOR_UNIGENE


def test_get_keyword_for_hosts():
    host_keywords = get_keyword_for_hosts()
    assert isinstance(host_keywords, dict)
    assert "bos taurus" in host_keywords
    assert "equus caballus" in host_keywords
    assert "homo sapiens" in host_keywords
    assert "mus musculus" in host_keywords
    assert "ovis aries" in host_keywords
    assert "rattus norvegicus" in host_keywords


def test_get_error_string_4_ValueError():
    assert get_error_string_4_ValueError() is None


def test_get_error_string_4_TypeError():
    assert get_error_string_4_TypeError() is None


def test_get_error_string_4_PermissionError():
    assert get_error_string_4_PermissionError(FILE_TO_TEST) is None


def test_get_error_string_4_FileNotFoundError():
    assert get_error_string_4_FileNotFoundError(FILE_TO_TEST) is None


def test_get_error_string_4_opening_file_OSError():
    assert get_error_string_4_opening_file_OSError(FILE_TO_TEST, MODE) is None


def test_get_error_string_4_opening_directory_OSError():
    directory = "test_directory"
    assert get_error_string_4_opening_directory_OSError(directory) is None


def test_MyOSError():
    err = "Test error"
    my_os_error = MyOSError(FILE_TO_TEST, MODE, err)
    assert isinstance(my_os_error, Exception)
    assert my_os_error.file == FILE_TO_TEST
    assert my_os_error.mode == MODE
    assert my_os_error.err == err
    assert str(my_os_error) == f"Error: {err}\nCould not open the fh_in': {FILE_TO_TEST} for type {MODE}"
