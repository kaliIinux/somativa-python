from selenium import webdriver
import time 


class MagazineLuiza:
    def __init__(self) -> None:
        self.site_link = 'https://www.magazineluiza.com.br/'
        self.site_map = {}
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.maximize_window()
        
    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.site_link)
        time.sleep(1)
        
    def nav(self):
        self.input = self.driver.find_element('tag name', 'input')
        self.input.send_keys("celular samsung")
        time.sleep(1)
        self.input.submit()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(1000000)
        
    def samsung(self):
        lista = self.driver.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul/')
        celulares = lista.text
        celulares = celulares.split("\n")
        count = 0

        for celular in celulares:
            if "Smartphone" in celular:
                if count == 10:
                    break
                else:
                    print(celular)
                    count += 1  
                    
        time.sleep(1000000)
        
site = MagazineLuiza()
site.abrir_site()
site.nav()