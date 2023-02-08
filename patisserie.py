class patisserie:
    createur = "ratatouille"

    def __init__(self, p=0, c=None):
        self.__poids = p
        self.__categorie = c

    def get_poids(self):
        return self.__poids

    def get_categorie(self):
        return self.__categorie

    def set_poids(self, po):
        self.__poids = po

    def set_categorie(self, ca):
        self.__categorie = ca

    def __str__(self):
        return 'le poids est de ' + str(self.__poids) + ' de la catégorie ' + str(self.__categorie)

    def __del__(self):
        del self.__categorie
        del self.__poids

    @staticmethod
    def get_categorie_autorise():
        return ["gateau", "tarte"]

    @classmethod
    def get_createur(cls):
        return cls.__createur

    @classmethod
    def get_createur(cls):
        return cls.__createur

    @classmethod
    def set_createur(cls, createur):
        cls.__createur = createur

    def __eq__(self, other):
        return self.__poids == other.__poids

    def __add__(self, other):
        if self.__categorie == other.__categorie:
            retour = self.__categorie
        else:
            retour = None
        return self.__poids + other.__poids, retour



