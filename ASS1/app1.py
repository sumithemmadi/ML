from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://twitter.com/imVkohli')

time.sleep(10)
name = driver.find_element(By.CSS_SELECTOR, "div.r-adyw6z:nth-child(1) > span:nth-child(1) > span:nth-child(1)").text
following = driver.find_element(By.CSS_SELECTOR, ".r-1mf7evn > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)").text
followers = driver.find_element(By.CSS_SELECTOR, "div.r-13awgt0:nth-child(5) > div:nth-child(2) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)").text
no_tweets = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div").text
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

print(name)
print(following)
print(followers)
print(no_tweets)

# posts = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section")

retwites = []

# for i in range(1,3):
#     x_path = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div["+str(1)+"]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span/span"
#     print(x_path)
#     retwites_count = driver.find_element(By.XPATH,x_path).text
#  /html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span
#  /html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[2]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span
# /html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[{}]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span/span
# /html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/span/span/span
    # print(retwites_count)

# print(posts)