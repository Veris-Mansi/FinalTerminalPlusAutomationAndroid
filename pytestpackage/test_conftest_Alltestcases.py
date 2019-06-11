import unittest
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
        self.walkin_email_details=data['walkin_email_details']
        self.member_email_detail=data['member_email_detail']
        self.email_invited_details=data['email_invited_details']

    def test_start_activity(self):
        try:
            start_activity(self.driver)
        except Exception as e:
            print(e)
            print("unable to start activity")


    def test_login(self):
        try:
            login(self.driver)

        except Exception as e:
            print (e)


    def test_fresh_user_walkin(self):
        walkin_visitor(self.driver,self.walkin_details)
        self.driver.background_app(1)

    def test_member_check_in(self):
        try:

            time.sleep(0.5)
            checkIn(self.driver)
            time.sleep(0.5)
            #setting_contact_member(self.driver)
            setting_contact_member_touch(self.driver)
            phone = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Employee')))
            phone.click()

            cameraretake(self.driver)
            print(type(self.member_details))
            print(self.member_details)
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
    def test_invited_user(self):
        try:
            checkIn(self.driver)
            contact=setting_invite_touch(self.driver)
            InvitedWF(self.driver)
            FLEP_auto_fetch_visitor(self.driver,self.invited_details,contact)
            meeting_with_invite(self.driver)
            Next(self.driver)
            time.sleep(2)
            activity_complete(self.driver, self.invited_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
            self.driver.background_app(2)
        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_member(self):
        try:

            time.sleep(0.5)
            late_tracking(self.driver)
            setting_contact_member_touch(self.driver)

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
            self.status_test = True
            statusOftest(self.status_test, self.driver)
            #self.driver.background_app(2)
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
            contact = setting_contact_touch(self.driver)
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
            self.driver.background_app(2)
        except:
            print("exception")
            takeScreenshot(self.driver)

            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_email_walkin(self):
        try:

            time.sleep(1)
            # walkin_visitor(self.driver, self.walkin_email_details)
            checkIn(self.driver)
            time.sleep(0.5)
            email = setting_email(self.driver)
            wf = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Visitor2_email')))
            wf.click()
            camera(self.driver)
            m = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Emergencycontactname')))
            m.send_keys(self.walkin_email_details['Emergency_contact_name'])
            Next(self.driver)
            FLEP_Email_Screen(self.driver, self.walkin_email_details, email)
            activity_complete(self.driver, self.walkin_email_details)
            self.driver.background_app(2)
        except:
            takeScreenshot(self.driver)
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_email_member(self):

        try:
            checkIn(self.driver)
            time.sleep(0.5)

            setting_email_member(self.driver)
            phone = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Employee')))
            phone.click()
            print("sleep")
            time.sleep(0.5)
            cameraretake(self.driver)

            print("sleep")
            time.sleep(0.5)
            FLEP_auto_fetch_member(self.driver, self.member_email_detail)
            Next(self.driver)
            Meeting_with_screen(self.driver)
            emergency_details_autofetch(self.driver, self.member_email_detail)
            unique_id_autofetch(self.driver, self.member_email_detail['unique_id'])
            Next(self.driver)
            time.sleep(1)
            activity_complete(self.driver, self.member_email_detail)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
            self.driver.background_app(1)
        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    def test_email_invited(self):
        try:
            checkIn(self.driver)
            email = setting_email_invite(self.driver)
            InvitedWF(self.driver)
            FLEP_Autofetch_Email_walkin(self.driver, self.email_invited_details, email)
            meeting_with_invite(self.driver)
            Next(self.driver)
            time.sleep(2)
            activity_complete(self.driver, self.email_invited_details)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
        except:
            self.status_test = False
            takeScreenshot(self.driver)
            statusOftest(self.status_test, self.driver)
            raise

    def test_general_activity_emailmember(self):
        try:

            time.sleep(0.5)
            late_tracking(self.driver)
            setting_email_member(self.driver)
            Next(self.driver)
            # time.sleep(2)
            cameraretake(self.driver)
            FLEP_auto_fetch_member(self.driver, self.member_email_detail)
            time.sleep(0.5)
            emergency_details_autofetch(self.driver, self.member_email_detail)
            time.sleep(0.5)
            Next(self.driver)
            unique_id_autofetch(self.driver, self.member_email_detail['unique_id'])
            gender_Screen(self.driver)
            Next(self.driver)
            activity_complete_general(self.driver, self.member_email_detail)
            self.status_test = True
            statusOftest(self.status_test, self.driver)
            self.driver.background_app(1)
            assert True
        except:
            print("exception")
            takeScreenshot(self.driver)
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise
    def test_general_activity_walkin_autofetch(self):
        try:
            late_tracking(self.driver)
            time.sleep(0.5)
            contact = setting_contact_touch(self.driver)
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
            #self.driver.background_app(2)
        except:
            print("exception")
            takeScreenshot(self.driver)
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_email_autofetch(self):
        try:
            # autofetch_user(self.driver,self.walkin_email_details)
            checkIn(self.driver)
            time.sleep(0.5)
            email = setting_email(self.driver)
            wf = WebDriverWait(self.driver, 10, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Visitor2_email')))
            wf.click()
            cameraretake(self.driver)

            emer_name = WebDriverWait(self.driver, 20, poll_frequency=0.005).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Emergencycontactname')))
            name = emer_name.text
            print(name)
            assert name == self.walkin_email_details['Emergency_contact_name']
            Next(self.driver)
            FLEP_Autofetch_Email_walkin(self.driver, self.walkin_email_details, email)
            activity_complete(self.driver, self.walkin_email_details)

        except:
            takeScreenshot(self.driver)
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise
    def test_autofetch_user_walkin(self):

        autofetch_user(self.driver, self.walkin_details)

    def test_checkout_walkinuser(self):
       try:
           check_out(self.driver, self.walkin_details)

       except:
           print("exception")
           self.status_test = False
           statusOftest(self.status_test, self.driver)
           raise
    def test_checkout_member(self):
        try:
            check_out(self.driver, self.member_details)
            #self.driver.background_app(1)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise
    def test_checkout_invite(self):
        try:
            check_out(self.driver, self.invited_details)

        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise
    def test_email_checkout_walkinuser(self):
        try:
            check_out(self.driver, self.walkin_email_details)

        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_email_checkout_invite(self):
        try:
            check_out(self.driver, self.email_invited_details)

        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

    def test_email_checkout_member(self):
        try:
            check_out(self.driver, self.member_email_detail)

        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise

