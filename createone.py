import time
from selenium import webdriver
import pandas as pd
    
driver=webdriver.Chrome()
driver.get("https://adc3-zeam-fa-ext.oracledemos.com/")
#login
time.sleep(10)
driver.find_element_by_xpath("//*[@id='userid']").send_keys("hcm_impl")
driver.find_element_by_xpath("//*[@id='password']").send_keys("PTH36854")
driver.find_element_by_xpath("//*[@id='btnActive']").click()
time.sleep(10)
    
#excel sheet extraction
file_data=pd.ExcelFile("namessheet.xlsx")
final_data=file_data.parse("Sheet1")
username=final_data['Name'][0]
entities=final_data['Entity'][0]
addr1=final_data['Address1'][0]
town=final_data['City'][0]
busunit=final_data['Business_unit'][0]
time.sleep(10)
    
#Oracle web-site
    
driver.find_element_by_xpath("//*[@id='pt1:_UISmmLink::icon']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='pt1:_UISnvr:0:nvgpgl2_groupNode_workforce_management']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='pt1:_UISnvr:0:nv_itemNode_workforce_management_new_person']/span").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:_FOTsdiAddCwkDefaultRegional::icon']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:_FOTRaT:0:RAtl1']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:0:pt1:SP1:NewPe1:0:pt_r1:0:r1:0:i1:0:it20::content']").send_keys(username)
time.sleep(10)
    
#step1-Identification
    
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:0:pt1:SP1:selectOneChoice3::content']").send_keys(entities)
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:0:pt1:SP1:selectOneChoice3::su0']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:0:pt1:SP1:tt1:next']/a/span/span").click()
time.sleep(10)
    
#step2-personal information
    
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:1:pt1:SP1:Perso2:0:Perso1:0:Maint1:0:i1:0:inputText17::content']").send_keys(addr1)
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:1:pt1:SP1:Perso2:0:Perso1:0:Maint1:0:i1:3:inputText21::content']").send_keys(town)
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:1:pt1:SP1:tt1:next']/a/span").click()
time.sleep(10)
    
#step3-employment information
    
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:2:pt1:sP2:NewPe3:0:NewPe1:0:businessUnitId::content']").send_keys(busunit)
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:2:pt1:sP2:tt1:next']/a").click()
time.sleep(10)
    
#step4-compensation
    
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:3:pt1:SP1:tt1:next']/a").click()
time.sleep(10)
    
#step5-preview
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:4:pt1:AP1:tt1:submit']/a").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:4:pt1:AP1:tt1:okWarningDialog']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='_FOpt1:_FOr1:0:_FONSr2:0:MAnt2:1:pt1:pt_r1:4:pt1:AP1:tt1:okConfirmationDialog']").click()
time.sleep(10)
    
    





