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
        self.walkin_email_details=data['walkin_email_details']

    @pytest.mark.order1
    @pytest.mark.dependency(name="Start activity")
    def test_start_activity(self):
        try:
            start_activity(self.driver)
        except Exception as e:
            print(e)
            print("unable to start activity ")

    @pytest.mark.order2
    @pytest.mark.dependency(name="Login activity",depends=["Start activity"])
    def test_login(self):
        try:
            login(self.driver)

        except Exception as e:
            print (e)


    """@pytest.mark.order3
    @pytest.mark.dependency(name="fresh_user_walkin",depends=["Login activity"])
    def test_fresh_user_walkin(self):
        walkin_visitor(self.driver,self.walkin_details)"""

    @pytest.mark.order3
    @pytest.mark.dependency(name="autofetch_user_walkin", depends=["Login activity"])
    def test_autofetch_user_walkin(self):

        autofetch_user(self.driver, self.walkin_details)
    @pytest.mark.order5
    @pytest.mark.dependency(name="member_check_in", depends=["Login activity"])
    def test_member_check_in(self):
        try:
            user_action = TouchAction(self.driver)
            checkIn(self.driver)
            time.sleep(0.5)
            setting_contact_member(self.driver)
            print("old screen")
            cameraretake(self.driver)
            FLEP_auto_fetch_member(self.driver, self.member_details)

            Meeting_with_screen(self.driver)
            time.sleep(1)
            try:
                emergency_details_autofetch(self.driver, self.member_details)
                unique_id_autofetch(self.driver, self.member_details['unique_id'])

            except:
                emergency_contact(self.driver,self.member_details)
                unique_id(self.driver,self.member_details)

            Next(self.driver)
            time.sleep(1)
            activity_complete(self.driver, self.member_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise
    @pytest.mark.order7
    @pytest.mark.dependency(name="invited_user", depends=["Login activity"])
    def test_invited_user(self):
        try:
            self.status_test = False
            checkIn(self.driver)
            setting_contact_invite(self.driver)
            InvitedWF(self.driver)
            FLEP_auto_fetch_member(self.driver, self.invited_details)
            # time.sleep(2)
            Next(self.driver)
            time.sleep(2)
            activity_complete(self.driver, self.invited_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    @pytest.mark.order8
    @pytest.mark.dependency(name="general_activity_member", depends=["Login activity"])
    def test_general_activity_member(self):
        try:
            late_tracking(self.driver)
            setting_contact_member(self.driver)
            # time.sleep(2)
            cameraretake(self.driver)
            FLEP_auto_fetch_member(self.driver, self.member_details)
            time.sleep(0.5)
            emergency_details_autofetch(self.driver, self.member_details)
            time.sleep(0.5)
            Next(self.driver)
            unique_id_autofetch(self.driver, self.member_details['unique_id'])
            gender_Screen(self.driver)
            Next(self.driver)
            activity_complete_general(self.driver, self.member_details)
            check_out(self.driver, self.member_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
            assert True
        except:
            print("exception")
            takeScreenshot(self.driver)
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_walkin(self):

        try:
            late_tracking(self.driver)
            time.sleep(0.5)
            contact = setting_contact(self.driver)
            camera(self.driver)
            FLEP_Screen(self.driver, self.walkin_details, contact)
            emergency_contact(self.driver, self.walkin_details)
            Next(self.driver)
            unique_id(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            self.driver.hide_keyboard()
            Next(self.driver)

            activity_complete_general(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_walkin_autofetch(self):
        try:
            late_tracking(self.driver)
            time.sleep(0.5)
            contact = setting_contact(self.driver)
            cameraretake(self.driver)
            FLEP_auto_fetch_visitor(self.driver, self.walkin_details, contact)
            time.sleep(1)
            emergency_details_autofetch(self.driver, self.walkin_details)
            Next(self.driver)
            unique_id_autofetch(self.driver, self.walkin_details['unique_id'])
            gender_Screen(self.driver)
            Next(self.driver)
            activity_complete_general(self.driver, self.walkin_details)
            # check_out(self.driver, self.walkin_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_checkout_user(self):
        check_out(self.driver, self.walkin_details)
        check_out(self.driver, self.member_details)
        check_out(self.driver,self.invited_details)

    def test_email_walkin(self):
        walkin_visitor(self.driver,self.walkin_email_details)

    def test_email_autofetch(self):
        autofetch_user(self.driver,self.walkin_email_details)