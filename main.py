import voiture as myvoiture

merco = myvoiture.voiture()
merco.set_couleur("rouge")
merco.set_marque("merco")
merco.set_modele("a45")
merco.set_chevaux("450")
merco.ajouter_option("chevaliere")
merco.ajouter_option("chevaliere")
merco.ajouter_option("chevalieres")
merco.is_option_present("chevalieree")
print(merco)
del merco
print(merco)