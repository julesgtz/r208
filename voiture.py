class voiture:
    def __init__(self, mar=None, mod=None, ch=None, coul=None, options=[]):
        self.__marque=mar
        self.__modele=mod
        self.__chevaux=ch
        self.__couleur=coul
        self.__options=options

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_chevaux(self):
        return self.__chevaux

    def get_couleur(self):
        return self.__couleur

    def set_marque(self, marq):
        self.__marque = marq

    def set_modele(self, modl):
        self.__modele = modl

    def set_chevaux(self, che):
        self.__chevaux = che

    def set_couleur(self, coule):
        self.__couleur = coule

    def __str__(self):
        return 'Ma voiture est de la marque ' + str(self.__marque) + ' du modele ' + str(self.__modele) + ' avec ' + str(self.__chevaux) + ' chevaux et de couleur ' + str(self.__couleur) + ' dont les options sont ' + " ".join(self.__options)

    def get_options(self):
        return self.__options

    def set_options(self, op):
        self.__options=op

    def ajouter_option(self, opts):
        self.__options.append(opts)

    def supprimer_option(self, opt):
        self.__options.remove(opt)

    def is_option_present(self, opt):
        if opt in self.__options:
            print("l'options est deja présente")
        else:
            print("l'option n'est pas présente")

    def __del__(self):
        del self.__couleur
        del self.__options
        del self.__chevaux
        del self.__modele
        del self.__marque