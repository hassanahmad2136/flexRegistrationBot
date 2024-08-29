from initdriver import get_driver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import pyautogui as pg

driver = get_driver()

url = "https://flexstudent.nu.edu.pk/"
driver.get(url)
time.sleep(5)
cookies = driver.get_cookies()

for cookie in cookies:
    if cookie["name"] == "ASP.NET_SessionId":

        cookie["value"] = "REPLACE" 

        driver.delete_cookie(cookie["name"])

        driver.add_cookie(cookie)
        break

url = "https://flexstudent.nu.edu.pk/Student/StudentAttendance"
driver.execute_script(f"window.location.href='{url}'")

while len(driver.find_elements(By.XPATH, "//a[contains(@href, '/Student/CourseRegistration')]")) == 0:
    pass
driver.find_element(By.XPATH, "//a[contains(@href, '/Student/CourseRegistration')]").click()
while "CourseRegistration" not in driver.current_url:
    pass
time.sleep(1)
print(driver.page_source)
print("Checking Now...")

while len(driver.find_elements(By.TAG_NAME, "input")) == 0: # waiting for registration to open
    time.sleep(3)
    driver.refresh()

print("Registration is Open")
while len(driver.find_elements(By.TAG_NAME, "tr")) == 0: pass
courses = driver.find_elements(By.TAG_NAME, "tr")
for course in courses:
    if "Digital Image Processing" in course.text:
        select_element = course.find_elements(By.TAG_NAME, "select")
        select = Select(select_element[0])
        try:
            select.select_by_index(0)
        except:
            pass
        driver.execute_script("arguments[0].click();",course.find_elements(By.TAG_NAME, "input")[0])
driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH,"//button[@id='submit' and contains(text(), 'Register Courses')]"))

while True:
    try:
        alert = Alert(driver)
        alert_text = alert.text
        print(f"Alert detected: {alert_text}")
        alert.accept()  
        break
    except:
        print("No alert present, breaking the loop.")
