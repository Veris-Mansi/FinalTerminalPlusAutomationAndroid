import pytest


@pytest.mark.usefixtures("data","driver")
class TestComplete():

    @pytest.fixture(autouse=True)
    def classSetup(self,data,driver):
        self.driver=driver
        self.data=data
        self.walkin_details=data['walkin_details']
        self.member_details=data['member_details']
        self.invited_details=data['invited_details']

    def test_login(self):
            time.sleep(2)
            login(self.driver)
            assert True

    def test_fresh_user(self):
        try:
            user_action = TouchAction(self.driver)
            checkIn(self.driver)
            contact = setting_contact(self.driver)
            time.sleep(3)
            #self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[3]').click()
            p = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')))
            p.click()
            #list=self.driver.find_elements_by_xpath('	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
            #print(list.length)
            #list[1].click()
            time.sleep(2)
            FLEP_Screen(self.driver,self.walkin_details,contact)
            time.sleep(2)
            activity_complete(self.driver,self.walkin_details)
        except:
            print("Exception")
            assert False
