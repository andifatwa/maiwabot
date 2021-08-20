import selenium
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(5)

sleep(2)

driver.get("https://berita.maiwanews.com/")

a = 1
b = 0

while a == 1:

    sleep(3)

    baca = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/section/div[1]/div/ul/li[4]/article/h2/a")
    baca.click()
    b += 1
    print("sudah mengunjungi page sebanyak:", b)

    sleep(3)
    
    

    baca2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/main/article/div[2]/div[5]/a[1]/font")
    baca2.click()
    b += 1
    print("sudah mengunjungi page sebanyak:", b)

    sleep (3)

    baca3 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/main/article/div[2]/div[5]/a[2]/font")
    baca3.click()
    b += 1
    print("sudah mengunjungi page sebanyak:", b)

    sleep(3)

    baca4 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/main/article/div[2]/div[2]/a[3]/font")
    baca4.click()
    b += 1
    print("sudah mengunjungi page sebanyak:", b)

    sleep(3)

    baca5 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/main/article/div[2]/div[2]/a[4]/font")
    baca5.click()
    b += 1
    print("sudah mengunjungi page sebanyak:", b)

    sleep(3)

    baca6 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/main/article/div[2]/div[2]/a[5]/font")
    baca6.click()
    b += 1
    print("sudah mengunjungi page sebanyak:", b)

    sleep(3)

    driver.get("https://berita.maiwanews.com/")

    sleep(2)