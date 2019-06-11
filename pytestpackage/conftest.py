import pytest

from utilities.Resources_small import *
@pytest.fixture(scope='module')
def data():
    start_server()
    data = settingup()
    yield data
@pytest.fixture(scope='module')
def driver(data):
    time.sleep(0.5)
    driver = launch_application(data['desired_capabilities'])
    #lists=[]
    #lists.append(driver)
    #lists.append(data)
    return driver
    """print("teardown")
    driver.close_app()
    driver.remove_app('com.veristerminal')
    driver.quit()"""
"""
@pytest.fixture()
def status_test(driver):

    print("running before each method")
    status_test =False
    print(status_test)
    yield status_test
    if (status_test == False):
        print("test case failed")
        a = WebDriverWait(driver, 5, poll_frequency=0.05).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'cancelButton')))
        s = a.is_diasplayed()
        if (s == True):
            a.click()
        time.sleep(1)
    else:
        print("test case passed")
"""
"""
@pytest.fixture
def driver(lists):
    driver=lists[0]
    return driver
"""

