
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        t = Terrain()

        t.charger("terrains/t1.txt")

        self.assertEqual(t.hauteur, 10)
        self.assertEqual(t.largeur, 21)
        self.assertEqual(len(t.get_clients()), 3)
        self.assertNotEqual(t.get_entree(), (-1, -1))

        t.charger("terrains/t2.txt")

        self.assertEqual(t.hauteur, 10)
        self.assertEqual(t.largeur, 21)
        self.assertEqual(len(t.get_clients()), 7)
        self.assertNotEqual(t.get_entree(), (-1, -1))

    def test_get_entree(self):
        t = Terrain()
        t.cases = [
                [Case.VIDE, Case.VIDE, Case.ENTREE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        entree = t.get_entree()
        self.assertIsNotNone(entree)
        self.assertEqual(entree[0], 0)
        self.assertEqual(entree[1], 2)

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

