import json
import random
from combat import Combat
from pokemon import Normal, Feu, Eau, Plante

class Pokedex:
    def __init__(self):
        with open('pokedex.json', 'r') as f:
            self.pokemon = json.load(f)

    def print_pokemon(self):
        for p in self.pokemon:
            p_type = p["type"]
            if p_type == "Normal":
                pokemon = Normal(p["nom"])
            elif p_type == "Feu":
                pokemon = Feu(p["nom"])
            elif p_type == "Eau":
                pokemon = Eau(p["nom"])
            elif p_type == "Plante":
                pokemon = Plante(p["nom"])

            print(f'{pokemon.nom} ({p_type}) - {pokemon.defense} Defense - {pokemon.puissance_attaque} Attaque - {pokemon.point_de_vie} HP')

    def add_pokemon(self, nom, p_type):
        if p_type == "Normal":
            pokemon = Normal(nom)
        elif p_type == "Feu":
            pokemon = Feu(nom)
        elif p_type == "Eau":
            pokemon = Eau(nom)
        elif p_type == "Plante":
            pokemon = Plante(nom)

        self.pokemon.append({"nom": pokemon.nom, "type": p_type})
        with open('pokedex.json', 'w') as f:
            json.dump(self.pokemon, f)

    def get_pokemon(self, nom):
        for p in self.pokemon:
            if p["nom"] == nom:
                p_type = p["type"]
                if p_type == "Normal":
                    return Normal(p["nom"])
                elif p_type == "Feu":
                    return Feu(p["nom"])
                elif p_type == "Eau":
                    return Eau(p["nom"])
                elif p_type == "Plante":
                    return Plante(p["nom"])
        return None

pokedex = Pokedex()

def add_pokemon():
    nom = input('Entrez le nom du Pokémon : ')
    p_type = input('Entrez le type du Pokémon : ')
    pokedex.add_pokemon(nom, p_type)
    print(f"Le Pokémon {nom} a été ajouté au Pokédex.")

def view_pokedex():
    pokedex.print_pokemon()

while True:
    print('\nBienvenue sur le jeu !')
    print('choisissez une option:')
    print("1. Lancer une partie")
    print("2. Ajouter un Pokémon")
    print("3. Accéder au Pokédex")
    print("4. Quitter")

    choix = input('Entrez votre choix : ')

    if choix == '1':
        print("Choisissez votre Pokémon (nom du Pokémon) :")
        pokemon1 = input("Pokemon 1: ")
        pokemon2 = random.choice([p["nom"] for p in pokedex.pokemon])
        if pokemon1 not in [p["nom"] for p in pokedex.pokemon]:
            print("Le pokemon n'existe pas")
        else:
            pokemon1 = pokedex.get_pokemon(pokemon1)
            pokemon2 = pokedex.get_pokemon(pokemon2)
            combat = Combat(pokemon1, pokemon2, pokedex)
            combat.jouer()
    elif choix == '2':
        add_pokemon()
    elif choix == '3':
        view_pokedex()
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print('Choix incorrect, réessayez.')