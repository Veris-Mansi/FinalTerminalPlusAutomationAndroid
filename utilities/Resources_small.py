import time
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

i=1
def start_server():
    # if server is already started in some port then it will not show error and requests will be sent to that paticular server

    os.system("start /B start cmd.exe @cmd /k appium")

    #time.sleep(5)

def settingup():

    desired_capabilities = {

        "app": "C:\\Users\\veris\Videos\\JUNE_latestt_again\\JUNE-Terminal-Plus-release.apk",
        "platformName": "Android",
        "deviceName": "fc378d12",
        "appActivity": ".MainActivity",
        "appPackage": "com.veristerminal",
        "unicodeKeyboard": False,
        "resetKeyboard": False,
        "platformVersion": "8.1.0",
        "appiumVersion": "1.12.1"
    }
    walkin_details = {
        "firstname": "tone",
        "lastname": "ttwo",
        "email": "tt@st.com",
        "unique_id":"test111",
        "address":"JMD",
        "Emergency_contact_name":"TOM",
        "Emergency_contact":"9988776655",
        "status":"walkin",
        "type":"mobile"
    }
    walkin_email_details = {
        "firstname": "emone",
        "lastname": "emto",
        "phone": "7777777777",
        "unique_id": "e111",
        "address": "JMD",
        "Emergency_contact_name": "RAM",
        "Emergency_contact": "9988776644",
        "status": "walkin",
        "type": "email"
    }
    member_details = {
        "firstname": "mansi",
        "lastname": "sahu",
        "email": "mansisahu1480@gmail.com",
        "phone": "9993483676",
        "unique_id": "m123",
        "Emergency_contact_name": "test name",
        "status": "member",
        "Emergency_contact": "9992223331",
        "type": "mobile"
    }
    invited_details = {
        "firstname": "invite",
        "lastname": "invite",
        "email": "invite@a.nn",
        "phone":"3333333333",
        "status":"invite",
        "type": "mobile"
    }
    email_invited_details = {
        "firstname": "invemail",
        "lastname": "invemail",
        "email": "testveris19@gmail.com",
        "phone": "9638527418",
        "status": "invite",
        "type": "email"
    }
    offline_walkin_details = {
        "firstname": "offone",
        "lastname": "offtwo",
        "email": "off@t.co",
        "unique_id": "test111",
        "address": "JMD",
        "Emergency_contact_name": "TOM",
        "Emergency_contact": "9988776655",
        "status": "offline",
        "type": "mobile"
    }
    member_email_detail={
        "firstname": "emone",
        "lastname": "emone",
        "email": "nurik@rockmail.top",
        "phone": "7777777777",
        "unique_id": "m123",
        "Emergency_contact_name": "tname",
        "Emergency_contact": "9992223331",
        "status": "member",
        "type": "email"
    }

    data={}
    data['desired_capabilities']=desired_capabilities
    data['walkin_details']=walkin_details
    data['member_details']=member_details
    data['invited_details']=invited_details
    data['offline_walkin_details']=offline_walkin_details
    data['walkin_email_details']=walkin_email_details
    data['email_invited_details']=email_invited_details
    data['member_email_detail'] = member_email_detail
    return data


def permission_buttons(driver):
    for a in range(2):
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
        time.sleep(0.05)
        #driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
def launch_application(desired_capabilities):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    return driver


def permission_buttons_small_device(driver):
    for a in range(2):
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]').click()
        time.sleep(0.5)
def start_activity(driver):
    time.sleep(0.5)
    permission_buttons_small_device(driver)
    time.sleep(1.5)
    driver.press_keycode(4)
    time.sleep(0.5)
    driver.start_activity("com.veristerminal", ".MainActivity")
    time.sleep(1)


def login(driver):
    #start_activity(driver)
    q = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located(
            (By.XPATH, '//android.view.ViewGroup[@content-desc="domainPicker"]/android.widget.Spinner')))
    q.click()

    r = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')))
    r.click()

    p = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization ID')))
    p.send_keys('N1')

    driver.hide_keyboard()
    p = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Authorization Code')))
    p.send_keys('1')
    driver.hide_keyboard()
    r = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'LOGIN')))
    r.click()
    assert True
