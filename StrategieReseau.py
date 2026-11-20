from Terrain import Terrain, Case


class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []


class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []


class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:

        noeuds = {}
        arcs = []
        entree = t.get_entree()

        if entree == (-1, -1):
            return -1, {}, []

        # Création des noeuds du réseau
        for i in range(t.hauteur):
            for j in range(t.largeur):
                n = i * t.largeur + j
                noeuds[n] = (i, j)

        # Création des liaisons
        for i in range(t.hauteur):
            for j in range(t.largeur):
                n = i * t.largeur + j

                # Liaison horizontale
                if j + 1 < t.largeur:
                    arcs.append((n, n + 1))

                # Liaison verticale
                if j == 0 and i + 1 < t.hauteur:
                    arcs.append((n, n + t.largeur))

        # Identification du noeud d'entrée
        noeud_entree = entree[0] * t.largeur + entree[1]

        return noeud_entree, noeuds, arcs
