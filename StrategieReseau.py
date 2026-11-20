
from Terrain import Terrain

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        entree = t.get_entree()

        noeud_entree = 0
        noeuds = {0: entree}
        arcs = []
        numero = 1

        while True:
            t.afficher()
            print("Noeuds actuels :", noeuds)
            print("Arcs actuels :", arcs)

            ligne = int(input("Ligne du nouveau noeud (-1 pour terminer) : "))

            if ligne == -1:
                break

            colonne = int(input("Colonne du nouveau noeud : "))

            if ligne < 0 or ligne >= t.hauteur or colonne < 0 or colonne >= t.largeur:
                print("Coordonnees invalides")
                continue

            if (ligne, colonne) in noeuds.values():
                print("Un noeud existe deja a cet endroit")
                continue

            noeuds[numero] = (ligne, colonne)

            print("Noeuds disponibles :", list(noeuds.keys()))

            while True:
                n = input("Noeud a relier (Entrée pour terminer) : ")

                if n == "":
                    break

                n = int(n)

                if n not in noeuds or n == numero:
                    print("Noeud invalide")
                    continue

                ligne_n, colonne_n = noeuds[n]

                distance = abs(ligne - ligne_n) + abs(colonne - colonne_n)

                if distance != 1:
                    print("Les noeuds ne sont pas voisins")
                    continue

                arc = (min(n, numero), max(n, numero))

                if arc not in arcs:
                    arcs.append(arc)

            numero += 1

        return noeud_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []

