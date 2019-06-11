import pytest
import time
from utilities.Resources_small import *

@pytest.mark.usefixtures("data","driver")
class TestWalkInemail():

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
        self.email_invited_details = data['email_invited_details']

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
            self.driver.background_app(1)
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
            self.driver.background_app(1)
        except:
            print("exception")
            self.status_test = False
            statusOftest(self.status_test, self.driver)
            raise
