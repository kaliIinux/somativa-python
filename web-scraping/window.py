from tkinter import *
from tkinter import ttk
from db import Database


window = Tk()

class Aplication():

    def __init__(self):
        self.window = window
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        
        window.mainloop()
    
    def tela(self):
        self.window.title("Cadastro de clientes")
        self.window.configure(background= "white")
        self.window.geometry("700x500") #Definir dimensões da tela
        self.window.resizable(False, False) #Impedir que seja possível alterar o tamanho da tela no eixo x e y
        
    def frames_da_tela(self):
        self.frame_1 = Frame(self.window, bg="#c0c0c0", highlightthickness=2, highlightbackground="#a30000")
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth=0.96, relheight=0.46)
        
        self.frame_2 = Frame(self.window, bg="#c0c0c0", highlightthickness=2, highlightbackground="#a30000")
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth=0.96, relheight=0.46)
        
    def widgets_frame1(self):
        
        ###Criação do botão limpar
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Limpar", font="Arial", command=self.limpar)
        self.btn_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão buscar
        self.btn_buscar = Button(self.frame_1, bg="#a30000", text="Buscar", font="Arial", command=self.buscar_produto)
        self.btn_buscar.place(relx= 0.35, rely=0.1, relwidth=0.1, relheight=0.15)
        
        self.lista_marcas = ['Nokia', 'Samsung', 'Apple', 'Xiaomi', 'Motorola']
        self.clicked = StringVar()
        self.drop_marcas = OptionMenu(self.frame_1, self.clicked, *self.lista_marcas)
        self.drop_marcas.pack()
        
        
        self.drop_marcas.place(relx=0.05, rely=0.15, relwidth=0.15)
        
        
    def lista_frame2(self):
        self.lista_cell = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3"))
        self.lista_cell.heading("#0", text="id", anchor=CENTER)
        self.lista_cell.heading("#1", text="Modelo")
        self.lista_cell.heading("#2", text="Marca", anchor=CENTER)
        self.lista_cell.heading("#3", text="Preço", anchor=CENTER)
        
        self.lista_cell.column("#0", width=1)
        self.lista_cell.column("#1", width=247)
        self.lista_cell.column("#2", width=100, anchor=CENTER)
        self.lista_cell.column("#3", width=125, anchor=CENTER)
        
        self.lista_cell.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        #Barra de rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_cell.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
    
    def buscar_produto(self):
        db = Database()
        self.limpar()
        linhas = db.get_products(marca=self.clicked.get())
        for i in range (len(linhas)):
            self.lista_cell.insert(index=i, values=[linhas[i][1], linhas[i][2], linhas[i][3]], parent='', text=linhas[i][0])

    def limpar(self):
        self.lista_cell.delete(*self.lista_cell.get_children())
        
Aplication()        
            