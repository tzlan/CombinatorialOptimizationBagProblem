class Objet:

    def initialisation(ob, poids, valeur, indice):
        ob.indice = indice
        ob.poids = poids
        ob.valeur = valeur
        ob.rapport = valeur // poids

    def compareRapport(ob, autreObject):

        return ob.rapport < autreObject.rapport

    def utilitePoidsUtilite(ob, autreObject):

        if ob.poids >=0 and autreObject.poids >=0:
            for i in range(ob.poids, autreObject.poids):
                return ob.poids[i] / ob.valeur[i]

    listePoidsObjets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listeValeursObjets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    capaciteSac1 = 55
    capaciteSac2 = 30


    utilite = utilitePoidsUtilite()
