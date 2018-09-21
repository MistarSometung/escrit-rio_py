import tkinter as tk
import crud 

class Main(tk.Frame):
   def __init__(self, master=None):
      super().__init__(master)
      self.pack()#grid(row=0, column=0)
      self.Widgets()
      
   def Widgets(self):
      """
      CRIA A BARRA DE MENU
      """
      self.menubar = tk.Menu(self)
      self.master.config(menu=self.menubar)
      
      self.menu_pedidos = tk.Menu(self.menubar, tearoff=0)
      self.menu_clientes = tk.Menu(self.menubar, tearoff=0)
      self.menu_clientes.config(bg='white')
                       
      
      self.menubar.add_cascade(menu=self.menu_pedidos, label='Pedidos')
      self.menubar.add_cascade(menu=self.menu_clientes, label='Clientes')
      
      self.menu_clientes.add_command(label="Inserir Clientes", command=self.Clientes)
      
   def Clientes(self):
      """
      CRIA O FRAME BASE PARA OS FRAMES DE BOTÃO E INSERÇÃO DE DADOS
      """
      self.frame_base = tk.Frame(self)
      self.frame_base.pack()#grid(row=0,column=0)
      """
      CRIA FRAME DE INSERÇÃO DE DADOS
      """
      self.frame_clientes = tk.LabelFrame(self.frame_base)
      self.frame_clientes['text']="Inserir clientes"
      self.frame_clientes.grid(row=0,column=0)
      
      
      
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
#=============================================================================
      self.frame_bt = tk.Frame(self.frame_base)
      self.frame_bt.grid(row=2,column=0)
      
      self.frame_busca =tk.LabelFrame(self.frame_base,bd=2, relief='sunken')
      self.frame_busca['text']="Cliente"
      self.frame_busca.grid(row=1,column=0)
      
      
      self.lb_nome = tk.Label(self.frame_busca)
      self.lb_nome['text']="NOME / RAZÃO SOCIAL"
      self.lb_nome.grid(row=0,column=0, sticky='w')
      
      self.label_nome = tk.Label(self.frame_busca, width=62)
      self.label_nome.grid(row=1,column=0, sticky='w')
      
      self.lb_cnpj = tk.Label(self.frame_busca)
      self.lb_cnpj['text']="CNPJ"
      self.lb_cnpj.grid(row=2,column=0, sticky='w')
      
      self.label_cnpj = tk.Label(self.frame_busca, width=18)
      self.label_cnpj.grid(row=3,column=0, sticky='w')
      
      self.lb_insc = tk.Label(self.frame_busca)
      self.lb_insc['text']="INSCRIÇÃO ESTADUAL"
      self.lb_insc.grid(row=2,column=1, sticky='w')
      
      self.label_insc = tk.Label(self.frame_busca, width=12)
      self.label_insc.grid(row=3,column=1, sticky='w')
      
      self.lb_endereço = tk.Label(self.frame_busca)
      self.lb_endereço['text']="ENDEREÇO"
      self.lb_endereço.grid(row=4,column=0, sticky='w')
      
      self.label_endereço = tk.Label(self.frame_busca, width=40)
      self.label_endereço.grid(row=5,column=0, sticky='w')
      
      self.lb_bairro = tk.Label(self.frame_busca)
      self.lb_bairro['text']="BAIRRO"
      self.lb_bairro.grid(row=4,column=1, sticky='w')
      
      self.label_bairro = tk.Label(self.frame_busca, width=15)
      self.label_bairro.grid(row=5,column=1, sticky='w')
      
      self.lb_cep = tk.Label(self.frame_busca)
      self.lb_cep['text']="CEP"
      self.lb_cep.grid(row=4,column=2, sticky='w')
      
      self.label_cep = tk.Label(self.frame_busca, width=8)
      self.label_cep.grid(row=5,column=2, sticky='w')
      
      self.lb_city = tk.Label(self.frame_busca)
      self.lb_city['text']="MUNICÍPIO"
      self.lb_city.grid(row=6,column=0, sticky='w')
      
      self.label_city = tk.Label(self.frame_busca, width=20)
      self.label_city.grid(row=7,column=0, sticky='w')
      
      self.lb_uf = tk.Label(self.frame_busca)
      self.lb_uf['text']="UF"
      self.lb_uf.grid(row=6,column=1, sticky='w')
      
      self.label_uf = tk.Label(self.frame_busca, width=2)
      self.label_uf.grid(row=7,column=1, sticky='w')
     
      self.lb_tel = tk.Label(self.frame_busca)
      self.lb_tel['text']="TELEFONE"
      self.lb_tel.grid(row=8,column=0, sticky='w')
      
      self.label_tel = tk.Label(self.frame_busca, width=12)
      self.label_tel.grid(row=9,column=0, sticky='w')
      
      self.lb_email = tk.Label(self.frame_busca)
      self.lb_email['text']="E-MAIL"
      self.lb_email.grid(row=10,column=0, sticky='w')
      
      self.label_email = tk.Label(self.frame_busca, width=30)
      self.label_email.grid(row=11,column=0, sticky='w')     
#==============================================================================

      self.salvar_bt = tk.Button(self.frame_bt)
      self.salvar_bt['text']="Salvar"
      self.salvar_bt['command']=self.Salvar_Cliente
      self.salvar_bt.grid(row=0,column=0)      
      
      
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
      
      
      
      
      


root = tk.Tk()
root.title("C&P Manager_ver.0.1")
root.geometry("800x600")
apk = Main(master=root)
apk.mainloop()
      