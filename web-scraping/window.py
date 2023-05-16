from tkinter import *
from tkinter import ttk


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
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Limpar", font="Arial")
        self.btn_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão buscar
        self.btn_limpar = Button(self.frame_1, bg="#a30000", text="Buscar", font="Arial")
        self.btn_limpar.place(relx= 0.35, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação da label e entrada do código
        self.label_codigo = Label(self.frame_1, text= "Código", bg="#c0c0c0")
        self.label_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.067)
        
        ###Criação da label e entrada do nome
        self.label_nome = Label(self.frame_1, text= "Nome", bg="#c0c0c0")
        self.label_nome.place(relx=0.05, rely=0.35)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.45, relwidth=0.85)
        
        ###Criação da label e entrada do telefone
        self.label_nome = Label(self.frame_1, text= "Telefone", bg="#c0c0c0")
        self.label_nome.place(relx=0.05, rely=0.6)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        ###Criação da label e entrada da cidade
        self.label_nome = Label(self.frame_1, text= "Cidade", bg="#c0c0c0")
        self.label_nome.place(relx=0.5, rely=0.6)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    
    def lista_frame2(self):
        self.lista_cell = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3"))
        self.lista_cell.heading("#0", text="")
        self.lista_cell.heading("#1", text="Marca")
        self.lista_cell.heading("#2", text="Modelo")
        self.lista_cell.heading("#3", text="Preço")
        
        self.lista_cell.column("#0", width=1)
        self.lista_cell.column("#1", width=50)
        self.lista_cell.column("#2", width=200)
        self.lista_cell.column("#3", width=125)
        
        self.lista_cell.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        #Barra de rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_cell.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        
Aplication()        
            