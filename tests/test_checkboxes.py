import pytest
from pages.checkboxes_page import CheckboxesPage as cbp

def test_check_checkbox1(driver):
    page= cbp(driver)
    page.load()
    num = 1
    # assert initial state
    assert page.get_checkbox_status(num) == False
    # click
    page.click_checkbox(num)
    # assert changed state
    assert  page.get_checkbox_status(num) == True

def test_uncheck_checkbox2(driver):
    page= cbp(driver)
    page.load()
    num = 2
    # assert initial state
    assert page.get_checkbox_status(num) == True
    # click
    page.click_checkbox(num)
    # assert changed state
    assert page.get_checkbox_status(num) == False

def test_invalid_checkbox_number(driver):
    page = cbp(driver)
    page.load()
    with pytest.raises(ValueError) as exc_info:
        page.click_checkbox(5)
    assert "Checkbox 5 does not exist" in str(exc_info.value)