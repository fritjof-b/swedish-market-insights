from datetime import date

from context import utils


def test_date_from_string_valid_input():
    d = "1992-12-13"
    assert utils.date_from_string(d) == date(1992, 12, 13)


def test_date_from_string_invalid_input():
    d = "1992-12-13-"
    try:
        utils.date_from_string(d)
        assert False, "Should raise ValueError"
    except ValueError:
        assert True


def test_volume_from_string_valid_input():
    assert utils.parse_volume_from_string("1 000") == 1000
    assert utils.parse_volume_from_string("1000") == 1000
    assert utils.parse_volume_from_string("100 000") == 100000
    assert utils.parse_volume_from_string("100,000,000") == 100000000


def test_price_from_string_valid_input():
    assert utils.parse_price_from_string("13,37") == 13.37
    assert utils.parse_price_from_string("0.93") == 0.93
    assert utils.parse_price_from_string("1,84184415") == 1.84184415


def test_price_from_string_should_not_round():
    assert utils.parse_price_from_string("13.37") != 13.4
