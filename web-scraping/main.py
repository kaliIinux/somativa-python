from selenium import webdriver
import time 
from db import Database


db = Database()
class MagazineLuiza:
    def __init__(self) -> None:
        self.site_link = 'https://www.magazineluiza.com.br/'
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.maximize_window()
        
    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.site_link)
        time.sleep(1)
        
    def nav(self, pesquisa):
        self.input = self.driver.find_element('tag name', 'input')
        self.input.send_keys(pesquisa)
        time.sleep(1)
        self.input.submit()
        time.sleep(2)
        self.driver.refresh()
        
    def modelo_celular(self, marca):
        lista = self.driver.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul')
        celulares = lista.text
        celulares = celulares.split("\n")
        count = 0
        
        preco = lista.text
        preco = preco.split(marca)
        for celular in celulares:
            if marca in celular:
                if count == 10:
                    break
                else:
                    print(celular)
                    db.insert_into_table(modelo=celular.replace('"', '').replace("'", ''), marca=marca)
                    count += 1
        self.abrir_site()
        print()
    
        
    def precos(self, marca):
        lista = self.driver.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul')
        precos = lista.text
        precos = precos.split(marca)
        count = 1
        
        for preco in precos:
            preco = preco.split("R$")
            if count == 10:
                break
            else:
                try:
                    p = preco[2].split("\n")
                    print(p[0][0:8])
                    db.insert_price(preco=p[0][0:8])
                    count += 1 
                except:
                    print("")
        time.sleep(1)
        self.abrir_site()
    
    def web(self):
        self.abrir_site()
        self.nav("celular nokia")
        self.modelo_celular(marca="Nokia")
        self.nav("celular nokia")
        self.precos(marca="Nokia")
        
        self.nav("iphone")
        self.modelo_celular(marca="Apple")
        self.nav("iphone")
        self.precos(marca='Iphone')
        
        """
        self.nav('celular samsung')
        self.modelo_celular(marca="Samsung")
        
        self.nav("celular motorola")
        self.modelo_celular(marca="Motorola")
        
        self.nav("celular xiaomi")
        self.modelo_celular(marca="Xiaomi")
        """
        
site = MagazineLuiza()
db.remove_table()
db.create_table()
site.web()







