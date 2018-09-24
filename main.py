import tkinter.ttk as ttk
import tkinter as tk
import crud 

class Main(tk.Frame):
   def __init__(self, master=None):
      super().__init__(master)
      self.pack()#grid(row=0, column=0)
      self.Widgets()
      
      self.combovar = tk.StringVar()
      
      
            
      self.frame_de_base = tk.Frame(self)
      self.frame_de_base.pack()
      
   def Widgets(self):
      """
      CRIA A BARRA DE MENU
      """
      self.menubar = tk.Menu(self)
      self.master.config(menu=self.menubar)
      
      self.menu_pedidos = tk.Menu(self.menubar, tearoff=0)
      self.menu_produtos = tk.Menu(self.menubar, tearoff=0)
      self.menu_clientes = tk.Menu(self.menubar, tearoff=0)
      self.menu_clientes.config(bg='white')
                       
      
      self.menubar.add_cascade(menu=self.menu_pedidos, label='Pedidos')
      self.menubar.add_cascade(menu=self.menu_clientes, label='Clientes')
      self.menubar.add_cascade(menu=self.menu_produtos, label='Produtos')
      
      self.menu_clientes.add_command(label="Inserir clientes", command=self.Inserir_Clientes)
      self.menu_clientes.add_command(label="Buscar clientes", command = self.Buscar_Clientes)
      self.menu_produtos.add_command(label="Inserir produto",command = self.Inserir_Produtos)
      
   def Inserir_Clientes(self):
      
      self.frame_de_base.destroy()
      
      self.frame_de_base = tk.Frame(self)
      self.frame_de_base.pack()
      
      try:
         """
         CRIA FRAME DE INSERÇÃO DE DADOS
         """
         self.frame_clientes = tk.LabelFrame(self.frame_de_base)
         self.frame_clientes['text']="Inserir clientes"
         self.frame_clientes.grid(row=0,column=0)
         
         
         """
         CRIA OS LABELS E ENTRYS DO INSERIR CLIENTES
         """
         self.lb_nome = tk.Label(self.frame_clientes)
         self.lb_nome['text']="NOME / RAZÃO SOCIAL"
         self.lb_nome.grid(row=0,column=0, sticky='w')
         
         self.entry_nome = tk.Entry(self.frame_clientes, width=62)
         self.entry_nome.grid(row=1,column=0, sticky='w')
         
         self.lb_cnpj = tk.Label(self.frame_clientes)
         self.lb_cnpj['text']="CNPJ"
         self.lb_cnpj.grid(row=2,column=0, sticky='w')
         
         self.entry_cnpj = tk.Entry(self.frame_clientes, width=18)
         self.entry_cnpj.grid(row=3,column=0, sticky='w')
         
         self.lb_insc = tk.Label(self.frame_clientes)
         self.lb_insc['text']="INSCRIÇÃO ESTADUAL"
         self.lb_insc.grid(row=2,column=1, sticky='w')
         
         self.entry_insc = tk.Entry(self.frame_clientes, width=12)
         self.entry_insc.grid(row=3,column=1, sticky='w')
         
         self.lb_endereço = tk.Label(self.frame_clientes)
         self.lb_endereço['text']="ENDEREÇO"
         self.lb_endereço.grid(row=4,column=0, sticky='w')
         
         self.entry_endereço = tk.Entry(self.frame_clientes, width=40)
         self.entry_endereço.grid(row=5,column=0, sticky='w')
         
         self.lb_num = tk.Label(self.frame_clientes)
         self.lb_num['text']="NUMERO"
         self.lb_num.grid(row=6,column=0, sticky='w')
         
         self.entry_num = tk.Entry(self.frame_clientes, width=5)
         self.entry_num.grid(row=7,column=0, sticky='w')
         
         self.lb_bairro = tk.Label(self.frame_clientes)
         self.lb_bairro['text']="BAIRRO"
         self.lb_bairro.grid(row=4,column=1, sticky='w')
         
         self.entry_bairro = tk.Entry(self.frame_clientes, width=15)
         self.entry_bairro.grid(row=5,column=1, sticky='w')
                   
         self.lb_cep = tk.Label(self.frame_clientes)
         self.lb_cep['text']="CEP"
         self.lb_cep.grid(row=4,column=2, sticky='w')
         
         self.entry_cep = tk.Entry(self.frame_clientes, width=8)
         self.entry_cep.grid(row=5,column=2, sticky='w')
         
         self.lb_city = tk.Label(self.frame_clientes)
         self.lb_city['text']="MUNICÍPIO"
         self.lb_city.grid(row=8,column=0, sticky='w')
         
         self.entry_city = tk.Entry(self.frame_clientes, width=20)
         self.entry_city.grid(row=9,column=0, sticky='w')
         
         self.lb_uf = tk.Label(self.frame_clientes)
         self.lb_uf['text']="UF"
         self.lb_uf.grid(row=7,column=1, sticky='w')
         
         self.entry_uf = tk.Entry(self.frame_clientes, width=2)
         self.entry_uf.grid(row=8,column=1, sticky='w')
        
         self.lb_tel = tk.Label(self.frame_clientes)
         self.lb_tel['text']="TELEFONE"
         self.lb_tel.grid(row=10,column=0, sticky='w')
         
         self.entry_tel = tk.Entry(self.frame_clientes, width=12)
         self.entry_tel.grid(row=11,column=0, sticky='w')
         
         self.lb_email = tk.Label(self.frame_clientes)
         self.lb_email['text']="E-MAIL"
         self.lb_email.grid(row=12,column=0, sticky='w')
      
         self.entry_email = tk.Entry(self.frame_clientes, width=30)
         self.entry_email.grid(row=13,column=0, sticky='w')
      except tk.TclError:
         self.frame_de_base = tk.Frame(self)
         self.frame_de_base.pack()
         
         self.Inserir_Clientes()
         
#=============================================================================

      """
      CRIA O FRAME DOS BOTÕES
      """
      self.frame_bt = tk.Frame(self.frame_de_base)
      self.frame_bt.grid(row=2,column=0)
      
      """
      CRIA OS BOTÕES DO *INSERIR CLIENTES*
      """
      self.salvar_bt = tk.Button(self.frame_bt)
      self.salvar_bt['text']="Salvar"
      self.salvar_bt['command']=self.Salvar_Cliente
      self.salvar_bt.grid(row=0,column=0)   
      
      self.voltar_bt = tk.Button(self.frame_bt)
      self.voltar_bt['text']="Voltar"
      self.voltar_bt['command']= self.Home
      self.voltar_bt.grid(row=0,column=1)
      
   """
   RETORNA PARA A PÁGINA PRINCIPAL DO PROGRAMA
   """   
   def Home(self):
      self.frame_de_base.destroy()
   
   
   """
   SALVA NOVOS CLIENTES NO BANCO DE DADOS
   """
   def Salvar_Cliente(self):
      if len(self.entry_nome.get())==0 or len(self.entry_cnpj.get())==0:
         print("Preencha todos os campos")
      else:
         nome = self.entry_nome.get()
         cnpj = self.entry_cnpj.get()
         insc = self.entry_insc.get()
         endereço = self.entry_endereço.get()
         numero = self.entry_num.get()
         bairro = self.entry_bairro.get()
         cep = self.entry_cep.get()
         municipio = self.entry_city.get()
         uf = self.entry_uf.get()
         phone = self.entry_tel.get()
         email = self.entry_email.get()
         
         crud.Inserir(nome, cnpj, insc, endereço,numero, bairro, cep, municipio, uf, phone, email)
  
   
   """
   BUSCA POR CLIENTES JÁ CADASTRADOS
   """   
    
   def Buscar_Clientes(self):
      
      self.frame_de_base.destroy()
      
      self.frame_de_base = tk.Frame(self)
      self.frame_de_base.pack()
      
      self.rest= ["","",]
      nome = self.rest[1]
      print(nome)
      
      
      self.frame_bt = tk.Frame(self.frame_de_base)
      self.frame_bt.grid(row=0,column=0)
      
      
      self.combo = ttk.Combobox(self.frame_bt)
      self.combo['values']='nome', 'cnpj', 'insc', 'endereço', 'numero', 'bairro', 'cep', 'municipio', 'uf', 'phone', 'email'
      self.combo.grid(row=0,column=0)
      
      self.entry_pesq = tk.Entry(self.frame_bt)
      self.entry_pesq.grid(row=0,column=1)
      
      self.pesquisar_bt = tk.Button(self.frame_bt)
      self.pesquisar_bt['text']="Pesquisar"
      self.pesquisar_bt['command']= self.Pesquisar_cliente
      self.pesquisar_bt.grid(row=0,column=2)
      
      
   def Pesquisar_cliente(self):
      coluna =self.combo.get()
      valor = self.entry_pesq.get()
      
      rest = crud.Buscar(valor, coluna)
      busca = rest[0]
 
      print(busca)
