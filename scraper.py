from genericpath import isfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import isdir
from os import mkdir

#final_string = string + " IMAGES"
class Webscraper:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument
        self.driver = webdriver.Chrome()
        

    def getinputarea(self):
        search_area = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        return search_area

    def search_string(self, data):
        self.data = data
        if not isdir(f"tmp/{self.data}"):
            mkdir("tmp/"+self.data)

        self.driver.get(f'https://www.google.com/search?channel=fs&source=univ&tbm=isch&q={data}')

    def get_images_button(self):
        img_button = '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]'
        #//*[@id="iur"]/div[2]/div/div/div[1]/a/g-img/div
        return img_button
        
    def click_img_button(self):
        img_click = self.get_images_button()
        self.driver.find_element_by_xpath(xpath=img_click).click()

    def after_click_image_loc(self):
        img_location = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img'
        return img_location

    def screenshot_image(self,img_num):
        img_ss = self.after_click_image_loc()
        self.driver.find_element_by_xpath(xpath=img_ss).screenshot(f'tmp/{self.data}/{self.data + img_num}.png')
        return f'tmp/{self.data}/{self.data + img_num}.png'

    def get_next_button(self):
        next_button = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[3]'
        return next_button

    def click_next_button(self):
        next_button_loc = self.get_next_button()
        self.driver.find_element_by_xpath(xpath=next_button_loc).click()


    def close(self):
        self.driver.close()