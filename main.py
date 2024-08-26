from initdriver import get_driver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import pyautogui as pg

driver = get_driver()

url = "https://flexstudent.nu.edu.pk/"
driver.get(url)
time.sleep(50)
print("Checking Now...")
while len(driver.find_elements(By.TAG_NAME, "input")) == 0:
    pg.click()
    time.sleep(1)

    driver.refresh()

print("here")
while len(driver.find_elements(By.TAG_NAME, "tr")) == 0: pass
courses = driver.find_elements(By.TAG_NAME, "tr")
print(len(courses))
i = 0
for course in courses:
    print(i)
    i+=1
    if "Computer Vision" in course.text:
        select_element = course.find_elements(By.TAG_NAME, "select")
        select = Select(select_element[0])
        try:
            select.select_by_index(0)
        except:
            pass
        driver.execute_script("arguments[0].click();",course.find_elements(By.TAG_NAME, "input")[0])
driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH,"//button[@id='submit' and contains(text(), 'Register Courses')]"))
time.sleep(2)
try:
    alert = Alert(driver)
    alert_text = alert.text  # You can capture the text if needed
    print(f"Alert detected: {alert_text}")
    alert.accept()  # Or use alert.dismiss() to dismiss the alert
except:
    print("No alert present")