def checkIn(driver):

    checkin= WebDriverWait(driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Check-In')))
    checkin.click()
    assert True

def setting_email(driver):

    p = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Email')))
    p.click()
    q = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Please write here')))
    q.send_keys('qqq@nb.com')
    email=q.text
    print(email)
    driver.hide_keyboard()
    p = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
    p.click()

    return email

def setting_email_member(driver):

    p = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Email')))
    p.click()
    q = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Please write here')))
    q.send_keys('nurik@rockmail.top')
    email=q.text
    driver.hide_keyboard()
    print(email)
    p = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
    p.click()
    return email

def setting_email_invite(driver):
    p = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Email')))
    p.click()
    q = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Please write here')))
    q.send_keys('testveris19@gmail.com')
    email = q.text
    print(email)
    driver.hide_keyboard()
    p = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
    p.click()
    return email

def setting_contact_invite(driver):
    i = "3"
    contact = "3333333333"
    useraction=TouchAction(driver)
    for k in range(10):
        """p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@content-desc="three"]')))
        p.click()
        contact = contact + i;"""
        useraction.tap(x=624, y=573).perform()
    time.sleep(0.05)
    Next(driver)
    return contact

def setting_invite_touch(driver):
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Mobile Number')))
    p.click()
    time.sleep(0.5)
    useraction=TouchAction(driver)
    contact = "3333333333"
    for i in range(10):
        useraction.tap(x=624, y=573).perform()

    Next(driver)
    return contact

def setting_contact_touch(driver):
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Mobile Number')))
    p.click()
    time.sleep(0.5)
    useraction=TouchAction(driver)
    useraction.tap(x=174, y=834).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=620, y=709).perform()
    useraction.tap(x=620, y=709).perform()
    useraction.tap(x=620, y=709).perform()
    useraction.tap(x=174, y=834).perform()
    useraction.tap(x=174, y=834).perform()

    time.sleep(0.5)
    Next(driver)
    contact="7888866677"
    return contact
    """
    9=(new TouchAction(driver)).tap(628, 843).perform()
    8=(new TouchAction(driver)).tap(399, 841).perform()
    7=(new TouchAction(driver)).tap(174, 834).perform()
    6=(new TouchAction(driver)).tap(620, 709).perform()
    5=(new TouchAction(driver)).tap(401, 709).perform()
    4=(new TouchAction(driver)).tap(178, 715).perform()
    3=(new TouchAction(driver)).tap(624, 573).perform()
    2=(new TouchAction(driver)).tap(395, 575).perform()
    1=(new TouchAction(driver)).tap(170, 579).perform()
    0=(new TouchAction(driver)).tap(399, 974).perform()
    """

def setting_contact_member_touch(driver):
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Mobile Number')))
    p.click()
    time.sleep(0.5)
    useraction=TouchAction(driver)
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=624, y=573).perform()
    useraction.tap(x=178, y=715).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=624, y=573).perform()
    useraction.tap(x=620, y=709).perform()
    useraction.tap(x=174, y=834).perform()
    useraction.tap(x=620, y=709).perform()
    time.sleep(0.5)
    Next(driver)
def setting_contact(driver):

    i = "8"
    j="4"

    contact = ""
    print("in small device")
    for k in range(5):
        #p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        #    EC.presence_of_element_located((By.XPATH,
        #                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[15]/android.view.ViewGroup')))
        """p=WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@content-desc="nine"]')))
        p.click()"""
        print("waiting for ",i)
        p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nine')))
        print("done ",i)
        print(p)
        p.click()
        print("click done ",i)
        contact = contact + i

    for k in range(5):
        """p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[13]/android.view.ViewGroup')))
        
        p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//android.widget.TextView[@content-desc="two"]')))

        p.click()
        """
        print("waiting for ", j)
        p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'two')))
        print("done ", j)
        print(p)

        p.click()
        print("click done ",j)
        contact = contact + j

    Next(driver)
    return contact

