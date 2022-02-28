from functionNetworkWideLicense import Licensereport
from TrayIcon import Tray
licensereport = Licensereport()

#Tray Icon Started
tray = Tray()
mainObject = tray.initializeSystray()
mainObject.start()

print("Reading Configuration File")
licensereport.readConfiguration()
print("Browser Init")
licensereport.chromeconfig()
print("Entering Credentials")
licensereport.login()
print("Close Popup Windows")
licensereport.windowhandeler()
print("Network Management")
licensereport.networkManagement()
print("Switching Window")
licensereport.windowswitching()
print("Microwave License Capacity Report")
licensereport.stepofMicrowavelicenseCapacityReport()
print("Downloading Network Wide License Report")
licensereport.downloadNetworkWideLicenseReport()
print("Logout")
licensereport.logout()
print("Closing the Automation")
licensereport.exitApp()























# ---------------------------================== Raw Code (That's  not necessary for automation) ==================------------------------------------
# import time
# import pyautogui as pag
# import pyscreeze
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType
#
# import pyscreeze
# from PIL import Image
# import cv2
# from tkinter import messagebox
#
# with open('information.txt', 'r') as f:
#     url = f.readline()
#     f_url = url[4:]
#     print(f_url)
#
#     username = f.readline()
#     f_username = username[9:]
#     print(f_username)
#
#     password = f.readline()
#     f_password = password[9:]
#     print(f_password)
#
#
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver.get(f_url)
# driver.maximize_window()
# time.sleep(2)
# advance = driver.find_element_by_xpath('//*[@id="details-button"]')
# advance.click()
# time.sleep(1)
# ip = driver.find_element_by_xpath('//*[@id="proceed-link"]')
# ip.click()
# time.sleep(2)
# username = driver.find_element_by_xpath('//*[@id="username"]')
# username.send_keys(f_username)
# time.sleep(2)
# pin = driver.find_element_by_xpath('//*[@id="value"]')
# pin.send_keys(f_password)
#
# btn = driver.find_element_by_xpath('//*[@id="submitDataverify"]')
# btn.click()
#
# time.sleep(5)
# agree = driver.find_element_by_xpath('//*[@id="login_warn_confirm"]')
# agree.click()
# time.sleep(2)
#
#
# print("Login Completed")
#
# windows_1 = driver.current_window_handle
# print(" => Titale  %s: ", windows_1.title())
#
# networkManagement = driver.find_element_by_xpath('//*[@id="appComContainer_U2020-F_U2000_App"]/div[2]')
# networkManagement.click()
# time.sleep(15)
#
# # vai
# windows_list = driver.window_handles
# win_index = 1
# try:
#     print("Activating window ", windows_list[win_index].title(), "Total Count ", len(windows_list))
#     driver.switch_to.window(driver.window_handles[win_index])
# except IndexError:
#     print("Error : ", IndexError)
#
#
# resource = driver.find_element_by_xpath('//*[@id="refr.mm.U2020-F_U2000_App.U2020-F_Resource"]/span')
# resource.click()
#
# time.sleep(30)
#
# inventory_report = driver.find_element_by_xpath("//span[@id='action-0-0']/span[2]")
# inventory_report.click()
#
#
# time.sleep(10)
#
#
# iframe = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[2]/iframe')
# driver.switch_to.frame(iframe)
#
# microwave_report = driver.find_element_by_xpath("//div[@id='ev_PanelItem_10002']/div/span[2]")
# microwave_report.click()
#
# time.sleep(5)
#
# microwave_license_capacity_report = driver.find_element_by_xpath("//div[@id='ev_PanelItem_10002']/div[2]/div/div[2]/div/div/div[2]")
# microwave_license_capacity_report.click()
#
# # ----------------------------------------------==========================================--------------------
# time.sleep(3)
# pag.click(8,250)
# time.sleep(3)
# pag.click(8,290)
# time.sleep(3)
# pag.click(28,310)
# time.sleep(3)
# pag.click(68,320)
# time.sleep(3)
# pag.doubleClick(196,200)     #arrow
#
# time.sleep(5)
#
# dialogbox = pag.locateOnScreen(
#     "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_result.png",
#     grayscale=True, confidence=.9)
# while dialogbox == None:
#
#     dialogbox = pag.locateOnScreen(
#         "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_result.png",
#         grayscale=True, confidence=.9)
#     if(dialogbox != None ):
#         pag.click(pag.center(dialogbox))
#         break;
#     time.sleep(3)
# pag.click(pag.center(dialogbox))
# pag.press('tab')
# pag.press('space')
#
# time.sleep(5)
# # --- for detect tab
# tab = pag.locateOnScreen(
#     "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_tab1.png",
#     grayscale=True, confidence=.9)
# while tab == None:
#
#     tab = pag.locateOnScreen(
#         "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_tab1.png",
#         grayscale=True, confidence=.9)
#     print("reload")
#     if(tab != None ):
#         pag.click(pag.center(tab))
#         print("detect tab")
#
#         break;
#     time.sleep(3)
# pag.click(pag.center(tab))
# print("done")
# pag.hotkey('ctrl', 'end')
#
# time.sleep(3)
#
# # #--- for detect save button
# save = pag.locateOnScreen(
#     "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_save.png",
#     grayscale=True, confidence=.9)
# while save == None:
#
#     save = pag.locateOnScreen(
#         "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_save.png",
#         grayscale=True, confidence=.9)
#     if(save != None ):
#         pag.click(pag.center(save))
#         break;
#     time.sleep(3)
# pag.click(pag.center(save))
#
# # #--- for detect After save button
# afsave = pag.locateOnScreen(
#     "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_lssave.png",
#     grayscale=True, confidence=.9)
# while afsave == None:
#
#     afsave = pag.locateOnScreen(
#         "G:\\RAT-Automation-src\\Network_Wide_License\\rsz_lssave.png",
#         grayscale=True, confidence=.9)
#     if(afsave != None ):
#         pag.click(pag.center(afsave))
#         print ("detect")
#         break;
#     time.sleep(3)
# pag.click(pag.center(afsave))
# pag.press('tab')
# time.sleep(1)
# pag.press('tab')
# time.sleep(1)
# pag.press('tab')
# time.sleep(3)
# pag.press('enter')
#
# time.sleep(5)
# # # last yes
# pag.press('tab')
# pag.press('enter')

