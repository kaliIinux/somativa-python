from selenium import webdriver
import time 


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
        
    def nome_celular(self, marca):
        lista = self.driver.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul')
        celulares = lista.text
        celulares = celulares.split("\n")
        count = 0

        for celular in celulares:
            if marca in celular:
                if count == 10:
                    break
                else:
                    print(celular)
                    count += 1  
        print()
        
    def precos(self):
        lista = self.driver.find_element('xpath', '/html/body/div[1]/div/main/section[4]/div[3]/div/ul')
        precos = lista.text
        precos = precos.split("Smartphone")
        count = 0
        
        for preco in precos:
            preco = preco.split("R$")
            if count == 10:
                break
            else:
                try:
                    p = preco[2].split("\n")
                    print(p[0][0:8])
                    count += 1 
                except:
                    print("")
        
site = MagazineLuiza()

site.abrir_site()
site.nav("celular nokia")
site.nome_celular(marca="Nokia")
site.abrir_site()
site.nav("iphone")
site.nome_celular(marca="Apple")
site.abrir_site()
site.nav('celular samsung')
site.nome_celular(marca="Samsung")
site.abrir_site()
site.nav("celular motorola")
site.nome_celular(marca="Motorola")
site.abrir_site()
site.nav("celular xiaomi")
site.nome_celular(marca="Xiaomi")