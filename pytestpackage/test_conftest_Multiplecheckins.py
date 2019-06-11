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

    def test_login(self):
        time.sleep(3)
        time.sleep(0.5)
        permission_buttons_small_device(self.driver)
        time.sleep(1.5)
        self.driver.press_keycode(4)
        time.sleep(0.5)
        self.driver.start_activity("com.veristerminal", ".MainActivity")
        time.sleep(1)

        q=WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH,'//android.view.ViewGroup[@content-desc="domainPicker"]/android.widget.Spinner')))
        q.click()

        r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')))
        r.click()
        p = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization ID')))
        p.send_keys('N1')
        self.driver.hide_keyboard()
        p = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization Code')))
        p.send_keys('1')

        self.driver.hide_keyboard()
        r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'LOGIN')))
        r.click()

        for i in range(2):
            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Check-In')))
            m.click()
            print(type(self.member_details))
            print(self.member_details)
            setting_contact_touch(self.driver)

            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'NDA_ONLY')))
            m.click()
            cameraretake(self.driver)

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Confirm Check-in')))
            r.click()
            self.driver.background_app(2)
        for i in range(2):
            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Check-In')))
            m.click()

            setting_contact_member(self.driver)

            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'NDA_ONLYtwo')))
            m.click()
            cameraretake(self.driver)

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Confirm Check-in')))
            r.click()
            print("executed " + str(i))
            self.driver.close_app()
            time.sleep(0.5)
            self.driver.activate_app('com.veristerminal')
            print(self.member_details)
            print(type(self.member_details))

        for i in range(1):
            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Check-In')))
            m.click()

            setting_contact(self.driver)

            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'NDA_ONLY')))
            m.click()
            cameraretake(self.driver)

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Confirm Check-in')))
            r.click()
            print("executed "+str(i))

        for i in range(2):
            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Check-In')))
            m.click()

            setting_contact_member(self.driver)

            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'NDA_ONLYtwo')))
            m.click()
            cameraretake(self.driver)

            r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Confirm Check-in')))
            r.click()
            print("executed " + str(i))

