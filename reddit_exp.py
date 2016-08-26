from selenium import webdriver
import time
import subprocess
import os
# Driver support
# Firefox Version(Recommended)
driver = webdriver.Firefox()
# Below is the Chrome Version
# ***********************************************************************
# System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
# WebDriver driver = new ChromeDriver();c

website = driver.get("https://www.reddit.com/")
# Assignments
uname = driver.find_element_by_name("user")
pword = driver.find_element_by_name("passwd")
button = driver.find_element_by_class_name("btn")

time.sleep(0.5)
# Username and Password Input (Your own information)
uname.send_keys("YOURUSERNAMEHERE")
pword.send_keys("YOURPASSWORDHERE")


time.sleep(0.3)
button.click()
# Pinging Process (for my own personal reason)
with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 200):
                ip="".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                	time.sleep(2)
                        print ip, "inactive"
                else:
                	time.sleep(2)
                        print ip, "active"
