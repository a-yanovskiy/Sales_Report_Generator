import sales_report_generator.report_generator as report
import pytest
from format_report import read_xlsx

REPORT1_PATH = "tests/fixtures/stocks_1.xlsx"
RESULT1_PATH = "tests/fixtures/result_1.txt"

REPORT2_PATH = "tests/fixtures/stocks_2.xlsx"
RESULT2_PATH = "tests/fixtures/result_2.txt"

DISH_ADD = 'Dish:'
LEADERS_ADD = 'Sales Leaders:'
GROWS_ADD = 'Growth:'
FALLS_ADD = 'Falls:'
DISH_DEL = 'Yammy'


@pytest.mark.parametrize("report_path, result_path", [
                        (REPORT1_PATH, RESULT1_PATH),
                        (REPORT2_PATH, RESULT2_PATH)])
def test_generate_report(report_path, result_path):
    file = read_xlsx(report_path)

    generated_report = report.generate_report(file,
                                              dish_add_text=DISH_ADD,
                                              leaders_add_text=LEADERS_ADD,
                                              grows_add_text=GROWS_ADD,
                                              falls_add_text=FALLS_ADD,
                                              dish_del_text=DISH_DEL)

    with open(result_path, 'r', encoding='utf-8') as f:
        result = f.read()

    assert generated_report == result
