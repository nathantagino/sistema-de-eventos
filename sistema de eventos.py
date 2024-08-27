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
janela.minsize(550, 350)
janela.maxsize(550, 350)

#Frames
frame1 = tk.Frame(master=janela, width=150, height=350, relief="raised", bd=1) 
frame1.place(x=0, y=0)

frame2 = tk.Frame(master=janela, width=400, height=350) #usar sunken
frame2.place(x=150, y=0)

# Labels
lb_codigo = tk.Label(master = frame1, text="Digite o Código do Evento:")
lb_codigo.place(x=0, y=0)

# Entrys
entry_codigo = tk.Entry(master = frame1)
entry_codigo.place(x=10, y=25)

bt_pesquisar = tk.Button(master = frame1, text="Buscar Evento")
bt_pesquisar.place(x=30, y=50)

center(janela)
janela.mainloop()