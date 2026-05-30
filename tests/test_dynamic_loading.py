from pages.dynamic_loading_page import DynamicLoadingPage as dpl

def test_finish_text(driver):
    page = dpl(driver)
    page.load().click_start()
    assert page.get_finish_text() == "Hello World!"
    


