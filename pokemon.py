class Pokemon:
    def __init__(self, nom, p_type, defense, puissance_attaque, point_de_vie):
        self.nom = nom
        self.p_type = p_type
        self.defense = defense
        self.puissance_attaque = puissance_attaque
        self.point_de_vie = point_de_vie

class Normal(Pokemon):
    def __init__(self, nom, defense=5, puissance_attaque=10, point_de_vie=100):
        super().__init__(nom, "Normal", defense, puissance_attaque, point_de_vie)

class Feu(Pokemon):
    def __init__(self, nom, defense=4, puissance_attaque=12, point_de_vie=80):
        super().__init__(nom, "Feu", defense, puissance_attaque, point_de_vie)

class Eau(Pokemon):
    def __init__(self, nom, defense=6, puissance_attaque=8, point_de_vie=120):
        super().__init__(nom, "Eau", defense, puissance_attaque, point_de_vie)

class Plante(Pokemon):
    def __init__(self, nom, defense=8, puissance_attaque=6, point_de_vie=150):
        super().__init__(nom, "Plante", defense, puissance_attaque, point_de_vie)

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def point_de_vie(self):
        return self._point_de_vie

    @point_de_vie.setter
    def point_de_vie(self, value):
        self._point_de_vie = value

    def afficher_informations(self):
        print("Nom: {}\nType: {}\nPoints de vie: {}\nDéfense: {}\nPuissance d'attaque: {}\n"
              .format(self.nom, self.p_type, self.point_de_vie, self.defense, self.puissance_attaque))

