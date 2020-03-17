#this code does the login function

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep

Notliked = "M34.3 3.5C27.2 3.5 24 8.8 24 8.8s-3.2-5.3-10.3-5.3C6.4 3.5.5 9.9.5 17.8s6.1 12.4 12.2 17.8c9.2 8.2 9.8 8.9 11.3 8.9s2.1-.7 11.3-8.9c6.2-5.5 12.2-10 12.2-17.8 0-7.9-5.9-14.3-13.2-14.3zm-1 29.8c-5.4 4.8-8.3 7.5-9.3 8.1-1-.7-4.6-3.9-9.3-8.1-5.5-4.9-11.2-9-11.2-15.6 0-6.2 4.6-11.3 10.2-11.3 4.1 0 6.3 2 7.9 4.2 3.6 5.1 1.2 5.1 4.8 0 1.6-2.2 3.8-4.2 7.9-4.2 5.6 0 10.2 5.1 10.2 11.3 0 6.7-5.7 10.8-11.2 15.6z"
liked = "M35.3 35.6c-9.2 8.2-9.8 8.9-11.3 8.9s-2.1-.7-11.3-8.9C6.5 30.1.5 25.6.5 17.8.5 9.9 6.4 3.5 13.7 3.5 20.8 3.5 24 8.8 24 8.8s3.2-5.3 10.3-5.3c7.3 0 13.2 6.4 13.2 14.3 0 7.8-6.1 12.3-12.2 17.8z"

#binary = FirefoxBinary(r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')
#driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver\\geckodriver.exe')

class InstragramBot:
	def __init__(self, username, password):
		#Login
		self.username = username
		self.driver = webdriver.Firefox()
		self.driver.get("https://instagram.com")
		sleep(5)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		sleep(5)
		#Close Pop-Up
		self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()

	def TagSearch(self, tag):
		#Go to explorer page
		self.driver.get("https://www.instagram.com/explore/tags/"+tag+"/")
		sleep(1)

	def Like(self):
		#open the first photo
		self.driver.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]').click()
		sleep(2)

		#like
	
		while True:
			try:
				like = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
				sleep(2)
				next = self.driver.find_element_by_xpath("//a[text()=\"Próximo\"]").click()
				sleep(2)
			except:
				print("erro")
				next = self.driver.find_element_by_xpath("//a[text()=\"Próximo\"]").click()
				sleep(2)

MyBot = InstragramBot('<username>', '<password>')
MyBot.TagSearch('pizza')
MyBot.Like()
