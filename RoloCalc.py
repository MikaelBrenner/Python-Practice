from tkinter import *
from tkinter import ttk

def calc_length(_diametro_externo = 0.0,_diametro_interno = 0.0,_espessura = 0.0):
  
    pi = 3.141592   
    numero_de_voltas = (abs(_diametro_externo - _diametro_interno) / (2 * _espessura))
    variation = _espessura * (numero_de_voltas - 1)
    _length = pi * numero_de_voltas * (_diametro_interno + variation)
    return _length

def calc_quant(*args):
    
    try:
        diametro_interno = float(diametroin.get())
        diametro_externo = float(diametroex.get())
        espessura_fita = (float(espessura.get()))
        densidade_linear = (float(densidade.get()) / 10.0)   
        length = (calc_length(_diametro_externo = diametro_externo,_diametro_interno = diametro_interno,_espessura = espessura_fita) / 10)
        quantidade = length * densidade_linear
        quantidade = int(quantidade)
        comprimento.set(quantidade)
    except ValueError:
        pass

root = Tk()
root.title("RoloCalc by Mikael Brenner")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

diametroin = StringVar()
diametroex = StringVar()
espessura = StringVar()
densidade = StringVar()
comprimento = StringVar()

diametroin_entry = ttk.Entry(mainframe, width=10, textvariable=diametroin)
diametroin_entry.grid(column=2, row=1, sticky=(W, E))

diametroex_entry = ttk.Entry(mainframe, width=10, textvariable=diametroex)
diametroex_entry.grid(column=2, row=2, sticky=(W, E))

espessura_entry = ttk.Entry(mainframe, width=10, textvariable=espessura)
espessura_entry.grid(column=2, row=3, sticky=(W, E))

densidade = ttk.Entry(mainframe, width=10, textvariable=densidade)
densidade.grid(column=2, row=4, sticky=(W, E))

ttk.Label(mainframe, textvariable=comprimento).grid(column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text="Calcular", command=calc_quant).grid(column=3, row=6, sticky=W)

ttk.Label(mainframe, text="Diâmetro Interno").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Diâmetro Externo").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Espessura").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Densidade").grid(column=1, row=4, sticky=E)

ttk.Label(mainframe, text="milímetros.").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="milímetros.").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="milímetros.").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="componentes à cada 10 centimetros.").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="Há aproximadamente").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="componentes nesse rolo.").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text="Mikael Brenner,2017.").grid(column=4, row=7, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

diametroin_entry.focus()
root.bind('<Return>', calc_quant)

root.mainloop()