#==============================================================================         
      self.frame_busca =tk.LabelFrame(self.frame_de_base ,bd=2, relief='sunken')
      self.frame_busca['text']="Cliente"
      self.frame_busca.grid(row=1,column=0)
                  
      self.lb_nome = tk.Label(self.frame_busca)
      self.lb_nome['text']="NOME / RAZÃO SOCIAL"
      self.lb_nome.grid(row=0,column=0, sticky='w')
         
      self.label_nome = tk.Label(self.frame_busca)
      self.label_nome['bg']='white'
      self.label_nome['text']= busca[1]
      self.label_nome.grid(row=1,column=0, sticky='w')
      
      self.lb_cnpj = tk.Label(self.frame_busca)
      self.lb_cnpj['text']="CNPJ"
      self.lb_cnpj.grid(row=2,column=0, sticky='w')
         
      self.label_cnpj = tk.Label(self.frame_busca)
      self.label_cnpj['text']=busca[2]
      self.label_cnpj['bg']='white'
      self.label_cnpj.grid(row=3,column=0, sticky='w')
      
      self.lb_insc = tk.Label(self.frame_busca)
      self.lb_insc['text']="INSCRIÇÃO ESTADUAL"
      self.lb_insc.grid(row=2,column=1, sticky='w')
         
      self.label_insc = tk.Label(self.frame_busca)
      self.label_insc['text']=busca[3]
      self.label_insc['bg']='white'
      self.label_insc.grid(row=3,column=1, sticky='w')
      
      self.lb_endereço = tk.Label(self.frame_busca)
      self.lb_endereço['text']="ENDEREÇO"
      self.lb_endereço.grid(row=4,column=0, sticky='w')
         
      self.label_endereço = tk.Label(self.frame_busca)
      self.label_endereço['text']=busca[4]
      self.label_endereço['bg']='white'
      self.label_endereço.grid(row=5,column=0, sticky='w')
      
      self.lb_num = tk.Label(self.frame_busca)
      self.lb_num['text']="NUMERO"
      self.lb_num.grid(row=6,column=0, sticky='w')
      
      self.lb_num = tk.Label(self.frame_busca)
      self.lb_num['text']=busca[5]
      self.lb_num['bg']='white'
      self.lb_num.grid(row=7,column=0, sticky='w')
         
      self.lb_bairro = tk.Label(self.frame_busca)
      self.lb_bairro['text']="BAIRRO"
      self.lb_bairro.grid(row=4,column=1, sticky='w')
      
      self.label_bairro = tk.Label(self.frame_busca)
      self.label_bairro['text']=busca[6]
      self.label_bairro['bg']='white'
      self.label_bairro.grid(row=5,column=1, sticky='w')
         
      self.lb_cep = tk.Label(self.frame_busca)
      self.lb_cep['text']="CEP"
      self.lb_cep.grid(row=4,column=2, sticky='w')
         
      self.label_cep = tk.Label(self.frame_busca)
      self.label_cep['text']=busca[7]
      self.label_cep['bg']='white'
      self.label_cep.grid(row=5,column=2, sticky='w')
         
      self.lb_city = tk.Label(self.frame_busca)
      self.lb_city['text']="MUNICÍPIO"
      self.lb_city.grid(row=8,column=0, sticky='w')
         
      self.label_city = tk.Label(self.frame_busca)
      self.label_city['text']=busca[8]
      self.label_city['bg']='white'
      self.label_city.grid(row=9,column=0, sticky='w')
         
      self.lb_uf = tk.Label(self.frame_busca)
      self.lb_uf['text']="UF"
      self.lb_uf.grid(row=8,column=1, sticky='w')
         
      self.label_uf = tk.Label(self.frame_busca)
      self.label_uf['text']=busca[9]
      self.label_uf['bg']='white'
      self.label_uf.grid(row=9,column=1, sticky='w')
        
      self.lb_tel = tk.Label(self.frame_busca)
      self.lb_tel['text']="TELEFONE"
      self.lb_tel.grid(row=10,column=0, sticky='w')
         
      self.label_tel = tk.Label(self.frame_busca)
      self.label_tel['text']=busca[10]
      self.label_tel['bg']='white'
      self.label_tel.grid(row=11,column=0, sticky='w')
         
      self.lb_email = tk.Label(self.frame_busca)
      self.lb_email['text']="E-MAIL"
      self.lb_email.grid(row=12,column=0, sticky='w')
      
      self.label_email = tk.Label(self.frame_busca)
      self.label_email['text']=busca[11]
      self.label_email['bg']='white'
      self.label_email.grid(row=13,column=0, sticky='w')
   """
   FIM DA BUSCA POR CLIENTES
   """      