def setting_contact_offline(driver):
    phone = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Enter mobile number')))
    phone.click()
    contact_no = ""
    i="9"
    j="1"
    for k in range(5):
        p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[13]/android.view.ViewGroup')))
        p.click()
        contact_no=contact_no+i
        time.sleep(0.05)

    for k in range(5):
        p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[13]/android.view.ViewGroup')))
        p.click()
        contact_no = contact_no + j
        time.sleep(0.05)

    Next(driver)

    return contact_no

def setting_offline_touch(driver):
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Mobile Number')))
    p.click()
    time.sleep(0.5)
    useraction=TouchAction(driver)
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=628, y=843).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=399, y=841).perform()
    useraction.tap(x=628, y=843).perform()

    contact="9999988889"

    return contact

def setting_contact_member(driver):

    print("wait before nine")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nine')))
    print("done 9", p)
    p.click()
    print("click done 9")

    print("wait before nine")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nine')))
    print("done 9", p)
    p.click()
    print("click done 9")

    print("wait before nine")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'nine')))
    print("done 9", p)
    p.click()
    print("click done 9")

    print("wait before 3")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'three')))
    print("done 3" , p)
    p.click()
    print("click done 3")
    print("wait before 4")

    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'four')))
    print("done 4" ,p)
    p.click()
    print("click done 4")

    print("wait before 8")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'eight')))
    print("done 8",p)
    p.click()
    print("click done 8")

    print("wait before 3")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'three')))
    print("done 3",p)
    p.click()
    print("click done 3")
    print("wait before 6")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'six')))
    print("done 6",p)
    p.click()
    print("click done 6")
    print("wait before 7")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'seven')))
    print("done 7 ",p)
    p.click()
    print("click done 7")
    print("wait before 6")
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'six')))
    print("done 6 ", p)
    p.click()
    print("click done 6 ",p)
    Next(driver)
    #
