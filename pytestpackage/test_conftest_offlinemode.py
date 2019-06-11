import pytest
import time
from utilities.Resources_small import *

@pytest.mark.usefixtures("data","driver")
class TestWalk_In():

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']
        self.offline_walkin_details=data['offline_walkin_details']

    def test_start_activity(self):
        try:
            start_activity(self.driver)
        except Exception as e:
            print(e)
            print("unable to start activity ")

    def test_login(self):
        try:
            login(self.driver)
        except Exception as e:
            print(e)

    def test_offlineMode(self):
        try:
            time.sleep(0.3)
            offline_mode(self.driver)
            time.sleep(0.5)
            checkIn(self.driver)
            contact = setting_offline_touch(self.driver)
            Next(self.driver)
            phone = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Employee')))
            phone.click()
            camera(self.driver)
            FLEP_Screen(self.driver, self.offline_walkin_details, contact)
            Meeting_with_offline_screen(self.driver)
            emergency_contact(self.driver, self.offline_walkin_details)
            unique_id(self.driver, self.offline_walkin_details['unique_id'])
            Next(self.driver)
            activity_complete(self.driver, self.offline_walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)

        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    def test_checkout_offline(self):
        try:

            check_out(self.driver,self.offline_walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)

        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise
    def test_autofetch_online(self):
        autofetch_user(self.driver,self.offline_walkin_details)

