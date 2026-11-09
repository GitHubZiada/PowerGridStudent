
from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
        # L'entrée doit être un noeud existant
        if self.noeud_entree not in self.noeuds:
            return False
        # Parcours du réseau à partir du noeud d'entrée
        visites = {self.noeud_entree}
        a_traiter = [self.noeud_entree]
        while a_traiter:
            n = a_traiter.pop()
            for (n1, n2) in self.arcs:
                if n1 == n and n2 not in visites:
                    visites.add(n2)
                    a_traiter.append(n2)
                elif n2 == n and n1 not in visites:
                    visites.add(n1)
                    a_traiter.append(n1)
        # Valide si tous les noeuds ont été atteints
        return len(visites) == len(self.noeuds)

    def valider_distribution(self, t: Terrain) -> bool:
        # Le réseau doit d'abord être connecté à l'entrée
        if not self.valider_reseau():
            return False
        # Chaque client doit être couvert par un noeud du réseau
        cases_couvertes = set(self.noeuds.values())
        for client in t.get_clients():
            if client not in cases_couvertes:
                return False
        return True

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)

    def afficher(self) -> None:
        # TODO
        pass

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("~", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout

