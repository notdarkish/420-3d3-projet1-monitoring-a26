from observers.observer import Observateur
from datetime import datetime

class LoggerFichier(Observateur):
       def __init__(self, fichier_log: str = "monitoring.log"):
              self.fichier_log = fichier_log
              self.log_active = True  # Par défaut, le logging est activé


        def actualiser(self, sujet) -> None:
              # Récupérer les données du sujet
              donnees_metriques = sujet.get_donnees()
              cpu = donnees_metriques["cpu"]
              ram = donnees_metriques["ram"]
              disque = donnees_metriques["disque"]

              # Créer la ligne de log avec horodatage
              horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              ligne_log = (
                     f"{horodatage} | "
                     f"CPU: {cpu:.1f}% | "
                     f"RAM: {ram:.1f}% | "
                     f"Disque: {disque:.1f}%\n"
              )

              # Écrire dans le fichier log si le logging est activé
              if self.log_active:
                     with open(self.fichier_log, 'a') as f:
                            f.write(ligne_log)

              print(ligne_log)  # Afficher dans la console
