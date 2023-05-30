import mysql.connector

class Database:
    def __init__(self) -> None:
        self.__conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='database')
        self.__cursor = self.__conexao.cursor()
    
    def create_table(self):
        self.__cursor.execute("""CREATE TABLE `celulares` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`modelo` VARCHAR(150) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`marca` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	`preco` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_unicode_ci',
	PRIMARY KEY (`id`) USING BTREE
    )
    COLLATE='utf8mb4_unicode_ci'
    ENGINE=InnoDB
    AUTO_INCREMENT=1
    ;""")
        self.__conexao.commit()
        
    def insert_into_table(self, modelo, marca, preco):
        for i in range (10):
            self.__cursor.execute(f'INSERT INTO celulares (modelo, marca, preco) VALUES ("{modelo[i]}", "{marca}", "R${preco[i]}");')
            self.__conexao.commit()
        
    def insert_price(self, preco, id, lista):
        for i in lista:
            self.__cursor.execute(f'UPDATE celulares SET preco = "{preco[i]}" WHERE id = "{id[i]}"')
            self.__conexao.commit()
    
    def remove_table(self):
        self.__cursor.execute('DROP TABLE celulares')
        self.__conexao.commit()
    
    def get_products(self, marca):
        self.__cursor.execute(f'SELECT * FROM celulares where marca = "{marca}"')
        products = self.__cursor.fetchall()
        return products
    
    def get_all(self):
        self.__cursor.execute(f'SELECT * FROM celulares')
        linhas = self.__cursor.fetchall()
        return linhas





        

        