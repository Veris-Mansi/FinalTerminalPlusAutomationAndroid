import os
os.chdir("C:\\Users\\veris\\PycharmProjects\\Terminal+ new release testing - 11\\pytestpackage")

os.system("adb kill-server")
os.system("adb start-server")
os.system("adb devices")
#os.system('adb -s fc378d12 shell pm clear com.veristerminal')#os.system("pytest -v -s --html=report.html --self-contained-html test_conftest_Alltestcases.py")
os.system("pytest -v -s --html=report.html --self-contained-html test_conftest_offlinemode.py")
#os.system("pytest -v -s --html=report.html --self-contained-html test_conftest_Allcheckout.py")
#os.system("pytest -v -s --html=report.html --self-contained-html test_conftest_emailTestcases.py")
#pytest -v -s --html=report.html --self-contained-html test_conftest_Allcheckout.py
#os.system("pytest -v -s --html=report.html --self-contained-html test_conftest_Multiplecheckins.py")