#=============================================================================
      
   def Inserir_Produtos(self):
      self.frame_de_base.destroy()
      
      self.frame_de_base = tk.Frame(self)
      self.frame_de_base.pack()
      
      self.frame_prod = tk.Frame(self.frame_de_base)
      self.frame_prod.grid(row=0,column=0)
      
      self.lb_prod = tk.Label(self.frame_prod)
      self.lb_prod['text']="Produto"
      self.lb_prod.grid(row=0,column=0)
      
      self.lb_tipo = tk.Label(self.frame_prod)
      self.lb_tipo['text']="Tipo de produto"
      self.lb_tipo.grid(row=1,column=0)
      
      self.entry_nomeprod = tk.Entry(self.frame_prod)
      self.entry_nomeprod.grid(row=0,column=1, sticky='w')
      
      self.combo_pro = ttk.Combobox(self.frame_prod)
      self.combo_pro['values']=crud.Buscar_Produto()
      self.combo_pro.grid(row=1,column=1, sticky='w')
      
      self.entry_tipo = tk.Entry(self.frame_prod)
      self.entry_tipo.grid(row=1,column=2)
      
      self.lb_prodinfo = tk.Label(self.frame_prod)
      self.lb_prodinfo['text']= "Se o tipo do produto foi previamente cadastrado, utilize o ComboBox para inserir o tipo do novo produto"
      self.lb_prodinfo.grid(row=3,column=0, columnspan=5)
      
      self.bt_insprod = tk.Button(self.frame_prod)
      self.bt_insprod['text']="Inserir"
      self.bt_insprod['command']= self.New_Prod
      self.bt_insprod.grid(row=2,column=0)
      
   def New_Prod(self):
      nome = self.entry_nomeprod.get()
      tipo = self.entry_tipo.get()
         
      crud.Inserir_Produto(tipo, nome)
      
      
      
      
      
      
   
      
      
   
   
     
      
      
      
      


root = tk.Tk()
root.title("C&P Manager_ver.0.1")
root.geometry("800x600")
apk = Main(master=root)
apk.mainloop()
      