def late_tracking(driver):
    el = WebDriverWait(driver, 10, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Late_Tracking')))
    el.click()
def walkin_visitor(driver,walkin_details):
    try:
        time.sleep(1)
        status = walkin_details['status']
        type=walkin_details['type']
        user_action = TouchAction(driver)
        checkIn(driver)

        if (status == 'walkin' and type=='mobile'):
            contact = setting_contact_touch(driver)
            print(contact)

        elif(status == 'walkin' and type=='email'):
            email=setting_email(driver)
            print("email is "+email)

        elif (status == 'offline'):
            contact = setting_offline_touch(driver)
            print(contact)

        visitor = WebDriverWait(driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))
        #
        if (visitor.is_displayed()):
            print("Workflow autofetched test case passed")
            assert True
            visitor.click()
        else:
            assert False
        camera(driver)

        if (status == 'walkin' and type=='mobile'):
            FLEP_Screen(driver,walkin_details,contact)
        elif(status == 'walkin' and type=='email'):
            FLEP_Email_Screen(driver,walkin_details,email)
        elif (status == 'offline'):
            FLEP_Screen(driver, walkin_details, contact)

        if (status == 'walkin'):
            Meeting_with_screen(driver)
        elif (status == 'offline'):
            Meeting_with_offline_screen(driver)
        unique_id(driver, walkin_details['unique_id'])
        gender_Screen(driver)
        Multi_select_screen(driver)
        GOVT_Id_Screen(driver)
        single_dropdown_screen(driver)
        m = WebDriverWait(driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'address')))
        m.send_keys(walkin_details['address'])

        driver.hide_keyboard()
        emergency_contact(driver, walkin_details)
        rating_Screen(driver)
        time.sleep(0.05)
        #
        next = WebDriverWait(driver, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Next")))
        next.click()
        multi_tenant(driver)
        NDA_Smallscreen(driver)
        time.sleep(1)
        #
        m = WebDriverWait(driver, 20, poll_frequency=0.05).until(
            EC.presence_of_element_located((By.XPATH, '	//android.widget.TextView[@content-desc="Print"]')))
        m.click()
        m = WebDriverWait(driver, 20, poll_frequency=0.05).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
        m.click()
        date_and_time_small(driver)
        activity_complete(driver, walkin_details)
        #check_out(driver, walkin_details)
        status_test = True
        statusOftest(status_test, driver)
    except:
        status_test = False
        takeScreenshot(driver)
        statusOftest(status_test, driver)
        raise

def Next(driver):
    m = WebDriverWait(driver, 20, poll_frequency=0.05).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
    m.click()

def autofetch_user(driver,walkin_details):

    status=walkin_details['status']
    type=walkin_details['type']
    try:
        user_action = TouchAction(driver)
        checkIn(driver)
        if (status == 'walkin' and type=='mobile'):
            contact = setting_contact_touch(driver)
            print(contact)

        elif(status == 'walkin' and type =='email'):
            email=setting_email(driver)
            print(email)

        elif (status == 'offline'):
            contact = setting_offline_touch(driver)
            print(contact)

        visitor = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Visitor")))

        if (visitor.is_displayed()):
            assert True
            visitor.click()
        else:
            assert False
        #time.sleep(1)
        cameraretake(driver)

        if (status == 'walkin' and type=='mobile'):
            FLEP_auto_fetch_visitor(driver,walkin_details,contact)
        elif(status == 'walkin' and type=='email'):
            FLEP_Autofetch_Email_walkin(driver,walkin_details,email)
        elif (status == 'offline'):
            FLEP_auto_fetch_visitor(driver, walkin_details, contact)

        if(status == 'walkin'):
            Meeting_with_screen(driver)
        elif (status == 'offline'):
            Meeting_with_offline_screen(driver)
        unique_id_autofetch(driver, walkin_details['unique_id'])
        gender_Screen(driver)
        Multi_select_screen(driver)
        Govt_Id_Retake(driver)
        single_dropdown_screen(driver)
        time.sleep(1)
        m = WebDriverWait(driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'address')))
        my_address=m.text
        print(my_address)
        assert my_address == walkin_details['address']
        emergency_details_autofetch(driver, walkin_details)
        rating_Screen(driver)
        Next(driver)
        time.sleep(0.5)
        multi_tenant(driver)
        NDA_Smallscreen(driver)
        time.sleep(0.5)
        #
        m = WebDriverWait(driver, 20, poll_frequency=0.05).until(
            EC.presence_of_element_located((By.XPATH, '	//android.widget.TextView[@content-desc="Print"]')))
        m.click()
        m = WebDriverWait(driver, 20, poll_frequency=0.05).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
        m.click()
        date_and_time(driver)
        activity_complete(driver, walkin_details)
        #(driver, walkin_details)
        status_test = True
        statusOftest(status_test, driver)
    except:
        print("exception")
        takeScreenshot(driver)
        status_test = False
        statusOftest(status_test, driver)
        raise
def VisitorWF(driver):

    m = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Visitor')))
    m.click()
def InvitedWF(driver):

    m = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Invited')))
    m.click()

def EmployeeWF(driver):

    m = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Employee')))
    m.click()



def camera(driver):
    image=WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Click Image")))
    if(image.is_displayed()):
        assert True
        image.click()
    else:
        assert False
    Next(driver)
    assert True
    #time.sleep(10)
def cameraretake(driver):
    print("camera....retake")
    retakeButton = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Retake")))
    status = retakeButton.is_displayed()
    if (status):
        assert True
    else:
        print("Image not autofetched test case failed")
        assert False
    print("image")
    Next(driver)
def FLEP_Email_Screen(driver,walkin_details,email):
    FirstName = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'First Name')))
    driver.set_value(FirstName, walkin_details['firstname'])
    print("fname done")
    driver.hide_keyboard()
    LastName = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Last Name')))
    driver.set_value(LastName, walkin_details['lastname'])
    print("lname done")
    Email = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'email')))
    myemail=Email.text
    assert myemail==email
    contact_element = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'PhoneNumber')))
    contact_element.send_keys(walkin_details["phone"])
    Next(driver)

