import time
import pyautogui as pag
import pyscreeze
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


class Licensereport:
  def __init__(self):
      pass
# This Function is used to Read Data From Information.txt file
  def readConfiguration(self):
      configParser = ConfigParser(interpolation=None)
      configParser.read('G:/Huawei_Automations/Config/iMaster-NCE-Credentials.ini')
      self.f_username = configParser.get('NCE', 'Username')
      self.f_password = configParser.get('NCE', 'Password')
      self.f_url = configParser.get('NCE', 'Url')

# This function is used to load and install chrome driver and click on Advance button and Ip before login page
  def chromeconfig(self):
      options = webdriver.ChromeOptions()
      options.add_experimental_option("detach", True)

      self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
      self.driver.get(self.f_url)
      self.driver.maximize_window()
      time.sleep(2)
      advance = self.driver.find_element_by_xpath('//*[@id="details-button"]')
      advance.click()
      time.sleep(1)
      ip = self.driver.find_element_by_xpath('//*[@id="proceed-link"]')
      ip.click()
      time.sleep(2)

# This Function is used to get username and password from readtextfile() function and complete login & after login click agree button
  def login(self):
      username = self.driver.find_element_by_xpath('//*[@id="username"]')
      username.send_keys(self.f_username)
      time.sleep(2)
      pin = self.driver.find_element_by_xpath('//*[@id="value"]')
      pin.send_keys(self.f_password)

      btn = self.driver.find_element_by_xpath('//*[@id="submitDataverify"]')
      btn.click()

      time.sleep(5)
      agree = self.driver.find_element_by_xpath('//*[@id="login_warn_confirm"]')
      agree.click()
      time.sleep(2)



# This windowhandeler function is not necessary just for testing
  def windowhandeler(self):
      windows_1 = self.driver.current_window_handle
      print(" => Titale  %s: ", windows_1.title())

# This Function is used to click network management area
  def networkManagement(self):
      networkManagement = self.driver.find_element_by_xpath('//*[@id="appComContainer_U2020-F_U2000_App"]/div[2]')
      networkManagement.click()
      time.sleep(15)

# This Function is used for window switching (Here used for Resource & Inventory Report)
  def windowswitching(self):
      windows_list = self.driver.window_handles
      win_index = 1
      try:
          print("Activating window ", windows_list[win_index].title(), "Total Count ", len(windows_list))
          self.driver.switch_to.window(self.driver.window_handles[win_index])
      except IndexError:
          print("Error : ", IndexError)


# This Function is used for click resource option then click Inventory Report and switch Iframe and click microwave_report, microwave_license_capacity_report area
  def stepofMicrowavelicenseCapacityReport(self):

      resource = self.driver.find_element_by_xpath('//*[@id="refr.mm.U2020-F_U2000_App.U2020-F_Resource"]/span')
      resource.click()
      time.sleep(20)
      inventory_report = self.driver.find_element_by_xpath("//span[@id='action-0-0']/span[2]")
      inventory_report.click()
      time.sleep(10)

      iframe = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[2]/iframe')
      self.driver.switch_to.frame(iframe)

      microwave_report = self.driver.find_element_by_xpath("//div[@id='ev_PanelItem_10002']/div/span[2]")
      microwave_report.click()

      time.sleep(5)

      microwave_license_capacity_report = self.driver.find_element_by_xpath(
          "//div[@id='ev_PanelItem_10002']/div[2]/div/div[2]/div/div/div[2]")
      microwave_license_capacity_report.click()


# This Function is used for the download page
  def downloadNetworkWideLicenseReport(self):

      time.sleep(3)
      # It has used for arrow
      #pag.doubleClick(196, 200)  # arrow
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('tab')
      pag.press('enter')




      # time.sleep(3)
      # pag.click(8, 250)
      # time.sleep(3)
      # pag.click(8, 290)
      # time.sleep(3)
      # pag.click(28, 310)
      # time.sleep(3)
      # ##pag.click(68, 320)
      # pag.click(68, 250)

      # time.sleep(3)
      # pag.doubleClick(196, 200)  # arrow
      #
      # time.sleep(5)


# After loading all data on grid then execute this image

      dialogbox = pag.locateOnScreen(
          "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_blueicon.png",
          grayscale=True, confidence=.9)
      while dialogbox == None:

          dialogbox = pag.locateOnScreen(
              "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_blueicon.png",
              grayscale=True, confidence=.9)
          if (dialogbox != None):
              pag.click(pag.center(dialogbox))
              break;
          time.sleep(3)
      pag.click(pag.center(dialogbox))
      pag.press('tab')
      pag.press('tab')
      pag.press('space')
# This is additionaly add for green icon
      time.sleep(5)
      pag.press('tab')
      pag.press('space')

# This image is use to click  (Detailed Report of Network Wide License) Tab
      time.sleep(5)
      # --- for detect tab
      tab = pag.locateOnScreen(
          "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_tab1.png",
          grayscale=True, confidence=.9)
      while tab == None:

          tab = pag.locateOnScreen(
              "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_tab1.png",
              grayscale=True, confidence=.9)
          print("reload")
          if (tab != None):
              pag.click(pag.center(tab))
              print("detect tab")

              break;
          time.sleep(3)
      pag.click(pag.center(tab))
      print("done")
# This key is used to move on save as button
      pag.hotkey('ctrl', 'end')

      time.sleep(3)

#--- for detect save button
      save = pag.locateOnScreen(
          "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_save.png",
          grayscale=True, confidence=.9)
      while save == None:

          save = pag.locateOnScreen(
              "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_save.png",
              grayscale=True, confidence=.9)
          if (save != None):
              pag.click(pag.center(save))
              break;
          time.sleep(3)
      pag.click(pag.center(save))

#--- for detect After save button
      afsave = pag.locateOnScreen(
          "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_lssave.png",
          grayscale=True, confidence=.9)
      while afsave == None:

          afsave = pag.locateOnScreen(
              "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_lssave.png",
              grayscale=True, confidence=.9)
          if (afsave != None):
              pag.click(pag.center(afsave))
              print("detect")
              break;
          time.sleep(3)
      pag.click(pag.center(afsave))
      pag.press('tab')
      time.sleep(1)
      pag.press('tab')
      time.sleep(1)
      pag.press('tab')
      time.sleep(3)
      pag.press('enter')

      time.sleep(3)
# for last pop up and press yes button
      pag.press('tab')
      time.sleep(2)
      pag.press('enter')
      time.sleep(40)




  def logout(self):
      time.sleep(10)
      logouticon = pag.locateOnScreen(
          "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_1logout.png",
          grayscale=True, confidence=.9)
      while logouticon == None:

          logouticon = pag.locateOnScreen(
              "G:\\RAT-Automation-src\\Network_Wide_License\\images\\rsz_1logout.png",
              grayscale=True, confidence=.9)
          if (logouticon != None):
              pag.click(pag.center(logouticon))
              break;
          time.sleep(3)
      pag.click(pag.center(logouticon))
      pag.press('enter')
      pag.press('enter')
      pag.press('tab')
      pag.press('enter')
      time.sleep(5)
      self.driver.quit()

  def exitApp(self):
      self.driver.quit()






