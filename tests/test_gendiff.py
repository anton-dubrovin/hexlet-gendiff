import pytest

from gendiff.file_parser.fabric import parse_file_data
from gendiff.gendiff import generate_diff

STYLISH = "stylish"
PLAIN = "plain"
JSON = "json"

FILE1_JSON = "tests/fixtures/file1.json"
FILE2_JSON = "tests/fixtures/file2.json"
FILE1_YML = "tests/fixtures/file1.yml"
FILE2_YML = "tests/fixtures/file2.yml"

FILE_RESULT_STYLISH = "tests/fixtures/result_stylish"
FILE_RESULT_PLAIN = "tests/fixtures/result_plain"
FILE_RESULT_JSON = "tests/fixtures/result_json"

extract_result = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {"doge": {"wow": "too much"}, "key": "value"},
    },
    "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
    "group2": {"abc": 12345, "deep": {"id": 45}},
    "group4": {
        "default": None,
        "foo": 0,
        "isNested": False,
        "nest": {"bar": "", "isNested": True},
        "type": "bas",
    },
}


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (parse_file_data(FILE1_JSON), extract_result),
        (parse_file_data(FILE1_YML), extract_result),
        (type(parse_file_data(FILE1_JSON)), dict),
        (type(parse_file_data(FILE1_YML)), dict),
    ],
)
def test_extract_data(input_data, expected):
    assert input_data == expected


with open(FILE_RESULT_STYLISH) as file_data:
    result_stylish = file_data.read()
with open(FILE_RESULT_PLAIN) as file_data:
    result_plain = file_data.read()
with open(FILE_RESULT_JSON) as file_data:
    result_json = file_data.read()


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (generate_diff(FILE1_JSON, FILE2_JSON, STYLISH), result_stylish),
        (generate_diff(FILE1_YML, FILE2_YML, STYLISH), result_stylish),
        (generate_diff(FILE1_JSON, FILE2_JSON, PLAIN), result_plain),
        (generate_diff(FILE1_YML, FILE2_YML, PLAIN), result_plain),
        (generate_diff(FILE1_JSON, FILE2_JSON, JSON), result_json),
        (generate_diff(FILE1_YML, FILE2_YML, JSON), result_json),
    ],
)
def test_generate_diff(input_data, expected):
    assert input_data == expected


# def test_output_format():
#     assert type(json_output(extract_result)) == str
#     assert type(plain_output(extract_result)) == str
#     assert type(stylish_output(extract_data)) == str
