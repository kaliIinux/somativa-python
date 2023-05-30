from selenium import webdriver
import time 
from db import Database


db = Database()
class MagazineLuiza:
    def __init__(self) -> None:
        self.site_link = 'https://www.magazineluiza.com.br/'
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.minimize_window()
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
        self.lista_modelo = []
        
        preco = lista.text
        preco = preco.split(marca)
        for celular in celulares:
            if marca in celular:
                if count == 10:
                    break
                else:
                    print(celular.replace('"', '').replace("'", ''))
                    celular = celular.replace('"', '').replace("'", '')
                    self.lista_modelo.append(celular)
                    count += 1
        self.abrir_site()
        print()
    
        
    def precos(self, marca):
        lista = self.driver.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul')
        precos = lista.text
        precos = precos.split(marca)
        count = 0
        self.lista_preco = []
        
        for preco in precos:
            preco = preco.split("R$")
            if count == 10:
                break
            else:
                try:
                    p = preco[2].split("\n")
                    self.lista_preco.append(p[0][0:8])
                    print(p[0][0:8])
                    count += 1 
                except:
                    print("")
                    
        
        print(self.lista_preco)
        time.sleep(1)
        self.abrir_site()
        
    def web(self):
        
        db.remove_table()
        db.create_table()
        
        self.abrir_site()
        
        self.nav('celular nokia')
        self.modelo_celular(marca="Nokia")
        self.nav('celular nokia')
        self.precos(marca='Nokia')
        db.insert_into_table(modelo=self.lista_modelo, marca='Nokia', preco= self.lista_preco)
        self.lista_modelo.clear()
        self.lista_preco.clear()
        
        self.nav('celular samsung')
        self.modelo_celular(marca="Samsung")
        self.nav('celular samsung')
        self.precos(marca='Samsung')
        db.insert_into_table(modelo=self.lista_modelo, marca='Samsung', preco= self.lista_preco)
        self.lista_modelo.clear()
        self.lista_preco.clear()
        
        self.nav("celular motorola")
        self.modelo_celular(marca="Motorola")
        self.nav("celular motorola")
        self.precos(marca='Motorola')
        db.insert_into_table(modelo=self.lista_modelo, marca='Motorola', preco= self.lista_preco)
        self.lista_modelo.clear()
        self.lista_preco.clear()
        
        self.nav("celular xiaomi")
        self.modelo_celular(marca="Xiaomi")
        self.nav("celular xiaomi")
        self.precos(marca='Xiaomi')
        db.insert_into_table(modelo=self.lista_modelo, marca='Xiaomi', preco= self.lista_preco)
        self.lista_modelo.clear()
        self.lista_preco.clear()
        
        self.nav("celular lg")
        self.modelo_celular(marca="LG")
        self.nav("celular lg")
        self.precos(marca='LG')
        db.insert_into_table(modelo=self.lista_modelo, marca='LG', preco= self.lista_preco)
        self.lista_modelo.clear()
        self.lista_preco.clear()







