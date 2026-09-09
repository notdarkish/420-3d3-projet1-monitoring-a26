from models.metrics import MetriquesSysteme
from views.dashboard import Dashboard
 
metriques = MetriquesSysteme()
root = Tk.tk() 
cpu = AffichageCPU(root)
metriques.abonner(cpu)



def rafraichir(self):
    self.metriques.actualiser_metriques()
    self.after(2000, self.rafraichir)
