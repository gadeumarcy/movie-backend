###### Classes ####

class Chien:
    pass


#### Objet (Instance) #####
mon_chien = Chien()
type(mon_chien)


#### Attributs ####
class Chien:
    def __init__(self,nom,race):
        self.nom = nom
        self.race =  race
    def aboyer(self):
        print(f"{self.nom} aboie!")
        
mon_chien =  Chien("Pipo", "Labrador")
print(mon_chien.nom)
print(mon_chien.race)
print(mon_chien.aboyer())


##### Méthodes #####