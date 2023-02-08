import sys
import patisserie as pat
import pickle

def main () :
    print (" Hello World ")


if __name__ == " __main__ ":
    sys . exit ( main () )


gat = pat.patisserie() #gat est une isntance
gat1 = pat.patisserie() #gat1 est une isntance
gat2 = pat.patisserie() #gat2 est une isntance

gat.set_poids("38")
gat.set_categorie("24")
gat1.createur = "tata"
gat.createur = "toto"
pat.createur = "tarte"
gat2.createur= "titi"

print(pat.createur) #retourne tarte
print(gat)
print(gat.get_categorie_autorise())

gat.set_createur("test")
print(gat.get_createur()) #retourne test

test = pat.patisserie() #test est une isntance
test1 = pat.patisserie() #test1 est une isntance
test2 = pat.patisserie() #test2 est une isntance
test.set_createur("t0")
test1.set_createur("t1")
print(gat.get_createur()) #print t1

gat=pat.patisserie(5)
gat1=pat.patisserie(6)
print(gat==gat1)

del gat1

gat2=pat.patisserie(5, "tarte")
gat3=pat.patisserie(12, "gateau")
gat4 = gat3 + gat2
print(gat4)


with open('test', 'wb') as f:
    pickle.dump(gat, f)
with open('test', 'rb'):
    f.read
f.close()
