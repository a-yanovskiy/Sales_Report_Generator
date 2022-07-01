import sales_report_generator.report_generator as report

REPORT1_PATH = "tests/fixtures/stocks_1.xlsx"
RESULT1_PATH = "tests/fixtures/result_1.txt"


def test_generate_report():
    file = report.read_xlsx(REPORT1_PATH)
    report_from_file = report.generate_report(file)

    with open(RESULT1_PATH, 'r', encoding='utf-8') as f:
        result = f.read()

    assert report_from_file == result
