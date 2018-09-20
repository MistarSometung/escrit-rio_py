import tkinter as tk

class Main(tk.Frame):
   def __init__(self, master=None):
      super().__init__(master)
      self.grid(row=0, column=0)
      self.Widgets()
      
   def Widgets(self):
      
      self.menubar = tk.Menu(self)
      self.master.config(menu=self.menubar)
      
      self.menu_pedidos = tk.Menu(self.menubar, tearoff=0)
      self.menu_clientes = tk.Menu(self.menubar, tearoff=0)
      
      self.menubar.add_cascade(menu=self.menu_clientes, label='Pedidos')
      self.menubar.add_cascade(menu=self.menu_pedidos, label='Clientes')
      
      self.menu_pedidos.add_command(label="Gerenciar Clientes", command=self.Clientes)
      
   def Clientes(self):
      
      self.frame_base = tk.Frame(self)
      self.frame_base.grid(row=0,column=0)
      
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
      self.lb_city.grid(row=6,column=0, sticky='w')
      
      self.entry_city = tk.Entry(self.frame_clientes, width=20)
      self.entry_city.grid(row=7,column=0, sticky='w')
      
      self.lb_uf = tk.Label(self.frame_clientes)
      self.lb_uf['text']="UF"
      self.lb_uf.grid(row=6,column=1, sticky='w')
      
      self.entry_uf = tk.Entry(self.frame_clientes, width=2)
      self.entry_uf.grid(row=7,column=1, sticky='w')
     
      self.lb_tel = tk.Label(self.frame_clientes)
      self.lb_tel['text']="TELEFONE"
      self.lb_tel.grid(row=8,column=0, sticky='w')
      
      self.entry_tel = tk.Entry(self.frame_clientes, width=12)
      self.entry_tel.grid(row=9,column=0, sticky='w')
      
      self.lb_email = tk.Label(self.frame_clientes)
      self.lb_email['text']="E-MAIL"
      self.lb_email.grid(row=10,column=0, sticky='w')
      
      self.entry_email = tk.Entry(self.frame_clientes, width=30)
      self.entry_email.grid(row=11,column=0, sticky='w')
      
      
      
      
      
      
      
      


root = tk.Tk()
root.title("C&P Manager_ver.0.1")
root.geometry("800x600")
apk = Main(master=root)
apk.mainloop()
      