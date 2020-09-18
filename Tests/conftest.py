
import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
    driver.get('https://www.instructables.com/craft/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()




