"""
If pytest will not find fixtures in class itself then it will check for the conf_test file
"""

import pytest


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
        time.sleep(2)
        login(self.driver)
        assert True

    def test_fresh_user(self):
       walkin_visitor(self.driver, self.walkin_details)
    """
    def test_autofetch_user_(self):
        autofetch_user(self.driver, self.walkin_details)

    def test_member_check_in(self):

        try:
            user_action = TouchAction(self.driver)
            checkIn(self.driver)
            time.sleep(0.5)
            setting_contact_member(self.driver)

            cameraretake(self.driver)
            FLEP_auto_fetch_member(self.driver, self.member_details)
            Meeting_with_screen(self.driver)
            time.sleep(1)
            emergency_details_autofetch(self.driver, self.member_details)
            unique_id_autofetch(self.driver, self.member_details['unique_id'])
            self.driver.find_element_by_accessibility_id('nextButton').click()

            time.sleep(1)
            activity_complete(self.driver, self.member_details)
            check_out(self.driver, self.member_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    def test_invited_user(self):
       try:
           self.status_test = False
           checkIn(self.driver)
           setting_contact_invite(self.driver)
           visitor = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
               EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Invited")))

           if (visitor.is_displayed()):
               assert True
               visitor.click()
           else:
               assert False
           FLEP_auto_fetch_member(self.driver, self.invited_details)
           # time.sleep(2)
           meeting = self.driver.find_element_by_xpath(
               '	//android.widget.EditText[@content-desc="meetingWithTextField"]')
           text = meeting.text
           if (len(text) > 0 and text == 'Mansi Sahu'):
               print("Meeting with test case passed")
               assert True
           else:
               print("Meeting with test case failed")
               assert False

           self.driver.find_element_by_accessibility_id('nextButton').click()
           time.sleep(2)
           activity_complete(self.driver, self.invited_details)
           check_out(self.driver, self.invited_details)
           self.status_test = True
           statusOftest(self.status_test, self.driver)
       except:
           self.status_test = False
           takeScreenshot(self.driver)
           statusOftest(self.status_test, self.driver)
           raise

    def test_general_activity_member(self):

       try:
           el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
           el.click()
           # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView').click()
           #time.sleep(0.05)
           setting_contact_member(self.driver)
           # time.sleep(2)
           cameraretake(self.driver)
           FLEP_auto_fetch_member(self.driver, self.member_details)
           time.sleep(0.5)
           emergency_details_autofetch(self.driver, self.member_details)
           time.sleep(0.5)
           el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                       '//android.view.ViewGroup[@content-desc="dropdownFormComponentField"]/android.view.ViewGroup')))
           el.click()
           el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]')))
           el.click()
           time.sleep(0.5)
           self.driver.find_element_by_accessibility_id('nextButton').click()
           unique_id_autofetch(self.driver, self.member_details['unique_id'])
           gender_Screen(self.driver)
           time.sleep(1)
           el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                         '//android.view.ViewGroup[@content-desc="dropdownFormComponentField"]/android.view.ViewGroup')))
           el.click()
           time.sleep(1)
           el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]')))
           el.click()
           next = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
               EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nextButton')))
           next.click()

           # time.sleep(3)

           # time.sleep(2)
           activity_complete(self.driver, self.member_details)
           check_out(self.driver, self.member_details)
           self.status_test = True
           statusOftest(self.status_test, self.driver)
           assert True
       except :
            print("exception")
            takeScreenshot(self.driver)
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_walkin(self):

        try:
            useraction = TouchAction(self.driver)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
            el.click()
            time.sleep(0.5)
            contact = setting_contact(self.driver)
            time.sleep(1)
            camera(self.driver)
            FLEP_Screen(self.driver, self.walkin_details, contact)
            time.sleep(1)
            emergency_contact(self.driver, self.walkin_details)
            time.sleep(0.5)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '//android.view.ViewGroup[@content-desc="dropdownFormComponentField"]/android.view.ViewGroup')))
            el.click()
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]')))
            el.click()
            time.sleep(0.5)
            self.driver.find_element_by_accessibility_id('nextButton').click()
            unique_id(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            self.driver.hide_keyboard()
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '//android.view.ViewGroup[@content-desc="dropdownFormComponentField"]/android.view.ViewGroup')))
            el.click()
            time.sleep(1)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]')))
            el.click()
            next = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nextButton')))
            next.click()

            activity_complete(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_walkin_autofetch(self):
        try:
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")))
            el.click()
            time.sleep(1)
            contact = setting_contact(self.driver)
            cameraretake(self.driver)
            FLEP_auto_fetch_visitor(self.driver, self.walkin_details, contact)
            time.sleep(1)
            emergency_details_autofetch(self.driver, self.walkin_details)
            time.sleep(0.5)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '//android.view.ViewGroup[@content-desc="dropdownFormComponentField"]/android.view.ViewGroup')))
            el.click()
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]')))
            el.click()
            time.sleep(0.5)
            self.driver.find_element_by_accessibility_id('nextButton').click()
            unique_id_autofetch(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '//android.view.ViewGroup[@content-desc="dropdownFormComponentField"]/android.view.ViewGroup')))
            el.click()
            time.sleep(1)
            el = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]')))
            el.click()
            next = WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nextButton')))
            next.click()
            activity_complete(self.driver, self.walkin_details)
            #check_out(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_request_meeting(self):
        #self.time.sleep(5)
        try:
            settings = WebDriverWait(self.driver, 15, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settingsButton")))
            settings.click()
            #time.sleep(3)
            self.driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="requestMeeting"]/android.view.ViewGroup').click()

            Fname = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Your First Name")))
            Fname.send_keys('test_w')

            Lname = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Your Last Name")))
            Lname.send_keys('test_s')

            Phone = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Your Phone Number")))
            Phone.send_keys('2222200000')
            time.sleep(3)
            Meeting = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//android.widget.EditText[@content-desc="searchFieldMeetingField"]')))
            Meeting.send_keys('Man')
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '	//android.view.ViewGroup[@content-desc="mansi sahu"]').click()

            time11 = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "dateTimePicker")))
            time11.click()

            c = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ID, "android:id/button1")))
            c.click()

            a = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Meeting Agenda")))
            a.send_keys('hi')
            self.driver.hide_keyboard()
            a = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                       '//android.view.ViewGroup[@content-desc="carryMobilePhone"]/android.widget.Switch')))
            a.click()

            a = WebDriverWait(self.driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                        '//android.view.ViewGroup[@content-desc="requestMeeting"]')))
            a.click()
        except:
            print('Unable to request meeting')
            time.sleep(2)
            takeScreenshot(self.driver)
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise
    
    def test_walkin_details_offline(self):

        #status="offline"

        offline_mode(self.driver)
        time.sleep(1)
        walkin_visitor(self.driver, self.offline_walkin_details)
        self.driver.toggle_wifi()

    def test_logout(self):
        logout(self.driver)
    """


