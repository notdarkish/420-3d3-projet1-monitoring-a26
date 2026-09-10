from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.disk_display import AffichageDisque
from observers.ram_display import AffichageRAM
import tkinter as tk

metriques = MetriquesSysteme()
root = tk.Tk()
cpu = AffichageCPU(root)
disque = AffichageDisque(root)
ram = AffichageRAM(root)
metriques.abonner(cpu)
metriques.abonner(disque)
metriques.abonner(ram)
def rafraichir():
    metriques.actualiser_metriques()
    root.after(2000, rafraichir)

rafraichir()
root.mainloop()