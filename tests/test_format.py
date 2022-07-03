import sales_report_generator.format as format
import pytest

INPUT_DICT_INT = {'a': '-10', 'b': '5', 'c': '-7', 'd': '45', 'e': '0'}
INPUT_DICT_FLOAT = {'a': '-10.0', 'b': '5.7', 'c': '-7.5', 'd': '45.0', 'e': '0.1'}
INPUT_DICT = {'Shop 10': 99, 'Shop 4 IE': 55, 'Shop 9': 45,'Shop 7 IE': 26,
              'Shop 5 IE': 6, 'Shop 8': 3}

RESULT_POSITIVE_DICT_FILTERED_INT = {'b': 5, 'd': 45, 'e': 0}
RESULT_NEGATIVE_DICT_FILTERED_INT = {'a': 10, 'c': 7}
RESULT_POSITIVE_DICT_FILTERED_FLOAT = {'b': 5.7, 'd': 45.0, 'e': 0.1}
RESULT_NEGATIVE_DICT_FILTERED_FLOAT = {'a': 10.0, 'c': 7.5}

RESULT_DICT_SORTED_INT = {'d': '45', 'b': '5', 'e': '0', 'c': '-7', 'a': '-10'}
RESULT_DICT_SORTED_FLOAT = {'d': '45.0', 'b': '5.7', 'e': '0.1', 'c': '-7.5',
                            'a': '-10.0'}
RESULT_FORMAT = 'Shop 10: 99 шт; Shop 4: 55 шт; Shop 9: 45 шт; Shop 7: 26 шт; ' \
                'Shop 5: 6 шт; Shop 8: 3 шт; '


@pytest.mark.parametrize("unfiltered_dict, filtered_result, filter_by", [
    (INPUT_DICT_INT, RESULT_POSITIVE_DICT_FILTERED_INT, 'positive'),
    (INPUT_DICT_INT, RESULT_NEGATIVE_DICT_FILTERED_INT, 'negative'),
    (INPUT_DICT_FLOAT, RESULT_POSITIVE_DICT_FILTERED_FLOAT, 'positive'),
    (INPUT_DICT_FLOAT, RESULT_NEGATIVE_DICT_FILTERED_FLOAT, 'negative'),
])
def test_filter_dict(unfiltered_dict, filtered_result, filter_by):
    filtered_dict = format.filter_dict(unfiltered_dict, filter_by)
    assert filtered_dict == filtered_result


@pytest.mark.parametrize("unsorted_dict, sorted_result", [
    (INPUT_DICT_INT, RESULT_DICT_SORTED_INT),
    (INPUT_DICT_FLOAT, RESULT_DICT_SORTED_FLOAT),
])
def test_sort_dict_by_float_values(unsorted_dict, sorted_result):
    sorted_dict = format.sort_dict_by_float_values(unsorted_dict)
    assert sorted_dict == sorted_result


@pytest.mark.parametrize("unformated_dict, formated_result, del_word", [
    (INPUT_DICT, RESULT_FORMAT, 'IE'),
])
def test_format_dict(unformated_dict, formated_result, del_word):
    formated_dict = format.format_dict(unformated_dict, del_word)
    assert formated_dict == formated_result
