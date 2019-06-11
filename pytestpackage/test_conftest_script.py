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
        time.sleep(3)
        time.sleep(0.5)
        permission_buttons(self.driver)
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
        """q = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.Spinner')))

        q.click()
        r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')))
        r.click()
        """
        p = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization ID')))
        p.send_keys('N1')
        p = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization Code')))
        p.send_keys('1')
        self.driver.hide_keyboard()
        r = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'LOGIN')))
        r.click()

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="Check-In"]')))
        m.click()

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Email')))
        m.click()

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Please write here')))
        m.send_keys('m@gmm.in')
        self.driver.hide_keyboard()

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Back')))
        m.click()
        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="Check-In"]')))
        m.click()
        """
        p = WebDriverWait(self.driver, 2, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'QR')))
        p.click()

        p = WebDriverWait(self.driver, 2, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Mobile Number')))
        p.click()
        """
        #3
        i="9"
        j="5"
        contact=""
        for k in range(5):

            #self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[12]/android.view.ViewGroup').click()
            self.driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="nine"]/android.view.ViewGroup').click()
            contact=contact+i;

        for k in range(5):

            #self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[12]/android.view.ViewGroup').click()
            self.driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="five"]/android.view.ViewGroup').click()
            contact=contact+j;

        """try:
            self.driver.find_element_by_accessibility_id('4').click()
            #self.driver.find_element_by_accessibility_id('7').click()
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[12]/android.view.ViewGroup').click()
        except Exception as e:
            print ("error")
            print(e)
        self.driver.find_element_by_accessibility_id('5').click()
        self.driver.find_element_by_accessibility_id('5').click()
        self.driver.find_element_by_accessibility_id('6').click()
        self.driver.find_element_by_accessibility_id('6').click()
        self.driver.find_element_by_accessibility_id('7').click()
        self.driver.find_element_by_accessibility_id('7').click()
        self.driver.find_element_by_accessibility_id('8').click()
        self.driver.find_element_by_accessibility_id('8').click()
        """
        """for k in range(3):
            self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="3"]').click()
            print("loop1")
            contact=contact+i

        time.sleep(1)
        for k in range(7):
            self.driver.find_element_by_xpath('	//android.widget.TextView[@content-desc="7"]').click()
            contact = contact + j
            print("loop2")
        """
        print(contact)

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
        m.click()
        try:
            VisitorWF(self.driver)
            #self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Visitor"]').click()
        except Exception as e:
            print("error")
            print("Exception")


        camera(self.driver)
        #time.sleep(5)
        #FLEP_Screen(self.driver,self.walkin_details,contact)
        FirstName = WebDriverWait(self.driver, 5, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'First Name')))
        self.driver.set_value(FirstName,self.walkin_details['firstname'])
        print("fname done")
        self.driver.hide_keyboard()
        LastName = WebDriverWait(self.driver, 5, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Last Name')))
        self.driver.set_value(LastName, self.walkin_details['lastname'])

        print("lname done")
        self.driver.hide_keyboard()
        Email = WebDriverWait(self.driver, 5, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'email')))
        self.driver.set_value(Email, self.walkin_details['email'])
        print("email done")
        self.driver.hide_keyboard()
        contact_element = WebDriverWait(self.driver, 5, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID,'PhoneNumber')))
        num = contact_element.get_attribute('text')
        print("num " + num)
        print(contact)

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
        m.click()

        time.sleep(0.5)

        #Meeting_with_offline_screen(self.driver)
        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'unique_id')))
        m.send_keys(self.walkin_details['unique_id'])
        gender_Screen(self.driver)
        Multi_select_screen(self.driver)
        GOVT_Id_Screen(self.driver)
        single_dropdown_screen(self.driver)
        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@content-desc="address"]')))
        m.send_keys(self.walkin_details['address'])
        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@content-desc="Emergencycontactname"]')))
        m.send_keys(self.walkin_details['Emergency_contact_name'])

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@content-desc="Emergencycontact"]')))
        m.send_keys(self.walkin_details['Emergency_contact'])
        self.driver.hide_keyboard()
        rating_Screen(self.driver)

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
        m.click()

        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Mansi Test')))
        m.click()
        NDA_screen(self.driver)
        m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
        m.click()
        user_action=TouchAction(self.driver)
        user_action.tap(x=285, y=809).perform()
        time.sleep(0.5)
        #
        user_action.tap(x=482, y=810).perform()
        date_and_time(self.driver)


assert True
