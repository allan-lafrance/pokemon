import random
import json
from pokemon import Pokemon, Normal, Eau, Feu, Plante

class Combat:
    def __init__(self, pokemon1, pokemon2, pokedex):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokedex = pokedex

    def est_fini(self):
        return self.pokemon1.point_de_vie <= 0 or self.pokemon2.point_de_vie <= 0

    def nom_vainqueur(self):
        if self.pokemon1.point_de_vie > 0:
            return self.pokemon1.nom
        elif self.pokemon2.point_de_vie > 0:
            return self.pokemon2.nom
        else:
            return None

    def peut_attaquer(self):
        return random.randint(0, 1) == 1

    def degats_infliges(self, attaquant, defenseur):
        type_attaque = attaquant.p_type
        type_defense = defenseur.p_type
        coef = 1
        if type_attaque == "Eau":
            if type_defense == "Feu":
                coef = 2
            elif type_defense == "Plante":
                coef = 0.5
        elif type_attaque == "Feu":
            if type_defense == "Eau":
                coef = 0.5
            elif type_defense == "Plante":
                coef = 2
        elif type_attaque == "Plante":
            if type_defense == "Eau":
                coef = 2
            elif type_defense == "Feu":
                coef = 0.5
        elif type_attaque == "Normal":
            if type_defense == "Eau":
                coef = 0.75
            elif type_defense == "Feu":
                coef = 0.75
            elif type_defense == "Plante":
                coef = 0.75
        return int(attaquant.puissance_attaque * coef - defenseur.defense)

    def attaquer(self, attaquant, defenseur):
        if self.peut_attaquer():
            degats = self.degats_infliges(attaquant, defenseur)
            if degats > 0:
                defenseur.point_de_vie -= degats
                print("{} attaque {} et inflige {} dégâts.".format(attaquant.nom, defenseur.nom, degats))
            else:
                print("{} attaque {} mais son attaque est sans effet.".format(attaquant.nom, defenseur.nom))
            if defenseur.point_de_vie <= 0:
                print("{} n'a plus de point de vie. {} a gagné le combat!".format(defenseur.nom, attaquant.nom))
        else:
            print("{} attaque {} mais loupe son attaque.".format(attaquant.nom, defenseur.nom))

    def nom_perdant(self):
        if self.pokemon1.point_de_vie <= 0:
            return self.pokemon1.nom
        elif self.pokemon2.point_de_vie <= 0:
            return self.pokemon2.nom
        else:
            return None

    def enregistrer_pokemon(self, pokemon):
        pokedex = self.pokedex
        pokedex.ajouter_pokemon(pokemon)

    def jouer(self):
        print("Le combat commence entre {} et {}!".format(self.pokemon1.nom, self.pokemon2.nom))
        while not self.est_fini():
            self.attaquer(self.pokemon1, self.pokemon2)
            if self.est_fini():
                break
            self.attaquer(self.pokemon2, self.pokemon1)