def FLEP_Autofetch_Email_walkin(driver,member_details,email):
    FirstName = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'First Name')))
    text = FirstName.text
    print(text)
    # print(member_details['firstname'])
    assert text == member_details['firstname']
    driver.hide_keyboard()
    LastName = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Last Name')))
    text1 = LastName.text
    print(text1)
    assert text1 == member_details['lastname']
    print("lname done")
    driver.hide_keyboard()

    Email = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'email')))
    myemail=Email.text
    assert myemail==email
    driver.hide_keyboard()

    contact_element = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'PhoneNumber')))
    c =contact_element.text
    assert c == member_details['phone']
    driver.hide_keyboard()

    Next(driver)

def FLEP_Screen(driver,walkin_details,contact):
    FirstName = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'First Name')))
    driver.set_value(FirstName, walkin_details['firstname'])
    print("fname done")
    driver.hide_keyboard()
    LastName = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Last Name')))
    driver.set_value(LastName, walkin_details['lastname'])

    print("lname done")
    driver.hide_keyboard()
    Email = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'email')))
    driver.set_value(Email, walkin_details['email'])
    print("email done")
    driver.hide_keyboard()
    contact_element = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'PhoneNumber')))
    num = contact_element.get_attribute('text')
    assert num == contact
    driver.hide_keyboard()

    btn = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Next")))
    btn.click()
    assert True

def FLEP_auto_fetch_member(driver,member_details):
    #time.sleep(5)
    Fname=WebDriverWait(driver, 5, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "First Name")))
    text = Fname.text
    print("email member details ",member_details)
    print(type(member_details))
    print(text)
    print(member_details['firstname'])
    assert text == member_details['firstname']
    #time.sleep(3)
    Lname = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Last Name")))

    status = Lname.is_displayed()
    print(status)
    text1 = Lname.text
    print(text1)
    assert text1 == member_details['lastname']
    email = WebDriverWait(driver, 5, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "email")))
    #Email = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Email"]/android.widget.EditText')
    text2 = email.text
    print(text2)
    if (len(text2) == 0):
        driver.set_value(email,member_details['email'])
        #time.sleep(0.5)
    else:
        if (len(text2) > 0 and text2 == member_details['email']):
            assert True
        else:
            assert False

    driver.hide_keyboard()
    #time.sleep(3)
    Phone = WebDriverWait(driver, 2, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "PhoneNumber")))
    text4 = Phone.text
    print(text4)
    if (len(text4) > 0 and text4 == member_details['phone']):
        assert True
        #print("Contact autofetched test case passed")
    else:
        driver.set_value(Phone, member_details['phone'])
        assert True
    Next(driver)
    #time.sleep(2)

def FLEP_auto_fetch_visitor(driver,visitor_details,contact_no):
    Fname = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "First Name")))
    text = Fname.text
    print(text)
    assert text == visitor_details['firstname']

    Lname =  WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Last Name")))
    text1 = Lname.text
    print(text1)
    assert text1 == visitor_details['lastname']

    Email =  WebDriverWait(driver, 2, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "email")))
    text2 = Email.text
    print(text2)
    print(len(text2))
    if(text2 == 'Email'):
        driver.set_value(Email,'testinvite@a.nn')
        assert True
    else:
        assert text2 == visitor_details['email']

    Phone = WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "PhoneNumber")))
    text4 = Phone.text
    print(text4)
    assert text4 == contact_no
    driver.find_element_by_accessibility_id('Next').click()
    #time.sleep(2)

def Meeting_with_screen(driver):

    meeting = driver.find_element_by_accessibility_id('WhomToMeet')
    driver.set_value(meeting, "man")
    #time.sleep(3)
    el=WebDriverWait(driver, 15, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'mansi sahu')))
    el.click()
    driver.hide_keyboard()

def Meeting_with_offline_screen(driver):

    meeting = driver.find_element_by_accessibility_id('WhomToMeet')
    driver.set_value(meeting, "man")
    #time.sleep(3)
    el=WebDriverWait(driver, 2, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Unable to find someone?')))
    el.click()
    driver.hide_keyboard()
def meeting_with_invite(driver):
    meeting = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'WhomToMeet')))
    text = meeting.text
    if (len(text) > 0 and text == 'Mansi Sahu'):
        print("Meeting with test case passed")
        assert True
    else:
        print("Meeting with test case failed")
        assert False


