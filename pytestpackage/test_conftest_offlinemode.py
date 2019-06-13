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

    def test_offline_mode(self):

        time.sleep(0.3)
        offline_mode(self.driver)

    def test_offlineMode_walkin(self):
        try:
            time.sleep(0.5)
            checkIn(self.driver)
            contact = setting_offline_touch(self.driver)

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

    def test_autofetch_offline(self):
        try:

            checkIn(self.driver)
            time.sleep(0.5)
            # setting_contact_member(self.driver)
            contact= setting_offline_touch(self.driver)
            phone = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Employee')))
            phone.click()

            cameraretake(self.driver)
            print(type(self.offline_walkin_details))
            print(self.offline_walkin_details)
            #FLEP_auto_fetch_member(self.driver, self.offline_walkin_details)
            FLEP_auto_fetch_visitor(self.driver,self.offline_walkin_details,contact)
            Meeting_with_offline_screen(self.driver)
            time.sleep(1)
            try:
                emergency_details_autofetch(self.driver, self.offline_walkin_details)
                unique_id_autofetch(self.driver, self.offline_walkin_details['unique_id'])

            except:
                emergency_contact(self.driver, self.offline_walkin_details)
                unique_id(self.driver, self.offline_walkin_details)

            Next(self.driver)
            time.sleep(1)
            activity_complete(self.driver, self.offline_walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.offline_walkin_details)

        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    def test_generalActivity_offline(self):
        general_activiity_walkin(self.driver,self.offline_walkin_details)


    def test_generalActivity_autofetch(self):
        self.driver.hide_keyboard()
        general_activity_autofetch(self.driver,self.offline_walkin_details)


    def test_checkout_offline(self):
        try:

            check_out(self.driver,self.offline_walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
            online_mode(self.driver)
        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    def test_logout(self):
        try:
            logout(self.driver)
            self.status_test = True
            statusOftest(self.status_test, self.driver)

        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise



