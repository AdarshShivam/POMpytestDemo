import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.common.service import Service

@pytest.fixture(params=["chrome","edge"], scope='class')
def init_driver(request):
    chrome_path = Service(TestData.CHROME_EXECUTABLE_PATH)
    edge_path = Service(TestData.EDGE_EXECUTABLE_PATH)

    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=chrome_path)
    if request.param == "edge":
        web_driver = webdriver.Edge(service=edge_path)

    request.cls.driver = web_driver
    yield
    web_driver.close()