def unique_id(driver,uniqueid):
    b = WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"unique_id")))
    b.send_keys(uniqueid)

def unique_id_autofetch(driver,unique_id):
    uniqid=WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"unique_id")))
    my_id = uniqid.text
    print(my_id)
    assert my_id == unique_id

def gender_Screen(driver):
    gender = []
    gender = driver.find_elements_by_xpath(
        '//android.view.ViewGroup[@content-desc="radioButtonField"]/android.view.ViewGroup/android.view.ViewGroup')
    print(len(gender))
    status_radio = gender[0].is_selected()

    if (status_radio == False):
        gender[0].click()
        assert True

def Multi_select_screen(driver):

    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    #time.sleep(0.5)
    a=WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")))
    a.click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
    assert True
    b = WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")))
    b.click()
    #time.sleep(0.5)
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    assert True
    b = WebDriverWait(driver, 3, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button")))
    b.click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
    assert True
    b = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,"Next")))

    b.click()
    assert True
    #driver.find_element_by_accessibility_id('Next').click()

def multi_tenant(driver):
    s=WebDriverWait(driver, 10, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Search company you wish to visit')))
    s.send_keys('Man')

    a = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Mansi Test")))

    a.click()
def takeScreenshot(driver):
    global i
    filename="./screenshots/test_"+str(i)+'.png'

    try:

        driver.save_screenshot(filename)
        print("saved =>"+filename)

    except NotADirectoryError:
        print("Not a directory")
    i = i + 1
    #print("screenshot saved")

def takeScreenshotError(driver):
    global j
    global j
    j=1
    filename = "./errors/errtest_" + str(j) + '.png'
    try:
        driver.save_screenshot(filename)
        print("saved =>" + filename)

    except NotADirectoryError:
        print("Not a directory")
    j = j + 1

def single_dropdown_screen(driver):

    driver.find_element_by_accessibility_id('dropdownFormComponentField').click()
    assert True
    #time.sleep(0.5)
    b = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")))
    b.click()

    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
    # user_action.tap(x=400,y=203).release().perform()
    assert True
    #time.sleep(2)

def rating_Screen(driver):
    time.sleep(0.5)
    listss = driver.find_elements_by_xpath(
        '//android.view.ViewGroup[@content-desc="ratingField"]/android.widget.Button')
    print(len(listss))
    listss[3].click()
    #driver.hide_keyboard
    #time.sleep(1)

def emergency_contact(driver,walkin_details):
    m = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Emergencycontactname')))
    m.send_keys(walkin_details['Emergency_contact_name'])

    m = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Emergencycontact')))
    m.send_keys(walkin_details['Emergency_contact'])
    driver.hide_keyboard()

def NDA_screen(driver):
    time.sleep(1)
    r = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'signatureField')))
    r.click()
    user_action=TouchAction(driver)
    user_action.press(x=240,y=791).move_to(x=369,y=739).release().perform()
    time.sleep(1)
    r = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
    r.click()
    #time.sleep(2)

def NDA_Smallscreen(driver):
    time.sleep(1)
    r = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'signatureField')))
    r.click()


    time.sleep(1)
    user_action = TouchAction(driver)
    user_action.press(x=221, y=901).move_to(x=393, y=911).release().perform()
    time.sleep(1)

    r = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
    r.click()
def date_and_time(driver):
    #time.sleep(2)
    p=WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup')))
    p.click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup').click()
    #time.sleep(2)
    p = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]')))

    p.click()

    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()

    #time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup').click()
    #time.sleep(2)
    driver.find_element_by_id('android:id/button1').click()
    #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
    #time.sleep(1)
    driver.find_element_by_accessibility_id('Next').click()
    #time.sleep(2)

def date_and_time_small(driver):
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.XPATH, '(//android.view.ViewGroup[@content-desc="dateTimePicker"])[1]/android.view.ViewGroup')))
    b.click()
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located(
            (By.ID, 'android:id/button1')))
    b.click()
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located(
            (By.XPATH, '(//android.view.ViewGroup[@content-desc="dateTimePicker"])[2]/android.view.ViewGroup')))
    b.click()
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(
        EC.presence_of_element_located(
            (By.ID, 'android:id/button1')))
    b.click()

    m = WebDriverWait(driver, 20, poll_frequency=0.05).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Next')))
    m.click()

def GOVT_Id_Screen(driver):
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Click Image")))
    b.click()
    #driver.find_element_by_accessibility_id("cardScanClickImageButton").click()
    #time.sleep(10)
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Next")))

    b.click()
   # driver.find_element_by_accessibility_id("cardScanNextButton").click()
    #time.sleep(5)

def Govt_Id_Retake(driver):
    #time.sleep(5)
    retakeButton=WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Retake")))
    #retakeButton = driver.find_element_by_accessibility_id("cardScanRetakeButton")
    status_card = retakeButton.is_displayed()
    print(status_card)
    if (status_card):
        assert True
        print("Image autofetched test case passed")
    else:
        assert False
        print("Image not autofetched test case failed")
    #time.sleep(10)
    b = WebDriverWait(driver, 10, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Next")))

    b.click()
    # driver.find_element_by_accessibility_id("cardScanNextButton").click()
    #time.sleep(2)
def activity_complete(driver,details):
    #driver.find_element_by_accessibility_id('activityCompletedButton').click()
    a = WebDriverWait(driver, 3, poll_frequency=0.05).until(
        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]")))
    texts=a.text
    print(texts)
    a=details['firstname']
    b=details['lastname']
    if(a in texts and b in texts):
        print("test case passed user completed actiivity")
    else:
        print("test case failed")

    b = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID,'Confirm Check-in')))
    b.click()
    assert True

def activity_complete_general(driver,details):
    a = WebDriverWait(driver, 3, poll_frequency=0.05).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]")))
    texts = a.text
    print(texts)
    a = details['firstname']
    b = details['lastname']
    if (a in texts and b in texts):
        print("test case passed correct user checkout")
    else:
        print("test case failed")

    b = WebDriverWait(driver, 3, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Complete Activity')))
    b.click()
    assert True
def activity_checkOut(driver,details):
    a = WebDriverWait(driver, 10, poll_frequency=0.05).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID,"ID_NOT_AVAILABLE")))

    texts = a.text
    print(texts)
    a = details['firstname']
    b = details['lastname']
    if (a in texts and b in texts):
        print("test case passed correct user checkout")
    else:
        print("test case failed")

    b = WebDriverWait(driver, 3, poll_frequency=0.005).until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID, 'Confirm Check-out')))
    b.click()
    assert True

def check_out(driver,details):
    time.sleep(1)
    #driver.find_element_by_accessiautofetch_userbility_id('Check-Out').click()

    checkin= WebDriverWait(driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="Check-Out"]')))
    checkin.click()
    time.sleep(1)
    if(details['status'] == 'walkin' and details['type'] == 'mobile'):
        setting_contact_touch(driver)
        time.sleep(1)
        activity_summary(driver,details)
    elif(details['status'] == 'invite' and details['type'] == 'mobile'):
        setting_invite_touch(driver)
        time.sleep(1)
        activity_summary(driver, details)
    elif (details['status'] == 'member' and details['type'] == 'mobile'):
        setting_contact_member_touch(driver)
    elif (details['status'] == 'walkin' and details['type'] == 'email'):
        setting_email(driver)
        time.sleep(1)
        activity_summary(driver, details)
    elif (details['status'] == 'invite' and details['type'] == 'email'):
        setting_email_invite(driver)
        time.sleep(1)
        activity_summary(driver, details)
    elif (details['status'] == 'member' and details['type'] == 'email'):
        setting_email_member(driver)
    elif (details['status'] == 'offline' and details['type'] == 'mobile'):
        setting_offline_touch(driver)

    #time.sleep(5)
    activity_checkOut(driver,details)

def emergency_details_autofetch(driver,walkin_details):

    emer_name = WebDriverWait(driver, 20, poll_frequency=0.005).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Emergencycontactname')))
    name = emer_name.text
    print(name)
    assert name == walkin_details['Emergency_contact_name']
    #time.sleep(2)
    emer_phone =WebDriverWait(driver, 20, poll_frequency=0.005).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Emergencycontact')))
    phone = emer_phone.text
    print(phone)
    assert phone == walkin_details['Emergency_contact']

def activity_summary(driver,details):
    e = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID, 'Activity_summary')))
    statuss=e.is_displayed()
    if(statuss):
        print("activity_summary_screen_displayed")
        time.sleep(0.5)
        if(details['status'] == 'walkin' and details['type'] == 'mobile'):
            element1 = WebDriverWait(driver, 10, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'TOM')))
            time.sleep(0.5)
            texts = element1.text
            if (texts == details['Emergency_contact_name']):
                print("Right user check-in")
                assert True
            else:
                assert False

        elif(details['status'] == 'walkin' and details['type'] == 'email'):
            element1 = WebDriverWait(driver, 10, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'RAM')))
            time.sleep(0.5)
            texts = element1.text
            if (texts == details['Emergency_contact_name']):
                print("Right user check-in")
                assert True
            else:
                assert False

        elif (details['status'] == 'invite' and details['type'] == 'mobile'):
            element1 = WebDriverWait(driver, 10, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.XPATH, '(//android.widget.TextView[@content-desc="invite"])[2]')))
            time.sleep(0.5)
            texts = element1.text
            if (texts == details['firstname']):
                print("Right user check-in")
                assert True
            else:
                assert False

        elif (details['status'] == 'invite' and details['type'] == 'email'):
            element1 = WebDriverWait(driver, 10, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.XPATH, '	(//android.widget.TextView[@content-desc="invemail"])[2]')))
            time.sleep(0.5)
            texts = element1.text
            if (texts == details['firstname']):
                print("Right user check-in")
                assert True
            else:
                assert False

        Next(driver)
    else:
        print("Activity summary screen not displayed")
        assert False

def general_activity_dropdown(driver):
    try:
        useraction = TouchAction(driver)
        e = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH, '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[1]/android.view.ViewGroup')))
        e.click()
        el = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")))
        el.click()
        e2 = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,'(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup')))
        e2.click()
        e3 = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,                                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]')))
        e3.click()

        """
        time.sleep(4)
        #useraction.tap(172, 196).perform()
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
        #	(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup
        time.sleep(3)
        g=driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup')
        #g = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH, '(//android.view.ViewGroup[@content-desc="dropdownFormComponentField"])[2]/android.view.ViewGroup')))
        g.click()
        time.sleep(4)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]').click()
        #useraction.tap(270, 196).perform()
        """
    except:
        print("Unable to select dropdown field")
        time.sleep(0.5)
        #e=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button').click()
        #e.click()
        raise

def logout(driver):
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settingsButton")))
    settings.click()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Authorization Code")))
    settings.send_keys("1")
    driver.hide_keyboard()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settings")))
    settings.click()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                  '//android.view.ViewGroup[@content-desc="logOutTerminal"]/android.view.ViewGroup/android.view.ViewGroup')))
    settings.click()
    c = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ID, "android:id/button1")))
    c.click()
def late_tracking(driver):
    c = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Late_Tracking")))
    c.click()
def offline_mode(driver):
    status = "offline"
    settings = WebDriverWait(driver, 15, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="settingsButton "]/android.widget.ImageView')))
    settings.click()
    code = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Authorization Code")))
    code.send_keys("1")
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "settings")))
    settings.click()
    settings = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "switchToOfflineMode")))
    settings.click()
    done = WebDriverWait(driver, 5, poll_frequency=0.5).until(
        EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Done")))
    done.click()
    time.sleep(0.5)
    driver.toggle_wifi()
def statusOftest(status_test,driver):
    if (status_test == False):
        print("test case failed")
        a = WebDriverWait(driver, 10, poll_frequency=0.5).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Cancel')))
        a.click()
        time.sleep(1)
        assert True
    else:
        print("test case passed")