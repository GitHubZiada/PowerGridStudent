from Terrain import Terrain, Case
import heapq

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

        entree = t.get_entree()

        if entree == (-1, -1):
            return -1, {}, []

        noeuds = {0: entree}
        arcs = []
        positions = {entree: 0}
        clients = set(t.get_clients())

        # Connecter progressivement tous les clients
        while clients - positions.keys():

            restants = clients - positions.keys()
            distances = {}
            precedents = {}
            file = []

            # Dijkstra depuis le réseau existant
            for position in positions:
                distances[position] = 0
                heapq.heappush(file, (0, position))

            cible = None

            while file:
                cout, position = heapq.heappop(file)

                if cout > distances[position]:
                    continue

                if position in restants:
                    cible = position
                    break

                i, j = position

                voisins = [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1)
                ]

                for x, y in voisins:
                    if not (0 <= x < t.hauteur and
                            0 <= y < t.largeur):
                        continue

                    voisin = (x, y)

                    if t[x][y] == Case.OBSTACLE:
                        nouveau_cout = cout + 3.5
                    else:
                        nouveau_cout = cout + 2.5

                    if nouveau_cout < distances.get(voisin, float("inf")):
                        distances[voisin] = nouveau_cout
                        precedents[voisin] = position
                        heapq.heappush(file, (nouveau_cout, voisin))

            if cible is None:
                return -1, {}, []

            # Reconstruction du chemin
            chemin = []
            position = cible

            while position not in positions:
                chemin.append(position)
                position = precedents[position]

            chemin.reverse()

            # Ajout du chemin au réseau
            precedent = positions[position]

            for position in chemin:
                numero = len(noeuds)
                noeuds[numero] = position
                positions[position] = numero

                arcs.append((precedent, numero))
                precedent = numero

        return 0, noeuds, arcs
