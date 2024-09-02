import tkinter as tk
# Funções

# Centraliza a Janela 
def center(win):
    win.update_idletasks() 
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
#Janela Principal

janela = tk.Tk()
janela.title("Sistema de Eventos")
janela.minsize(850, 550)
janela.maxsize(850, 550)

#Frames
frame1 = tk.Frame(master=janela, width=150, height=550, relief="raised", bd=1) 
frame1.place(x=0, y=0)

frame2 = tk.Frame(master=janela, width=700, height=550) #usar sunken
frame2.place(x=150, y=0)

# Labels - Frame 1
lb_codigo = tk.Label(master = frame1, text="Digite o Código do Evento:")
lb_codigo.place(x=0, y=0)

lb_usuario = tk.Label(master = frame1, text="Usuário:")
lb_usuario.place(x=0, y=420)
lb_usuario = tk.Label(master = frame1, text="Nível de Acesso:")
lb_usuario.place(x=0, y=440)

# Labels - Frame 2
lb_evento = tk.Label(master = frame2, text="Evento Selecionado:")
lb_evento.place(x=10, y=0)

lb_data = tk.Label(master = frame2, text="Data:")
lb_data.place(x=10, y=20)

lb_alunos = tk.Label(master = frame2, text="Alunos Cadastrados:")
lb_alunos.place(x=10, y=40)

lb_rodape = tk.Label(master = frame2, text="Sistema desenvolvido por Nathan Tagino - 2024")
lb_rodape.place(x=190, y=530)

# Entrys - Frame 1
entry_codigo = tk.Entry(master = frame1)
entry_codigo.place(x=10, y=25)

#Buttons - Frame 1
bt_pesquisar = tk.Button(master = frame1, text="Buscar Evento")
bt_pesquisar.place(x=30, y=50)

#Buttons - Frame 2
bt_pesquisar = tk.Button(master = frame2, text="Exportar Evento")
bt_pesquisar.place(x=600, y=0)

center(janela)
janela.mainloop()
